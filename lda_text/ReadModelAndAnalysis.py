from gensim.models.ldamodel import LdaModel
from gensim import corpora
from gensim import models
import operator
lda = LdaModel.load('/home/ubuntu/code/sol/zengxiaosen/LdaModel.model')
for topicid in range(0, 300, 1):
    mylist = lda.get_topic_terms(topicid, topn=10)
    print mylist

# ---------------------------------------------------------------
fr2 = open('/home/ubuntu/code/sol/zengxiaosen/textfile.txt')
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

    mytoken2id = mydictionary.token2id
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
    myfr = open('/home/ubuntu/code/sol/zengxiaosen/testclassify/%s.txt' %besttopicIdOfcurrentFile, 'a+')
    myfr.write(myline)
    myfr.write('\n')
    myfr.close()

fr2.close()