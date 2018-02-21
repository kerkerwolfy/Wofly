from datetime import datetime
import zipfile
import sys

def extractZip(zFile, strPassword):
    try:
        zFile.extractall(pwd=strPassword.encode('utf-8'))
        return strPassword
    except Exception as e:
        #print(sys.exc_info())
        return

def attackZip(strFileName):
    zFile = zipfile.ZipFile(strFileName)
    pwdFile = open("dictionary.txt")

    print('[+] Start guessing password...')
    for line in pwdFile.readlines():
        str_pwd = line.strip('\n')
        guess = extractZip(zFile, str_pwd)

        if guess:
            print('[+] Password = %s\n' % str_pwd)

    zFile.close()
    pwdFile.close()

if __name__ == '__main__':
    start = datetime.now()
    attackZip("wof.zip")
    end = datetime.now()
    print(end-start)