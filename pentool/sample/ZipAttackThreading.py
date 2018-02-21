import timeit
import zipfile
from threading import Thread
#import sys

def extractZip(zFile, strPassword):
    try:
        zFile.extractall(pwd=strPassword.encode('utf-8'))
        print('[+] Password found: %s' % strPassword)
    except:
        #print(sys.exc_info())
        pass

def attackZip(strFileName):
    zFile = zipfile.ZipFile(strFileName)
    pwdFile = open("dictionary.txt")

    print('[+] Start guessing password...')
    for line in pwdFile.readlines():
        str_pwd = line.strip('\n')
        t = Thread(target=extractZip, args=(zFile, str_pwd))
        t.start()


if __name__ == '__main__':
    start = timeit.default_timer()
    attackZip("wof.zip")
    end = timeit.default_timer()
    print(end-start)