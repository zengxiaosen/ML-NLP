# -*- coding:utf-8 -*-
# import codecs
from gensim import corpora
from gensim.models import LdaModel
from gensim import models
from gensim import similarities
from gensim.corpora import Dictionary
import gensim
import operator


hindi_stop_words = [
    'बावजूद',
    'आकस्मिक',
    'high...',
    '2017',
    'खत्म',
    'वर्ष',
    'बन',
    'उसके',
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
fd = file( "/home/ubuntu/code/sol/zengxiaosen/cal.txt", "r")
fr2 = open('/home/ubuntu/code/sol/zengxiaosen/30daysfilewithoutsw.txt', 'w')
fr = open('/home/ubuntu/code/sol/zengxiaosen/textfileOf30days.txt')
train=[]
s = 0
for line in fd.readlines():
    hindi_stop_words.append(line)
for line in fr.readlines():
    str = ''
    # line = str(list(line)[0:-1])
    line.replace(']', '')
    line.replace('[', '')
    line.replace('।', ' ')
    line.replace('-', '')
    line.replace('...', '')
    line.replace('<200d>', '')
    line.replace(')', '')
    line.replace('(', '')
    line.replace('1', '')
    line.replace('2', '')
    line.replace('3', '')
    line.replace('4', '')
    line.replace('5', '')
    line.replace('6', '')
    line.replace(',', '')
    line.replace('.', '')
    line.replace('7', '')
    line.replace('8', '')
    line.replace('9', '')
    line.replace('|', '')
    line.replace('<200d>', '')
    line.replace('\'', '')
    line.replace(':', '')


    line.replace('\n', '')
    line.replace('|', '')
    # print line
    # try:
    #     line = unicode(line, 'utf-8')
    # except:
    #     continue
    line = line.split(' ')
    # get rid of stop word
    for temp in line:
        if temp in hindi_stop_words:
            line.remove(temp)
    str = ' '.join(line)
    str += '\n'
    fr2.write(str)



fr.close()
fr2.close()