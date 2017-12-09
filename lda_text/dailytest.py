# -*- coding:utf-8 -*-
# http://blog.csdn.net/whzhcahzxh/article/details/17528261
import codecs
from gensim import corpora
from gensim.models import LdaModel
from gensim import models
from gensim import similarities
from gensim.corpora import Dictionary
import gensim
import operator
fr = open('/home/zengxiaosen/storesplitfile/part0001')
train=[]
s = 0
for line in fr.readlines():
    # line = str(list(line)[0:-1])
    line.replace('\n','')
    line.replace('|', '')
    print line
    line = line.split(' ')
    s += len(line)
    train.append(line)
print len(train)
print 'all words number: ', s
dictionary = corpora.Dictionary(train)
print 'dictionary: ', dictionary
print 'dictionary.token2id: ', dictionary.token2id
for word, index in dictionary.token2id.iteritems():
    print word + " 's id is : "+ str(index)
# through dictionary, transform the doc that show by string to the doc's vector that show by id
corpus = [dictionary.doc2bow(text) for text in train]
#print 'corpus: ', corpus

tfidf = models.TfidfModel(corpus)
#print 'tfidf: ', tfidf

corpus_tfidf = tfidf[corpus]
i = 0
for doc in corpus_tfidf:
    print 'doc_', i, ' : ', doc
    i = i + 1

# ======================
vec = [(4, 1), (12, 1)]
print 'tfidf[vec] : ', tfidf[vec]

print 'training lda model......'
lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=10)
lda2 = models.ldamulticore.LdaMulticore(corpus=corpus_tfidf, num_topics=10, id2word=None, workers=None, chunksize=2000,
                                        passes=1, batch=False, alpha='symmetric', eta=None, decay=0.5, offset=1.0,
                                        eval_every=10, iterations=50, gamma_threshold=0.001, random_state=None)
ldaOut = lda.print_topics(10)
print ldaOut
corpus_lda = lda[corpus_tfidf]
for doc in corpus_lda:
    print doc
# save model
lda.save('/home/ubuntu/code/sol/zengxiaosen/LdaModel.model')
# -----------------------------
# coming batch new file ( as a batch )
fr2 = open('/home/zengxiaosen/storesplitfile/part0002')
# output topic of each doc through the raw model
for line in fr2.readlines():
    mytrain = []
    # line = str(list(line)[0:-1])
    line.replace('\n', '')
    # get rid of '|'
    line.replace('|','')
    line = line.split(' ')
    mytrain.append(line)
    mydictionary = corpora.Dictionary(mytrain)
    mytoken2id = mydictionary.token2id
    mycorpus = [mydictionary.doc2bow(mytext) for mytext in mytrain]
    # get the new file 's topic distribution
    doc_lda = lda[mycorpus]
    # output the new file 's topic distribution
    print '---'
    besttopicIdOfcurrentFile = str()
    for topic in doc_lda:
        print topic
        mySortedTopic = topic.sort(key=operator.itemgetter(1), reverse=True)
        print "%s\t%f\n" % (lda.print_topic(topic[0][0]), topic[0][1])
        besttopic = lda.print_topic(topic[0][0])
        print 'besttopic: ', besttopic
        besttopicId = topic[0][0]
        print 'besttopicId: ', besttopicId
        besttopicIdOfcurrentFile = besttopicId
    print besttopicIdOfcurrentFile
    print '---'
fr2.close()
# --------------------the docs batch coming, and update the model
# fr2 = open('/home/zengxiaosen/storesplitfile/part0002')
# train2=[]
# s2 = 0
# for line in fr2.readlines():
#     line = line.split(' ')
#     s2 = s2 + len(line)
#     train2.append(line)
# print s2
# print len(train2)
# print 'all words number: ', s2
# dictionary2 = corpora.Dictionary(train2)
# print 'dictionary: ', dictionary2
# print 'dictionary.token2id: ', dictionary2.token2id
# print 'the adding batch......'
# for word, index in dictionary2.token2id.iteritems():
#     print word + " 's id is : "+ str(index)
# # through dictionary, transform the doc that show by string to the doc's vector that show by id
# corpus2 = [dictionary2.doc2bow(text2) for text2 in train2]
# #print 'corpus: ', corpus
# tfidf2 = models.TfidfModel(corpus2)
# #print 'tfidf: ', tfidf
#
# corpus_tfidf2 = tfidf2[corpus2]
# i = 0
# for doc in corpus_tfidf2:
#     print 'corpus_tfidf : added doc_', i, ' : ', doc
#     i = i + 1
# # topic distribution
# corpus_lda2 = lda[corpus_tfidf2]
# # get topic probability distribution for a document
# # print corpus_lda2
# for doc in corpus_lda2:
#     print 'corpus_lda2 : added doc_', i, ' : ', doc
# # update model
# # update the LDA model with additional documents
# lda.update(corpus_tfidf2)
# # get_document_topics(bow, minimum_probability=None, minimum_phi_value=None, per_word_topics=False
# # topic_list = lda.print_topics(10)
#
