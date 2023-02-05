import csv

def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        sp=[row for row in reader]
        sp=(sorted(sp, key=lambda x: float(x['average mark']),reverse=True))
        return [sp[a]['student name'] for a in range(number_of_top_students)]

def get_old_performers(file_path):
    with open(file_path,'r') as rcsvfile:
        with open('StudentSort.csv','w',newline='') as wcsvfile:
            reader = csv.DictReader(rcsvfile)
            sp=[row for row in reader]
            sp=(sorted(sp, key=lambda x: float(x['age'],),reverse=True))
            fieldnames = ['student name', 'age','average mark']
            writer = csv.DictWriter(wcsvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(sp)
            return 


print(get_top_performers("students.csv"))
get_old_performers("students.csv")

