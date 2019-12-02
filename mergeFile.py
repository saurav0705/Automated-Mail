def mergeFiles(**kwargs):
    masterFile = open(kwargs['master'],'a')
    for values in kwargs['differ']:
        masterFile.write(values+"\n")
    masterFile.close()
    print("Successfully updated master file")