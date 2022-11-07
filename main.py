import zipfile
import os

localFile = 'uploads/dasds.zip'

namepath = ""
for aux in range( len (localFile)):

    if localFile[aux] == ".":
        break 
    if aux > 7 :
        namepath += str(localFile[aux] )
    
BASE_DIR =  os.getcwd()

os.mkdir(   BASE_DIR + '/arquivos/'+namepath+'/'  )

with zipfile.ZipFile( localFile , 'r') as myzip:
    myzip.extractall('arquivos/')
    print ('got:', [info.filename for info in myzip.infolist()] ) 


os.remove(localFile)


    