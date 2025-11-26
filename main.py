from soul_painter import SoulPainter


def main():
    painter = SoulPainter("192.168.31.128", 8188, "./comfyUI.json")
    idea_file = "idea.txt"
    with open(idea_file, "r", encoding="utf-8") as f:
        ideas = [line.strip() for line in f.readlines() if line.strip()]

    batch = 4

    extra_prompt = "masterpiece, best quality, amazing quality, very awa,absurdres,newest,very aesthetic,depth of field, highres, (chiaroscuro,high contrast:0.5),(sunbeam), Nijimixa2nime"

    if len(ideas):
        print(f"发现{len(ideas)}个创意，开始批量生产")
        for index, idea in enumerate(ideas):
            for i in range(batch):
                print(
                    f"\n[任务 {index*batch + i + 1} / {len(ideas) * batch}]，主题：{idea}"
                )
                prompt = painter.generate_prompt(idea, extra_prompt=extra_prompt)
                # print(prompt)
                # todo save prompt
                save_name = painter.draw(prompt)
                if save_name:
                    print(f"文件{save_name}已保存在images文件夹下")
                else:
                    print("画图失败")
    else:
        print("先想点想法吧")


if __name__ == "__main__":
    main()
