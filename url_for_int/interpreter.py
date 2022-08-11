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


def file_catcher(file_name, prefix, *paths):
    # 解析路径（获取路径origin 及 生成路径to）
    origin_path = paths[0]
    if paths[1]:
        to_path = paths[1]
    else:
        to_path = origin_path
    del paths

    # 获取文件
    with open(os.path.join(origin_path, file_name), mode="r", encoding="utf-8") as f:
        origin_text = f.read()

    if not os.path.exists(to_path):
        os.makedirs(to_path)
        print("创建新的文件夹")

    x = int_main(origin_text)

    with open(os.path.join(to_path, prefix + file_name), mode="w", encoding="utf-8") as f:
        f.write(x)
        return True
