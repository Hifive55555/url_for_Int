import setuptools

with open("D:\\Projects\\url_for_Int\\README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="url_for_int",
    version="2.2.4",
    author="Hifive",
    author_email="2019912635@qq.com",
    description="帮助flask框架中将普通HTML文档转义为url-for的文档",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hifive55555/url_for_Int",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
