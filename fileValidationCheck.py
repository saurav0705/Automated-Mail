import re
import os 

#formatting function for output
def divider():
    print("#"*50)

#function for extracting path and filename from the user input
def extractPath(completePath):
    lengthPath = len(completePath)-1
    while lengthPath>=0:
        if completePath[lengthPath]=='\\':
            break
        lengthPath-=1
    #if it only contains filename not a path
    if lengthPath<0:
        return{
            'filePath':"",
            'fileName':completePath
        }
    #if it contains path
    else:
        return {
            'filePath':completePath[0:lengthPath],
            'fileName':completePath[lengthPath+1:]
            }


# validation of file for emails
def check(email):
    #matching a regex pattern for enail validation  
    if(re.search(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$",email)):  
        return True  
          
    else:  
        return False

#function integrating all the validation functions 
def fileValidation(**kwargs):
    divider()
    print("Validating File :: "+kwargs['file']) 

    #extracting path and filename from the file for future use   
    infoFile = extractPath(kwargs['file'])
    pathOfFile=infoFile['filePath']
    fileName=infoFile['fileName']
    
    flag= False
    #checking if the file given by the user exist or not
    try:  
        fileData = open(kwargs['file'],'r')
    except:
        print("file not Found")
        exit()
    #created file which will hold validated data
    if pathOfFile=="":
        modifiedFile ='modified.txt'
    else:
        modifiedFile = pathOfFile+'\\modified.txt'
    validFile = open(modifiedFile,'w')
    validDataList = []
    #cerating a list of data prenet in the weekned file 
    with fileData as variable:
        for line in variable:
            #checking for valid mails using check function
            if(check(line.replace("\n",""))):
                validDataList.append(line.replace("\n",""))
            else:
                flag=True
    #eliminating duplicate values from data
    validDataSet = set(validDataList)
    #writing the data to new file 
    for validData in validDataSet:
        validFile.write(validData+"\n")
    fileData.close()
    validFile.close()        
    #removing the old file
    os.remove(kwargs['file'])

    #renaming the modified file with the file given by user
    os.rename(modifiedFile,kwargs['file'])
    if (flag==True):
        print("file validated and edited succesfully")
    else:
        print("found no invalid data in file")
    divider()



