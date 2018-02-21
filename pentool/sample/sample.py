import zipfile

def extractZip(zFile, strPassword):
    try:
        zFile.extractAll(pwd=strPassword)
        return strPassword
    except:
        return

def attackZip(strFileName):
    zFile = zipfile.ZipFile(strFileName)
    pwdFile = open("dictionary.txt")

    for line in pwdFile.readlines():
        str_pwd = line.strip('\n')
        guess = extractZip(zFile, str_pwd)

        if guess:
            print('[+] Password = %s\n' % str_pwd)
            exit(0)
        else:
            print('[+] %s is not incorrect \n' % str_pwd)


if __name__ == '__main__':
    attackZip("wof.zip")