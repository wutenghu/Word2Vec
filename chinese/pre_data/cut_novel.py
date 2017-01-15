# -*- coding: utf-8 -*-
# author: Dr. Wu Tenghu

import jieba

re = open('sm_noval', 'r')
wr = open('text', 'w+')

line = re.readline()
while line:
    stopkeyword = [unicode(lin.strip(),'utf-8') for lin in open('stop.txt').readlines()]
    stopkeyword.append(u'')
    cut_line = " ".join(jieba.cut(line.strip())).split(" ")
    for item in cut_line:
        if item in stopkeyword:
            pass
        else:
            wr.write(item.encode('utf-8') + ' ') 
    line = re.readline()

wr.close()
re.close()
