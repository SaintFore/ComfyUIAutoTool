from soul_painter import SoulPainter


def main():
    painter = SoulPainter("192.168.31.128", 8188, "./comfyUI.json")
    subject = "湖中落日"
    print("正在构思prompt")
    prompt = painter.generate_prompt(subject)
    print(prompt)
    print("*" * 50)
    print("正在绘图")
    save_name = painter.draw(prompt)
    if save_name:
        print(f"文件{save_name}已保存在images文件夹下")
    else:
        print("画图失败")


if __name__ == "__main__":
    main()
