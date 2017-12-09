# -*- coding:utf-8 -*-
import string

fr = open('/home/zengxiaosen/storesplitfile/part0001')
train=[]
s = 0
for line in fr.readlines():
    # line = str(list(line)[0:-1])
    line.replace('\n','')
    line.replace('|', '')
    print line
    try:
        line = unicode(line, 'utf-8')
    except:
        continue
    line = line.split(' ')
    # counter[w if isinstance(w, unicode) else unicode(w, 'utf-8')] += 1
    s += len(line)
    train.append(line)
print len(train)
print 'all words number: '