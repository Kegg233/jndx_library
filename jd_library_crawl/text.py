#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: kyx
@time: 2020/2/4 13:31
"""
import re

url = "href=item.php?marc_no=786c515044585968415977546d534a4b326a4c7150513d3d&list=1"
url2 = re.findall(r"item\.php\?marc_no=.+list=1", url)
print(url2)
