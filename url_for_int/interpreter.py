# 主逻辑模块

import re
import os


def int_main(origin_text: str) -> str:
    """ 主逻辑函数，每次只进行一次操作 """

    # 添加 url_for 的函数
    def add(match) -> str:
        address = match.group()
        addition = r"{{ url_for('static', filename='" + address + r"') }}"
        return addition

    # 替换目录字符
    x = re.sub(r"/?(\w[\u4E00-\u9FA5\w_-]+/)+([\u4E00-\u9FA5\w_-]+\.)+\w+\b", add, origin_text)
    return x


def file_catcher(origin_file, to_path=None, prefix="int_", if_pre=False):
    file_name, origin_path, pre_folder = decompose(origin_file)
    if not to_path:
        to_path = origin_path
    if if_pre:
        to_path = os.path.join(to_path, pre_folder)
    to_file = os.path.join(to_path, prefix + file_name)
    # 获取文件

    with open(origin_file, mode="r", encoding="utf-8") as f:
        origin_text = f.read()

    if not os.path.exists(to_path):
        os.makedirs(to_path)
        print("创建新的文件夹")

    x = int_main(origin_text)

    with open(to_file, mode="w", encoding="utf-8") as f:
        f.write(x)
        print(f"{origin_file}  转义至  {to_file} 成功\n")
        return True


def decompose(content: str):
    """ 将文件路径拆解 """
    file, path = "", ""
    content = content.split("\\")
    file = content[-1]
    pre_folder = content[-2]
    del content[-1]
    content[0] += "\\"
    for i in content:
        path = os.path.join(path, i)
    return file, path, pre_folder
