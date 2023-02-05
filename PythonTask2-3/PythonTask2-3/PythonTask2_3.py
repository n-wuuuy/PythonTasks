def splitV2(slova,sim):
    spisok =[]
    while(slova.find(sim)!=-1):
        spisok.append(slova[:slova.find(sim)])
        slova=slova[slova.find(sim)+1:]
    spisok.append(slova)
    return spisok



slova="daf,d,afsaf"

y=splitV2(slova,",")
print(y)



