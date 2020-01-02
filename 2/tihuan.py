import re
import os
import shutil

def replaces(string):
    # 更改显示字符
    with open("singer.html", "r", encoding="utf-8") as f:
        s = f.read()

    s2 = re.sub("&&&", string, s)
    print(s2)

    # 建立新文件
    with open("singers.html", "w", encoding="utf-8") as f:
        f.write(s2)

    # 移动并替换
    if os.path.isfile("./templates/singers.html"):
        os.remove("./templates/singers.html")
    shutil.move("singers.html", "./templates/")


def append_cmd(cmd):
    with open("cmd.txt", "w", encoding="utf-8") as f:
        f.writelines(cmd)
    pass


def read_cmd():
    with open("cmd.txt", "r", encoding="utf-8") as f:
        cmd = f.readline()

    print(cmd)
    return cmd


if __name__ == '__main__':
    # replaces("ON")
    # append_cmd("ON")
    # read_cmd()
    pass