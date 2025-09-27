#6
def student(batch_Name,student_Name,*student_Hobbies,**student_Marks):
    print(batch_Name)
    print(student_Name)
    print(student_Hobbies)
    print(student_Marks,'\n')
    pass
student('Aliens','Suresh','Cycling','Swimming','Reading',java=80,os=85,dbms=78)

#7
def college(proff_Name,professor_Dept='ECE',**subject_knowledge):
    print(proff_Name)
    print(professor_Dept)
    print(subject_knowledge)
    return
college('govind',professor_Dept='CSE',data_structures='70%',mathematics='80%' )
print('\n')
college('hari', data_structures ='30%', mathematics ='80%')
print('\n')
college('Anand',professor_Dept='ISE',data_communications='90%',computer_networks='80%' )