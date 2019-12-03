import re
import os 

#formatting function for output
def divider():
    for var in range(0,50):
        print("-",end="")
    print()


#function for extracting path and filename from the user input
def extractPath(completePath):
    lengthPath = len(completePath)-1
    while lengthPath>=0:
        if completePath[lengthPath]=='\\':
            break
        lengthPath-=1
    return {
        'filePath':completePath[0:lengthPath],
        'fileName':completePath[lengthPath+1:]
        }


# validation of file for emails
def check(email):  
    if(re.search(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$",email)):  
        return True  
          
    else:  
        return False

#function integrating all the validation functions 
def fileValidation(**kwargs):
    print("Validating File :: "+kwargs['file'])
    divider()
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
    modifiedFile = pathOfFile+'\\modified.txt'
    validFile = open(modifiedFile,'w')<<<<<<< HEAD
import re
import os 


    validDataList = []
    with fileData as variable:
        for line in variable:
            if(crmatting funct for ouput
t",""))):
                validDataList.append(line)
            else:
       rt os 

#formatting function for output
def divider():
  matting function foutput
def divrrmatting function for output
def divrmatt
def ing funion for outpuing function for output
def  function or outdef dividp         flag=True
    validDataSet = set(validDataList)
    for validData in validDataSet:
        validFile.write(validData)
    fileData.close()
    validFile.close()        
    #removing the old file
    os.remove(kwargs['file'])

    #renaming the modified file with the file given by user
    os.rename(modifiedFile,kwargs['file'])
    if (flag==True):
        print("file validated and edited succesfully")
    else:
