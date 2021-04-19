
# //! python引入模块报错ValueError: attempted relative import beyond top-level package

import sys,os
# sys.path.append(os.path.dirname(__file__) + os.sep + '../') 

print(sys.path)

from A import a1,a2
from B import b1     # 从当前目录引入与之平行的目录下的 he.py

test = a1.test + a2.test() + b1.test
print(test)