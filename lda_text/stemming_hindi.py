# -*- coding:utf-8 -*-
# import codecs
from gensim import corpora
from gensim.models import LdaModel
from gensim import models
from gensim import similarities
from gensim.corpora import Dictionary


suffixes = {
    1: [u"ो", u"े", u"ू", u"ु", u"ी", u"ि", u"ा"],
    2: [u"कर", u"ाओ", u"िए", u"ाई", u"ाए", u"ने", u"नी", u"ना", u"ते", u"ीं", u"ती", u"ता", u"ाँ", u"ां", u"ों", u"ें"],
    3: [u"ाकर", u"ाइए", u"ाईं", u"ाया", u"ेगी", u"ेगा", u"ोगी", u"ोगे", u"ाने", u"ाना", u"ाते", u"ाती", u"ाता", u"तीं", u"ाओं", u"ाएं", u"ुओं", u"ुएं", u"ुआं"],
    4: [u"ाएगी", u"ाएगा", u"ाओगी", u"ाओगे", u"एंगी", u"ेंगी", u"एंगे", u"ेंगे", u"ूंगी", u"ूंगा", u"ातीं", u"नाओं", u"नाएं", u"ताओं", u"ताएं", u"ियाँ", u"ियों", u"ियां"],
    5: [u"ाएंगी", u"ाएंगे", u"ाऊंगी", u"ाऊंगा", u"ाइयाँ", u"ाइयों", u"ाइयां"],
}


def hi_stem(word):
    for L in 5, 4, 3, 2, 1:
        if len(word) > L + 1:
            for suf in suffixes[L]:
                # suf = unicode(suf, 'utf-8')
                # suf.encode('utf-8')
                # try:
                #     suf = suf.encode('utf-8')
                #     # word = word.encode('utf-8')
                # except Exception, e:
                #     print suf
                #     continue
                # print suf, word
                #word = unicode(word, 'utf-8')
                if word.endswith(suf):
                    return word[:-L]
    return word

if __name__ == "__main__":
    fr = open('/home/zengxiaosen/storesplitfile/write.txt')
    train = []
    s = 0
    for line in fr.readlines():
        # line = str(list(line)[0:-1])
        if len(line) < 10:
            continue
        line = line.replace('\n', '').replace('|', '')
        # line.replace('|', '')
        # print line
        line = line.split(' ')
        stemmed_line = [hi_stem(word) for word in line]
        utf_line = []

        for word in line:
            try:
                utf_line.append(unicode(word.encode('utf-8'), 'utf-8'))
            except Exception, e:
                continue


                # print len(line)
        if (len(line) == 1):
            print line
            # print len(stemmed_line)
            # print len(utf_line)
            # break
            # counter[w if isinstance(w, unicode) else unicode(w, 'utf-8')] += 1
            s += len(stemmed_line)
            # try:
            #     line = unicode(line, 'utf-8')
            # except:
            #     continue
        train.append(stemmed_line)
    print len(train)
    print 'all words number: ', s
    dictionary = corpora.Dictionary(train)
    # print 'dictionary: ', dictionary
    print 'dictionary.token2id: ', dictionary.token2id
    # for word, index in dictionary.token2id.iteritems():
    #    print word + " 's id is : "+ str(index)
    # through dictionary, transform the doc that show by string to the doc's vector that show by id
    corpus = [dictionary.doc2bow(text) for text in train]
    # print 'corpus: ', corpus

    tfidf = models.TfidfModel(corpus)
    # print 'tfidf: ', tfidf

    corpus_tfidf = tfidf[corpus]
    i = 0
    # for doc in corpus_tfidf:
    #    print 'doc_', i, ' : ', doc
    #    i = i + 1

    # ======================
    vec = [(4, 1), (12, 1)]
    # print 'tfidf[vec] : ', tfidf[vec]

    # print corpus_tfidf
    lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=100)
    # ldaOut = lda.print_topics(500)
    # fout = open('lda_out', 'a')
    # print >> fout, ldaOut
    corpus_lda = lda[corpus_tfidf]
    # for doc in corpus_lda:
    #    print doc
    # save model
    lda.save('/home/zengxiaosen/storesplitfile/LdaModel100.model')