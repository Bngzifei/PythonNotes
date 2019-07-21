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