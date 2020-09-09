# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-05-20 17:42:02
# @Last Modified by:   Marte
# @Last Modified time: 2019-05-20 17:53:08

import json

s = {
"type":"qcow2",
"path":"8551982286028#vm-disk-1.qcow2",
"id":"123"
}




c = json.dumps(s)

print(c)

# json文件转字典
with open("/sf/data/local/TESTCASE/HW_Platform/package.json", "r+") as fd:
    res = json.load(fd)
    # res = fd.read()

df = {
    "1": 1
}

# 写入一个字典,列表类型  字典或者列表生成.json文件
with open("xx.txt", "w") as fp:
    json.dump(df, fp)
