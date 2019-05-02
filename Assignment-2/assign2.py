students=[]

def menu():
    while True:
        print("Welcome to the Teacher’s Simple Class Calculator. Here’s the list of options:
")
        print("1- Enter student records (Name, ID, and 6 marks separated by commas)")
        print("2- Display the class average")   
        print("3- Display the total grade, letter grade and relation to class average for a given student")
        print("4- Display a simple bar chart to show grade distribution")
        print("5- Exit")
        
        raw_option=input()
        try:
            option=int(raw_option)
        except:
            print('Please enter an integer.')
            continue
        if option>=1 and option <=5:
            return option
        else:
            print('Please enter a number between 1 and 5.')

def validate_record(record):
    try:
        record = record.split(',')
    except:
        print('Please separate items in the record by commas, no spaces.', end=' ')
        return False

    if len(record) < 8:
        print('Record incomplete.', end=' ')
        return False
    if len(record) > 8:
        print('Record has too many items.')
        return False
            
    for i in range(1, 8): #try to cast the ID and all grades to integer
        try:
            record[i] = int(record[i])
        except:
            print(record[i] + ' must be an integer.', end=' ')
            return False
            
    if (record[1]<0) or (record[1]>999): #ID
        print('ID must be between 000 and 999.', end=' ')
        return False
    for i in range(2,4): #tests
        if (record[i]<0) or (record[i]>20):
            print('Test grades must be between 0 and 20.', end=' ')
            return False
    for i in range(4,8): #assignments
        if (record[i]<0) or (record[i]>15):
            print('Asignment grades must be between 0 and 15.', end=' ')
            return False
    if is_duplicate(record[1]):
        print('Duplicate ID number.', end=' ')
        
    return record #if record is valid and the function has gone through all previous validation tests without returning False

def record_exists(name, ID): #checks if a student record exists
    for record in students:
        if (name == record[0]) and (ID == record[1]):
            return True
    return False

def is_duplicate(ID):
    for record in students:
        if ID == record[1]:
            return True
    return False


def validate_query(query): #query is a string
    try:
        query = query.split(',')
    except:
        print('Please separate the name and ID by a comma, no spaces.', end=' ')
        return False
    
    if len(query) != 2:
        print('Please enter both the name and ID.', end=' ')
        return False
    
    try: #try to cast the query ID to an integer
        query[1] = int(query[1])
    except:
        print('The ID must be an integer.', end=' ')

    if (query[1]<0) or (query[1]>999):
        print('ID must be between 000 and 999.', end=' ')
        return False

    if not (record_exists(query[0], query[1])):
        print('No student records matching that query.', end=' ')
        return False

    return query #if query is valid and the function has gone through all previous validation tests without returning False

def student_avg(ID):
    for record in students:
        if record[1] == ID:
            student_grades = record[2:] #slice the grades (after thge name and ID at indices 0 and 1)
            student_average = int(sum(student_grades)) #out of 100 (20+20+15+15+15+15 = 100)
            return student_average
        
def class_avg():
    total=0
    for record in students:
        student_grades = record[2:]
        student_average = int(sum(student_grades))
        total+=student_average
    class_average=int(total/(len(students)))
    return class_average

def letter_grade(grade):
    if grade >= 87:
        return 'A'
    elif grade >= 75:
        return 'B'
    elif grade >= 65:
        return 'C'
    else:
        return 'F'

def deviation(student_average, class_average):
    if student_average > class_average:
        return student_average - class_average, 'above'
    else:
        return class_average - student_average, 'below'
    
while True: #main loop
    option = menu()
    if option == 1:
        while True: #keep on receiving records until user inputs 'done'
            raw_record = input("Enter students record(Separate by commas,no spaces)or done: ")
            
            if raw_record.lower().strip() == 'done':
                break #start the main loop again from menu
            
            record = validate_record(raw_record)
            
            if not record: #if the above validation function returned False
                print('Record rejected.')
                continue
            
            students.append(record)
            print('Record accepted')
        print('')
        continue #restart the main loop in any case

    if len(students) == 0:#if they have not chosen option 1 and there are not entered records, then the following options cannot be processed
        print('No records were entered.')
        continue

    if option == 2:
        print('Class Average = ' + str(class_avg()), end='\n'*2)
        continue
    
    if option == 3:
        raw_query = input('Enter the name and ID of the student: ')
        
        query = validate_query(raw_query)
        
        if not query:
            print('Invalid query.')
            continue

        student_name = query[0]
        student_ID = query[1]
        student_average = student_avg(student_ID)
        letter_grade = letter_grade(student_average)
        class_average = class_avg()
        deviation_pts, deviation_dir = deviation(student_average, class_average)
        
        print('Grade for {} ID = {}: {} {}, {} points {} average.'.format(student_name, student_ID, student_average, letter_grade, deviation_pts, deviation_dir), end='\n'*2)
        continue
