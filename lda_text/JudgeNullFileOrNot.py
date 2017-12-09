import os
dirname = '/home/zengxiaosen/'
count = 0
count1 = 0
for filename in os.listdir(dirname):
    # mystr = dirname.join(filename)
    mystr = dirname + filename
    count1 = count1 + 1
    # print('%d Bytes' % (os.path.getsize(mystr)))
    if os.path.getsize(mystr) > 1:
        #print('%d Bytes' % (os.path.getsize(mystr)))
        count = count + 1
# print "not null rate: " + count/count1*100 + "%"
rate = float(count) / float(count1)
print count
print count1
print rate
