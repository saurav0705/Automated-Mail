def compareFiles(**kwargs):
    masterData = open(kwargs['master'],'r')
    masterDataList = []
    with masterData as variable:
        for lines in variable:
            masterDataList.append(lines.replace("\n",""))
    masterData.close()
    differ=[]
    weekendData = open(kwargs['weekend'],'r')
    with weekendData as variable:
        for lines in variable:
            if lines.replace("\n","") not in masterDataList:
                differ.append(lines.replace("\n",""))
    weekendData.close()
    return differ


