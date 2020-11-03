

def create_outline():
    """
    TODO: implement your code here
    """
    Course_Topics = set(
        [
            'Introduction to Python',
            'Tools of the Trade',
            'How to make decisions',
            'How to repeat code',
            'How to structure data',
            'Functions',
            'Modules'
        ]
    )

    Topics = []
    


    Problems = {}
    problems_list = ['Problem 1','Problem 2','Problem 3']
    student_records = [
        ('Nyari','Introduction to Python','Problem 2','[STARTED]'),
        ('Adan','How to make decisions','Problem 1','[GRADED]'),
        ('Tom','Modules','Problem 2','[COMPLETED]'),
        ('Sihle','Tools of the Trade','Problem 3','[STARTED]',),
        ('David','functions','Problam 1','[GRADED]'),
        ('Joy','How to pepeat code','Problem 2','[GRADED]'),
        ('Timmy','How to structure data','Problem 1','[GRADED]')
    ]
    
    
    print('Course Topics:')
    for items in Course_Topics:
        Topics.append(items)
    Topics.sort()

    for topics in Topics:
        print('*', topics)

    print('Problems:')
    for topic in Course_Topics:
        Problems[topic] = problems_list

    for key,value in Problems.items():
        print('* '+str(key)+' :', str(value[0])+', '+str(value[1])+', '+str(value[2]))
    
    print('Student Progress:')
    i = 1
    student_records = [(index[3],index[1],index[2],index[0]) for index in student_records]
    student_records.sort(reverse = True)
    student_records = [(index[3],index[2],index[1],index[0]) for index in student_records]
    for indexer in range(len(student_records)):
      k = 0
      print(str(indexer + 1) + '.',end='')
      while(k < len(student_records[i])):
        if k < 3:
          print(student_records[indexer][k], end = '-')
        else:
          print(student_records[indexer][k])
        k += 1

    

    pass


if __name__ == "__main__":
    create_outline()
