import zipfile, glob, os, sys, getopt
        
password = [""]
link = ""
folderName = "Extracted"

def setPassword(arrayOfPassword):
    global password 
    index = 1
    for pwd in arrayOfPassword:
        password.insert(index, pwd)
        index = index + 1

def setLink(link_):
    global link
    link = link_

def setFolderName(folder_Name):
    global folderName
    folderName = folder_Name

def getPassword():
    return password

def getFolderName():
    return folderName

def getLink():
    return link

def extract(fileName):
    print(fileName)
    os.chdir(link)
    estratto = False
    if(zipfile.is_zipfile(fileName)):
        zf = zipfile.ZipFile(fileName)
        if(checkIfZipIsProtected(fileName)):
            if(len(password) > 1):
                if(not checkIfFileIsAlreadyExtracted(fileName)):
                    for i in range(1, len(password)):
                        estratto = False
                        try:
                            zf.extractall("../" + folderName, pwd=password[i])
                            estratto = True
                            break
                        except:
                            if(not estratto and i == (len(password) -1 )):
                                print("Non e' stata fornita la password per " + fileName + "\n")
                            else:
                                pass
                        if(not estratto):
                            print("Non sono riuscto ad estrarre " + fileName + "\n")
                        else:
                            print(fileName + " estratto con successo" + "\n")
                else:
                    print(fileName + " gia presente. Non sara estratto" + "\n")
            else:
                print("Sono presenti dei .zip protetti. Inserire la password." + "\n")
                sys.exit()
        else:
            if(not checkIfFileIsAlreadyExtracted(fileName)):
                print("Provo a decomprimere " + fileName + "\n")
                try:
                    zf.extractall("../" + folderName, pwd=password[0])
                    print(fileName + " estratto con successo" + "\n")
                except:
                    print("Non sono riuscto ad estrarre " + fileName)
            else:
                print(fileName + " gia presente. Non sara estratto" + "\n")
    else:
        pass
    os.chdir("..")

def extractAll(pathToFolder):
    os.chdir(pathToFolder)
    estratto = False
    for zip in glob.glob('*.zip'):
        if(zipfile.is_zipfile(zip)):
            zf = zipfile.ZipFile(zip)
            if(checkIfZipIsProtected(zip)):
                if(len(password) > 1):
                    if(not checkIfFileIsAlreadyExtracted(zip)):
                        print("Provo a decomprimere " + zip)
                        for i in range(1, len(password)):
                            estratto = False
                            try:
                                zf.extractall("../" + folderName, pwd=password[i])
                                estratto = True
                                break
                            except:
                                if(not estratto and i == (len(password) -1 )):
                                    print("Non e' stata fornita la password per " + zip + "\n")
                                else:
                                    pass
                        if(not estratto):
                            print("Non sono riuscto ad estrarre " + zip + "\n")
                        else:
                            print(zip + " estratto con successo" + "\n")
                    else:
                        print(zip + " gia presente. Non sara estratto" + "\n")
                else:
                    print("Sono presenti dei .zip protetti. Inserire la password." + "\n")
                    sys.exit()
            else:
                if(not checkIfFileIsAlreadyExtracted(zip)):
                    print("Provo a decomprimere " + zip + "\n")
                    try:
                        zf.extractall("../" + folderName, pwd=password[0])
                        print(zip + " estratto con successo" + "\n")
                    except:
                        print("Non sono riuscto ad estrarre " + zip)
                else:
                    print(zip + " gia presente. Non sara estratto" + "\n")
        else:
            pass
    os.chdir("..")

def checkIfZipIsProtected(zip):
    zf = zipfile.ZipFile(zip)
    for zip_info in zf.infolist():
        isEncrypted = zip_info.flag_bits & 0x1
    if(isEncrypted):
        return True
    else:
        return False

def checkIfFileIsAlreadyExtracted(zip):
    previousPath = os.getcwd()
    zf = zipfile.ZipFile(zip)
    os.chdir("..")
    os.chdir(os.getcwd() + "/" + folderName + "/")
    trovato = False
    for zipFile in zf.namelist():
        trovato = False
        for file in glob.glob('*'):
            if(zipFile == file):
                trovato = True
                break
            else:
                pass
        if(not trovato):
            break
        else:
            pass
    os.chdir(previousPath)
    return trovato

def createFolder(folderName):
    os.chdir(os.getcwd())
    if not os.path.exists(folderName):
        os.makedirs(folderName)

def main(argv):
    global password
    global link
    global folderName
    pwdInserted = ""
    if(len(argv) == 1 and argv[0] == "--help"):
        helpFile = open("helpUF.txt")
        for line in helpFile:
            print line
        sys.exit(2)
    try:
        opts, argv = getopt.getopt(argv, "", ("path=", "password=", "folder="))
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)
    for opt, arg in opts:
        if(opt == "--path"):
            link = arg
        elif(opt == "--password"):
            pwdInserted = arg.split(",")
        elif(opt == "--folder"):
            folderName = arg
    index = 1
    for i in range(0, len(pwdInserted)):
        password.insert(index, pwdInserted[i])
        index = index + 1
    createFolder(folderName)
    extractAll(link)

if __name__ == '__main__':
    main(sys.argv[1:])