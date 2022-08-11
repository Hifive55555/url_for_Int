# -*- coding:utf-8 -*-

# URL_FOR INTERPRETER 是用于将标准html文件转义为路径为url_for的html文件, 方便flask开发者快速添加url_for重定向
# 开发者: Hifive; GitHub: Hifive55555
# Version: 2.0.1 Beta 注释版
# 此版本包括由Tk编写的UI程序、cmd程序、以及API接口 (Python库)

# 更新日志
# 1.0.0 Beta 2022/1 UFI横空出世，推出核心功能
# 1.1.0 Beta 2022/1 增加UI界面
# 2.0.1 Beta 2022/8/5 重修代码，增加注释，逻辑业务分离
from url_for_int.interpreter import int_main, file_catcher
from url_for_int.int_gui import GUI

name = "url_for_int"


def start_gui():
    root = GUI()
    root.mainloop()


if __name__ == "__main__":
    start_gui()
