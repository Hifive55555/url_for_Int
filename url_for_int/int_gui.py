# GUI模块

import os
import tkinter as tk
from tkinter import filedialog

from url_for_int.interpreter import file_catcher


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.files, self.folders = None, None
        self.paths = []
        self.title("Html url_for Interpreter")
        self.resizable(False, False)  # 防止用户调整尺寸
        # self.geometry("600x300")

        tk.Button(self, text='打开文件', width=20, command=self.select_file).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(self, text='打开文件夹', width=20, command=self.select_folder).grid(row=1, column=1, padx=5, pady=5)

        self.listbox = tk.Listbox(self, setgrid=True, width=60, selectmode=tk.EXTENDED)
        self.listbox.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
        # 删除选项
        delete_button = tk.Button(self, text='删除', width=10, command=self.delete)
        delete_button.grid(row=1, column=2, padx=5, pady=5)

        tk.Label(self, text="\t\t前缀").grid(row=3, column=0, pady=10)
        self.entry_text = tk.StringVar(self, value="int_")
        tk.Entry(self, textvariable=self.entry_text).grid(row=3, column=1, pady=10)

        self.check_path = tk.IntVar(self, value=1)
        c1 = tk.Checkbutton(self, text="使用原文件路径", variable=self.check_path, onvalue=1, offvalue=0)
        c1.grid(row=4, column=0, pady=10)
        tk.Button(self, text="--> 转义", command=self.trans, width=20, height=2).grid(
            row=4, column=1, columnspan=1, pady=10)

    def delete(self):
        delete_tuple = self.listbox.curselection()
        delete_list = list(delete_tuple)
        delete_list.reverse()
        # print(delete_tuple, len(self.paths))
        for item in delete_list:
            del self.paths[item]
        self.listbox.delete(first=delete_tuple[0], last=delete_tuple[-1])

    def select_file(self):
        self.files = filedialog.askopenfilenames()  # 选择打开什么文件，返回文件名
        self.inter()

    def select_folder(self):
        self.folders = filedialog.askdirectory()  # 选择打开什么文件，返回文件名
        self.inter()

    def inter(self):
        def add_path(path):
            path = os.path.abspath(path)
            if path not in self.paths:
                self.paths.append(path)
            else:
                self.listbox.delete(self.paths.index(path))

        if self.files:
            for path in self.files:
                add_path(path)
        if self.folders:
            for filepath, dirnames, filenames in os.walk(self.folders):
                for filename in filenames:
                    add_path(os.path.join(filepath, filename))
        for i in self.paths:
            self.listbox.insert(tk.END, i)

    def trans(self):
        state = None

        if self.check_path.get() == 1:
            for ori in self.paths:
                state = file_catcher(origin_file=ori, prefix=self.entry_text.get())
        else:
            save_path = filedialog.askdirectory(title="选择保存的文件夹")
            for ori in self.paths:
                state = file_catcher(ori, save_path, self.entry_text.get())
        if state:
            tk.Message(self, text="转义成功").grid()
