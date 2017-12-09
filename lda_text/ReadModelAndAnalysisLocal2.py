from gensim.models.ldamodel import LdaModel
from gensim import corpora
from gensim import models
import operator
lda = LdaModel.load('/home/zengxiaosen/model_LDA.model')
# ---------------------------------------------------------------
#for topicid in range(0, 300, 1):
#    lda.get_topic_terms(topicid, topn=10)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
fr = open('/home/zengxiaosen/textfile.txt')
train = []
s = 0
s1 = 0
for line in fr.readlines():
    # line = str(list(line)[0:-1])
    if len(line) < 10:
        continue
    line = line.replace('\n', '').replace('|', '')
    line.replace('|', '')
    # print line
    line = line.split(' ')
    utf_line = []

    for word in line:
        try:
            print 'A', word
            utf_line.append(unicode(word, 'utf-8'))
            utf_line.append(word)
        except Exception, e:
            print 'Exception'
            print e, word, line
    print len(line)
    if(len(line) == 1):
        print line
    #print len(stemmed_line)
    print len(utf_line)
    #break
    # counter[w if isinstance(w, unicode) else unicode(w, 'utf-8')] += 1
    s += len(utf_line)
    # try:
    #     line = unicode(line, 'utf-8')
    # except:
    #     continue
    print type(utf_line)
    #train.extend(utf_line)
    #train.insert(s1, utf_line)
    s1 = s1 + 1
    train.append(utf_line)
print '--'
print type(train)
mydictionary = dict([(v, k) for (k, v) in corpora.Dictionary(train).token2id.items()])
#print mydictionary
print type(mydictionary)
lda.show_topic(10)
myfr = open('/home/zengxiaosen/topic_toke_p_statistic.csv', 'a')

for topicid in range(0, 10, 1):
    mylist = lda.get_topic_terms(topicid, topn=10)
    # print mylist
    # topicid = unicode(topicid, 'utf-8')

    for temp in mylist:
        print type(temp)
        key = temp[0]
        # try:
        #     key = unicode(key, 'utf-8')
        # except Exception, e:
        #     continue
        print 'key:',key
        value = temp[1]
        # try:
        #     value = unicode(value, 'utf-8')
        # except Exception, e:
        #     continue
        print key, type(key), mydictionary.get(key, 'None')
        token = mydictionary.get(key, 'None')
        # try:
        #     token = unicode(token.u, 'utf-8')
        # except Exception, e:
        #     continue
        myfr.write(str(topicid))
        myfr.write(',')
        myfr.write(token)
        myfr.write(',')
        myfr.write(str(value))
        myfr.write('\n')
myfr.close()

