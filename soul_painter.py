"""
File: ComfyUI/soul_painter.py
Description: 绘图类
Author: Soleil
Date: 2025-11-26
"""

import json
import os
import random
import requests
import uuid
import websocket
from typing import Optional
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


class SoulPainter:
    """绘图类

    负责调用comfyUI的api，以及google的llm生成prompt实现图像绘制与下载到本地

    Attribute:
        comfyui_ip: comfyui的远程ip地址
        comfyui_port: comfyui的端口号，默认是8188
        workflow_path: 通过api下载得到的工作流
    """

    def __init__(self, comfyui_ip: str, comfyui_port: int, workflow_path: str) -> None:
        """
        初始化SoulPainter实例，获取.env的API_KEY
        """
        self.comfyui_ip = comfyui_ip
        self.comfyui_port = comfyui_port
        self.comfyui_addr = f"{comfyui_ip}:{comfyui_port}"
        self.workflow_path = workflow_path
        load_dotenv()

    def generate_prompt(
        self, subject: str, extra_prompt: str = "", model: str = "gemini-2.5-flash"
    ) -> str:
        """
        调用gemini生成prompt
        """
        llm = ChatGoogleGenerativeAI(model=model)
        template = PromptTemplate.from_template(
            """
            你是一个资深的 Stable Diffusion/ComfyUI 提示词专家。
            请根据以下主题生成一段英文 Prompt：
            主题：{subject}
            
            要求：
            1. 只要英文关键词，用逗号分隔。
            2. 包含画质词（如 8k, masterpiece, photorealistic）。
            3. 不要包含任何解释性语句，直接输出 Prompt。
            """
        )
        chain = template | llm | StrOutputParser()
        prompt = chain.invoke({"subject": subject})
        if extra_prompt:
            prompt = f"{prompt}, {extra_prompt}"
        return prompt

    def draw(self, prompt: str, output_dir: str = "./images/") -> Optional[str]:
        """
        调用comfyUI在服务器生成图像，并下载回本地
        """
        comfyui_frame = self._open_comfyUI_api(output_dir)

        comfyui_frame["prompt"]["3"]["inputs"]["text"] = prompt
        comfyui_frame["prompt"]["5"]["inputs"]["seed"] = random.randint(1, 10**15)

        client_id = str(uuid.uuid4())
        comfyui_frame["client_id"] = client_id

        ws = websocket.WebSocket()
        ws_url = f"ws://{self.comfyui_addr}/ws?clientId={client_id}"
        ws.connect(ws_url)

        response = self._comfyUI_post(comfyui_frame=comfyui_frame)

        image_name = None

        print("监听comfyUI进度")
        print("-" * 20)
        if response.status_code == 200:
            while True:
                out = ws.recv()
                if isinstance(out, str):
                    message = json.loads(out)
                    end, image_name = self._message_type(
                        message=message,
                        comfyui_frame=comfyui_frame,
                        image_name=image_name,
                    )
                    if end:
                        break
        else:
            print(f"任务提交失败，{response.status_code}")
        ws.close()

        try:
            if image_name:
                download_url = (
                    f"http://{self.comfyui_addr}/view?filename={image_name}&type=output"
                )
                save_path = os.path.join(output_dir, image_name)
                print(f"正在下载图片：{image_name}")
                with requests.get(download_url) as r:
                    print(r)
                    with open(save_path, "wb") as image:
                        image.write(r.content)
                return save_path

        except NameError:
            print("未获取到图片名称")
            return None

    def _open_comfyUI_api(self, output_dir: str) -> dict:
        """将下载下来的节点api打开"""
        os.makedirs(output_dir, exist_ok=True)
        with open(self.workflow_path, "r", encoding="utf-8") as f:
            comfyui_frame = json.load(f)

        return comfyui_frame

    def _comfyUI_post(self, comfyui_frame: dict) -> requests.Response:
        """像comfyUI发送post请求，开始绘图"""
        url = f"http://{self.comfyui_addr}/prompt"

        payload = comfyui_frame
        response = requests.post(url, json=payload)

        return response

    def _message_type(self, message, comfyui_frame, image_name) -> tuple[bool, str]:
        """处理ws的信息"""
        msg_type = message["type"]  # print(f"收到消息，消息类型：{message['type']}")
        if msg_type == "status":
            print(
                f"队列还有{message['data']['status']['exec_info']['queue_remaining']}未画"
            )
        elif msg_type == "execution_start":
            print("开始绘画")
        elif msg_type == "executing":
            node = message["data"]["node"]
            node_type = comfyui_frame["prompt"][node]["class_type"]
            print(f"正在执行节点{node_type}")
        elif msg_type == "progress":
            current_step = message["data"]["value"]
            max_steps = message["data"]["max"]
            print(f"进度：{current_step/max_steps}")
        elif msg_type == "executed":
            image_node = message["data"]["output"]
            if "images" in image_node:
                image_name = image_node["images"][0]["filename"]
        elif msg_type == "execution_success":
            print("绘图完成")
            return True, image_name
        return False, image_name


if __name__ == "__main__":
    painter = SoulPainter("192.168.31.128", 8188, "./comfyUI.json")
    subject = "湖中落日"
    extra_prompt = "masterpiece, best quality, amazing quality, very awa,absurdres,newest,very aesthetic,depth of field, highres, (chiaroscuro,high contrast:0.5),(sunbeam), Nijimixa2nime"
    print("正在构思prompt")
    prompt = painter.generate_prompt(subject, extra_prompt=extra_prompt)
    print(prompt)
    print("*" * 50)
    print("正在绘图")
    save_name = painter.draw(prompt)
    if save_name:
        print(f"文件{save_name}已保存在images文件夹下")
    else:
        print("画图失败")
