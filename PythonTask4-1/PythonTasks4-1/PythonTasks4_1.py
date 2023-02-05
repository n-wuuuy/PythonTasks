with open('unsorted_names.txt','r') as rf:
    with open('sorted_names.txt','w') as wf:
        lines = rf.readlines()
        lines.sort()
        for line in lines:
            wf.write(line)


