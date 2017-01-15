# -*- coding: utf-8 -*-
# Author: Tenghu Wu
# Date: 2017-Jan-10
import jieba

if __name__ == '__main__':
    r = open('file_name', 'r')
    w = open('text', 'w+')

    line = re.readline()
    while line:
        stopkeyword = [unicode(lin.strip(),'utf-8') for lin in open('stop.txt').readlines()]
        stopkeyword.append(u'')
        cut_line = " ".join(jieba.cut(line.strip())).split(" ")
        for item in cut_line:
            if item in stopkeyword:
                pass
            else:
                w.write(item.encode('utf-8') + ' ') 
        line = r.readline()

    w.close()
    r.close()
