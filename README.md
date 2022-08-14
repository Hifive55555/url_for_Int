# url_for_Int *v2.2.3*

### 简介
- 这是 url-for Interpreter 的开源使用版，遵循 MIT 协议。<br>
开发者：Hifive
- Github: https://github.com/Hifive55555/url_for_Int <br>
Pypi: https://pypi.org/project/url-for-int
- 它总共分为两个部分：GUI 和 API，使用方法见下
### 新版内容
2.2.3 增加日志框显示转义日志，覆盖原文件会弹出提示框
2.2.2 修复了增加文件、文件夹、删除文件的listbox的bug。<br>

---

# 使用方法
## API
### 函数及类
- #### int_main 主函数
  - 输入：**origin_text**原始字符
  - 返回：**x:str**处理后的字符
- #### file_catcher ：导入文件处理
  - 输入：**origin_file**, **to_path**, **prefix**, **if_pre**
  - to_path默认为None，表示生成于原文件目录。若指定目录，则会加入pre_folder
  - prefix默认为"int_"
  - if_pre默认为False。若为True，则文件目录加上pre_folder
  - 返回：bool值，表示是否成功
- #### GUI ：用户界面
  - GUI是一个继承了tk.Tk的窗口类

### 教程
- 安装：`pip install url_for_int`
- 导入库：`from url_for_int import start_gui, file_catcher, int_main`
- 启用GUI界面：`start_gui()` 或直接运行 \_\_init__.py 文件
- 转义一个文件
  - 转录到当前文件夹：`file_catcher("test.html")`
  - 转录到指定文件夹：`file_catcher("test.html", "D:/test")`
  - 转录并覆盖原文件：`file_catcher("test.html", prefix="")`
  - 转录并指定前缀：`file_catcher("test.html", prefix="xxx-")`
  - 转录并增加pre_folder：`file_catcher("test.html", "D:/test", if_pre=True)`
- 转义一串字符
  ```python
  content = "xxx"
  after = int_main(content)
  ```