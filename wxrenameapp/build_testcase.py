#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 20:52:18 2015

@author: ronald
"""

import os
import glob

if __name__ == "__main__":
    if os.path.exists("./testcase"):
        for f in glob.glob("./testcase/*"):
            os.remove(f)
    else:
        os.mkdir("testcase", 0755)
    for i in range(1, 11):
        f = open("./testcase/case-%02d.txt" % i, 'w')
        f.close()
        f = open("./testcase/case-%02d.md" % i, 'w')
        f.close()
        f = open("./testcase/htmlcase-%02d.html" % i, 'w')
        f.close()
