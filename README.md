# url_for_Int *v2.1.0*

### 简介
- 这是 url-for Interpreter 的开源使用版，遵循 MIT 协议。<br>
开发者：Hifive
- 它总共分为两个部分：GUI 和 API，使用方法见下
### 新版内容
2.1.0 不再是 Beta 版，去除 cmd 函数，拆分代码，使其模块化。

---

## 使用方法
### API
- 通过 `import url_for_int` 导入库，此代码会将下列类或函数一并导入
  - #### int_main 主函数
    - 输入：**origin_text:str**原始字符
    - 返回：**x:str**处理后的字符
  - #### file_catcher ：导入文件处理
    - 输入：**file_name:str**, **prefix:str**, **paths**
    - 返回：bool值，表示是否成功
  - #### GUI ：用户界面
    - 启动方式 `start_gui()` 或直接打开 \_\_init__.py 文件

### GUI
目前在 delete 函数上存在少许 bug，但不影响正常使用。
