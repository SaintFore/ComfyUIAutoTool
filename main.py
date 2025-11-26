import argparse
from soul_painter import SoulPainter


def main():
    parser = argparse.ArgumentParser(description="SoulPainter - AI批量绘图")

    parser.add_argument("--ip", type=str, default="192.168.31.128", help="ComfyUI地址")
    parser.add_argument("--batch", type=int, default=1, help="每个想法绘制张数")
    parser.add_argument("--out", type=str, default="./images/", help="图像输出目录")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", type=str, help="创意列表文件路径 (.txt)")
    group.add_argument("--subject", type=str, help="直接输入单个创意主题")

    args = parser.parse_args()

    painter = SoulPainter(args.ip, 8188, "./comfyUI.json")

    ideas = []
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            ideas = [line.strip() for line in f.readlines() if line.strip()]
    elif args.subject:
        ideas = [args.subject]

    extra_prompt = "masterpiece, best quality, amazing quality, very awa,absurdres,newest,very aesthetic,depth of field, highres, (chiaroscuro,high contrast:0.5),(sunbeam), Nijimixa2nime"

    if len(ideas):
        print(f"发现{len(ideas)}个创意，开始批量生产")
        for index, idea in enumerate(ideas):
            for i in range(args.batch):
                print(
                    f"\n[任务 {index*args.batch + i + 1} / {len(ideas) * args.batch}]，主题：{idea}"
                )
                prompt = painter.generate_prompt(idea, extra_prompt=extra_prompt)
                # print(prompt)
                # todo save prompt
                save_name = painter.draw(prompt, output_dir=args.out)
                if save_name:
                    print(f"文件{save_name}已保存在{args.out}文件夹下")
                else:
                    print("画图失败")
    else:
        print("先想点想法吧")


if __name__ == "__main__":
    main()
