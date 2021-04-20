'''
步骤：
    1、去 https://choosealicense.com/ 拷贝license，将 https://choosealicense.com/licenses/mit/ 这里的 MIT icense 拷贝到 LICENSE 这个文件中
    2、设置 setup.py 的信息
    3、在本地进行安装测试：python3 setup.py install
    4、发布到 https://pypi.org/ 这个网站上，供别人安装使用
    5、检查安装最新的 setuptools wheel，命令为：python3 -m pip install --user --upgrade setuptools whell
    6、发布包的时候，还需要一个专门的工具：https://pypi.org/project/twine/，使用命令安装：pip install twine
    7、测试的时候，要发布到 https://test.pypi.org/ 上面，测试账号：martin5257，密码：Martin13798764075，邮箱：martinroad5257@gmail.com
    8、打包和分发项目：https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-py
    9、在该项目目录下执行：python3 setup.py sdist bdist_wheel
    10、发布到test.pypi，命令：twine upload --repository-url https://test.pypi.org/test_package，然后输入test.pypi的账号：martin5257，密码：Martin13798764075

'''



# //! 安装包命令：python3 setup.py install

import setuptools
import os
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))) # 说明包的路径特点，和第18行必须配合着写

with open('README.md', 'rb') as file:
    long_description = file.read()

setuptools.setup(
    name='testproject', # 发布到pipy后所显示的名称
    version='0.0.1',
    author='martin',
    author_email='734585846@qq.com',
    description='test puplish to pipy',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    py_modules = ['longspeak'],
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
)    
