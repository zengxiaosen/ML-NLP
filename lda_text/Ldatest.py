# -*- coding:utf-8 -*-
# import codecs
from gensim import corpora
from gensim.models import LdaModel
from gensim import models
from gensim import similarities
from gensim.corpora import Dictionary
import gensim
import operator

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


hindi_stop_words = [
    'के',
    'का',
    'एक',
    'में',
    'की',
    'है',
    'यह',
    'और',
    'से',
    'हैं',
    'को',
    'पर',
    'इस',
    'होता',
    'कि',
    'जो',
    'कर',
    'मे',
    'गया',
    'करने',
    'किया',
    'लिये',
    'अपने',
    'ने',
    'बनी',
    'नहीं',
    'तो',
    'ही',
    'या',
    'एवं',
    'दिया',
    'हो',
    'इसका',
    'था',
    'द्वारा',
    'हुआ',
    'तक',
    'साथ',
    'करना',
    'वाले',
    'बाद',
    'लिए',
    'आप',
    'कुछ',
    'सकते',
    'किसी',
    'ये',
    'इसके',
    'सबसे',
    'इसमें',
    'थे',
    'दो',
    'होने',
    'वह',
    'वे',
    'करते',
    'बहुत',
    'कहा',
    'वर्ग',
    'कई',
    'करें',
    'होती',
    'अपनी',
    'उनके',
    'थी',
    'यदि',
    'हुई',
    'जा',
    'ना',
    'इसे',
    'कहते',
    'जब',
    'होते',
    'कोई',
    'हुए',
    'व',
    'न',
    'अभी',
    'जैसे',
    'सभी',
    'करता',
    'उनकी',
    'तरह',
    'उस',
    'आदि',
    'कुल',
    'एस',
    'रहा',
    'इसकी',
    'सकता',
    'रहे',
    'उनका',
    'इसी',
    'रखें',
    'अपना',
    'पे',
    'उसके'
]

hindi_stop_words1 = [
    u'के',
    u'का',
    u'एक',
    u'में',
    u'की',
    u'है',
    u'यह',
    u'और',
    u'से',
    u'हैं',
    u'को',
    u'पर',
    u'इस',
    u'होता',
    u'कि',
    u'जो',
    u'कर',
    u'मे',
    u'गया',
    u'करने',
    u'किया',
    u'लिये',
    u'अपने',
    u'ने',
    u'बनी',
    u'नहीं',
    u'तो',
    u'ही',
    u'या',
    u'एवं',
    u'दिया',
    u'हो',
    u'इसका',
    u'था',
    u'द्वारा',
    u'हुआ',
    u'तक',
    u'साथ',
    u'करना',
    u'वाले',
    u'बाद',
    u'लिए',
    u'आप',
    u'कुछ',
    u'सकते',
    u'किसी',
    u'ये',
    u'इसके',
    u'सबसे',
    u'इसमें',
    u'थे',
    u'दो',
    u'होने',
    u'वह',
    u'वे',
    u'करते',
    u'बहुत',
    u'कहा',
    u'वर्ग',
    u'कई',
    u'करें',
    u'होती',
    u'अपनी',
    u'उनके',
    u'थी',
    u'यदि',
    u'हुई',
    u'जा',
    u'ना',
    u'इसे',
    u'कहते',
    u'जब',
    u'होते',
    u'कोई',
    u'हुए',
    u'व',
    u'न',
    u'अभी',
    u'जैसे',
    u'सभी',
    u'करता',
    u'उनकी',
    u'तरह',
    u'उस',
    u'आदि',
    u'कुल',
    u'एस',
    u'रहा',
    u'इसकी',
    u'सकता',
    u'रहे',
    u'उनका',
    u'इसी',
    u'रखें',
    u'अपना',
    u'पे',
    u'उसके'
]



suffixes = {
    1: ["ो", "े", "ू", "ु", "ी", "ि", "ा"],
    2: ["कर", "ाओ", "िए", "ाई", "ाए", "ने", "नी", "ना", "ते", "ीं", "ती", "ता", "ाँ", "ां", "ों", "ें"],
    3: ["ाकर", "ाइए", "ाईं", "ाया", "ेगी", "ेगा", "ोगी", "ोगे", "ाने", "ाना", "ाते", "ाती", "ाता", "तीं", "ाओं", "ाएं", "ुओं", "ुएं", "ुआं"],
    4: ["ाएगी", "ाएगा", "ाओगी", "ाओगे", "एंगी", "ेंगी", "एंगे", "ेंगे", "ूंगी", "ूंगा", "ातीं", "नाओं", "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां"],
    5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा", "ाइयाँ", "ाइयों", "ाइयां"],
}

def hi_stem(word):
    for L in 5, 4, 3, 2, 1:
        if len(word) > L + 1:
            for suf in suffixes[L]:
                # suf = unicode(suf, 'utf-8')
                # suf.encode('utf-8')
                # print suf, word
                #word = unicode(word, 'utf-8')
                if word.endswith(suf):
                    return word[:-L]
    return word


if __name__ == '__main__':
    fr = open('/home/zengxiaosen/storesplitfile/write.txt')
    train = []
    s = 0
    for line in fr.readlines():
        # line = str(list(line)[0:-1])
        if len(line) < 10:
            continue
        line = line.replace('\n', '').replace('|', '')
        line.replace('|', '')
        # print line
        line = line.split(' ')
        # stemmed_line = [hi_stem(word) for word in line]
        utf_line = []
        for word in line:
            try:
                utf_line.append(unicode(word, 'utf-8'))
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
        train.append(utf_line)
    # print len(train)
    # print 'all words number: ', s
    dictionary = corpora.Dictionary(train)
    # print 'dictionary: ', dictionary
    # print 'dictionary.token2id: ', dictionary.token2id
    # for word, index in dictionary.token2id.iteritems():
    #     print word + " 's id is : " + str(index)
    # through dictionary, transform the doc that show by string to the doc's vector that show by id
    corpus = [dictionary.doc2bow(text) for text in train]
    # print 'corpus: ', corpus

    tfidf = models.TfidfModel(corpus)
    # print 'tfidf: ', tfidf

    corpus_tfidf = tfidf[corpus]
    i = 0
    # for doc in corpus_tfidf:
    #     print 'doc_', i, ' : ', doc
    #     i = i + 1

    # ======================
    vec = [(4, 1), (12, 1)]
    # print 'tfidf[vec] : ', tfidf[vec]

    print 'training lda model......'
    # lda = LdaModel(corpus, num_topics=50, alpha='auto', eval_every=5)
    lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=300, alpha='auto', eval_every=10)
    # print "1"
    # print lda.log_perplexity(corpus_tfidf)
    # ldaOut = lda.print_topics(50)
    # print ldaOut
    # corpus_lda = lda[corpus_tfidf]
    # for doc in corpus_lda:
    #     print doc
    # save model
    lda.save('/home/zengxiaosen/model_LDA.model')