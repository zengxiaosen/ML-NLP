# -*- coding:utf-8 -*-
import sys,os
# split  to 15 M
kilobytes = 1024
megabytes = kilobytes * 1000
chunksize = int(200*megabytes)

def split(fromfile, todir, chunksize=chunksize):
    if not os.path.exists(todir): # check whether todir exists or not
        os.mkdir(todir)
    else:
        for fname in os.listdir(todir):
            os.remove(os.path.join(todir,fname))
    partnum = 0
    inputfile = open(fromfile, 'rb') #open the fromfile
    while True:
        chunk = inputfile.read(chunksize)
        if not chunk: #check the chunk is empty
            break
        partnum += 1
        filename = os.path.join(todir, ('part%04d'%partnum))
        fileobj = open(filename, 'wb') # make partfile
        fileobj.write(chunk) # write data into partfile
        fileobj.close()

    return partnum

if __name__ == '__main__':
    fromfile = input('File to be split?')
    todir = input('Directory to store part files?')
    chunksize = int(input('Chuncksize to be split?'))
    absfrom, absto = map(os.path.abspath, [fromfile, todir])
    print ('Splitting', absfrom, 'to', absto, 'by', chunksize)
    try:
        parts = split(fromfile, todir, chunksize)
    except:
        print ('Error during split:')
        print (sys.exc_info()[0], sys.exc_info()[1])
    else:
        print ('split finished:', parts,'parts are in', absto)