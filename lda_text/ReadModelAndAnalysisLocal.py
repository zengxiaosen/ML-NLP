from gensim.models.ldamodel import LdaModel
from gensim import corpora
from gensim import models
from gensim.corpora import Dictionary

import operator

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
fr = open('/home/zengxiaosen/storesplitfile/write.txt')
train = []
s = 0
s1 = 0
for line in fr.readlines():
    # line = str(list(line)[0:-1])
    if len(line) < 10:
        continue
    line = line.replace('\n', '').replace('|', '')
    #line.replace('|', '')
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
lda = LdaModel.load('/home/zengxiaosen/model_LDA.model')
print '--'
print type(train)
mydictionary = dict([(v, k) for (k, v) in corpora.Dictionary(train).token2id.items()])
#print mydictionary
print type(mydictionary)
lda.show_topic(10)
for topicid in range(0, 10, 1):
    mylist = lda.get_topic_terms(topicid, topn=10)
    # print mylist
    print topicid
    for temp in mylist:
        print type(temp)
        key = temp[0]
        print 'key:',key
        value = temp[1]

        print key, type(key), mydictionary.get(key, 'None')
        token = mydictionary.get(key, 'None')
        myfr = open('/home/zengxiaosen/zengxiaosen/pythonTokensCollection/all.txt' % topicid, 'a+')
        myfr.write(topicid)
        myfr.write(',')
        myfr.write(token)
        myfr.write(',')
        myfr.write(value)
        myfr.write('\n')
        myfr.close()
        # try:
        #     key = unicode(key, 'utf-8')
        # except Exception, e:
        #     continue
        # mytoken = mydictionary.get(key)
        # # mytoken = mydictionary[key]
        # print 'token:'
        # print mytoken
        # print "p:"
        # print value
exit(0)


# ---------------------------------------------------------------
fr2 = open('/home/zengxiaosen/textfile.txt')
# output topic of each doc through the raw model

for line in fr2.readlines():
    mytrain = []
    # line = str(list(line)[0:-1])
    line.replace('\n', '')
    # get rid of '|'
    line.replace('|','')
    line = line.split(' ')
    # print 'line:------------------', str(' '.join(line))
    myline = str(' '.join(line))
    mytrain.append(line)
    mydictionary = corpora.Dictionary(mytrain)
    print '---'
    print mydictionary
    print '---'
    mytoken2id = mydictionary.token2id
    print type(mytoken2id)

    mycorpus = [mydictionary.doc2bow(mytext) for mytext in mytrain]
    mytext = mytrain[0]
    # print 'mytext: ', mytext
    # get the new file 's topic distribution
    doc_lda = lda[mycorpus]
    # output the new file 's topic distribution
    print '---'
    besttopicIdOfcurrentFile = str()
    for topic in doc_lda:
        # print topic
        mySortedTopic = topic.sort(key=operator.itemgetter(1), reverse=True)
        # print "%s\t%f\n" % (lda.print_topic(topic[0][0]), topic[0][1])

        besttopic = lda.print_topic(topic[0][0])
        # print 'besttopic: ', besttopic
        besttopicId = topic[0][0]
        # print 'besttopicId: ', besttopicId
        besttopicIdOfcurrentFile = besttopicId
    print besttopicIdOfcurrentFile
    print '---'
    # output the myline to the specific file that matching besttopicIdOfcurrentFile
    myfr = open('/home/zengxiaosen/zengxiaosen/pythonTest/%s.txt' %besttopicIdOfcurrentFile, 'a+')
    myfr.write(myline)
    myfr.write('\n')
    myfr.close()

fr2.close()