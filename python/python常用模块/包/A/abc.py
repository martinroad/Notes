# coding=utf-8

import apython  # 从当前目录引入 apython.py
from ..B import he     # 从当前目录引入与之平行的目录下的 he.py

test = 'Test' + apython.test() + '-' + he.test