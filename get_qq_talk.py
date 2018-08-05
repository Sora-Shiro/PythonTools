"""
You need a qq.txt and in.txt to run this script
"""

import re
import os

pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"

QQ_NUMS = []

if_write = False

result_str = ""

with open("qq.txt", "r") as qq_file:
    lines = qq_file.readlines()
    for line in lines:
        final = line.replace("\n", "")
        QQ_NUMS.append(final)

with open("in.txt", "r") as in_file:
    lines = in_file.readlines()
    for line in lines:
        m = re.match(pattern, line, flags=0)
        if m:
            left = line.find("(")
            right = line.find(")")
            qq_num = line[left+1:right]
            if qq_num in QQ_NUMS:
                if_write = True
            else:
                if_write = False
        if if_write:
            with open("out.txt", "a") as out_file:
                out_file.write(line)


