#The goal of my project is to split students into groups
from random import choice

def group_generator():

    students = ['Ava', 'Cody', 'DeOnna', 'Dylan', 'Felix', 'Jacob', 'Kaylen', 'Logan', 'Maddie', 'Michaela', 'Nial', 'Rachel', 'Tyler', 'Zach']
    #this is the list of students to sort
    group1 = []
    group2 = []
    #these are the groups that they're sorted into
    
    while len(students) > 0:
        studentA = choice(students)
        #this will select a student
        group1.append(studentA)
        #this will move the student to a group (group 1)
        students.remove(studentA)
        #This will remove the student from the list
        
        if students == []:
            break
            #this will end the loop
            
        studentB = choice(students)
        #this will select a student
        group2.append(studentB)
        #this will move the student to a group
        students.remove(studentB)
        #this will remove the student from the list
        
    print('These are the groups:')
    print(group1)
    print(group2)
        
        
        
    
    