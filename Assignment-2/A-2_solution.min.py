students = [] #the 2-dimensional matrix used to store the records (each in the form of an 8-item list) for all students

def menu():
    print('\n')
    print(
"""Welcome to the Teacher’s Simple Class Calculator. Here’s the list of options:
    1- Enter student records (Name, ID, and 6 marks separated by commas)
    2- Display the class average
    3- Display the total grade, letter grade and relation to class average for a given student
    4- Display a simple bar chart to show grade distribution
    5- Exit"""
        )
        
    return int(input())

def is_unique(ID):
    for record in students:
        if ID == record[1]:
            return False
    return True

def record_exists(name, ID): #checks if a student record exists
    for record in students:
        if (name == record[0]) and (ID == record[1]):
            return True
    return False

def validate_record(record): #record is a string
    record = record.split(',')[:8] #slice and take only the first 8 items, in case the input record is too many items long, since there is no validation for records too long

    if len(record) < 8:
        print('Record incomplete.', end='')
        return False

    for i in range(1, 8): #cast the ID and all grades to integer
        record[i] = int(record[i])

    if not (is_unique(record[1])): #check if the inputed ID is unique
        print('Duplicate ID number.', end='')
        return False
        
    return record #if record is valid and the function has gone through all previous validation tests without returning False

def validate_query(query): #query is a string
    query = query.split(',')
    
    query[1] = int(query[1]) #cast the ID to int

    if not (record_exists(query[0], query[1])): #check if there are any records matching the query
        print('No student records matching that query.', end='')
        return False

    return query #if query is valid and the function has gone through all previous validation tests without returning False

def student_avg(ID):
    for record in students:
        if record[1] == ID: #once the record is found
            return int(sum(record[2:])) #slice the grades (after the name and ID at indices 0 and 1), sum them, and integer round to get an average out of 100 (20+20+15+15+15+15 = 100)  

def letter_grade(grade):
    if grade >= 87: return 'A'
    elif grade >= 75: return 'B'
    elif grade >= 65: return 'C'
    else: return 'F'

def class_avg():
    total=0
    for record in students:
        total += int(sum(record[2:])) #same as above. slice the current record list to get items from indices (inclusive) 2 to 7. then sum all elements of the list slice with sum(). round to int, and increment the total counter by this value

    return total//(len(students)) #floor division

def deviation(student_average, class_average):
    return abs(student_average - class_average), 'above' if student_average > class_average else 'below' #the first return value is the magnitude of the difference between averages, the second return value is the str decided by the ternary statement

##    if student_average > class_average: return (student_average - class_average), 'above'
##    else: return (class_average - student_average), 'below'
    
while True: #main loop
    option = menu()
    if option == 1:
        while True: #record inputing loop. continuously receive record inputs, validate them, store them in the students matrix if valid, and repeat until the user breaks out of this loop by inputing the keyword 'done'
            raw_record = input("Enter students record (separated by commas, no spaces) or done: ")
            
            if raw_record.lower().strip() == 'done': #first check if the user has inputed the keyword 'done' before validating the input string as a record. make lowecase, strip leading and trailing whitespace
                break #break from the nested record inputing loop, and go to the continue statement immediately after this nested while loop (can't break out of a nested loop to continue the enclosing loop in a single statement)
            
            record = validate_record(raw_record) #from the user inputed record string, the function will return an 8-item list consisting of all comma separated valuesin order, where all str values representing an int were cast to int
            
            if not record: #if the above validate_record() function returned False (when the raw_record fails any of the validation tests)
                print('Record rejected.')
                continue #continue to receive next record input (doesn't break out to main loop)
            
            students.append(record) #append this valid record to the 2-dimensional matrix of student records
            print('Record accepted') #continue to receive next record input
                   
        continue #restart the main loop, after the code execution has broken out of the nested record inputing while loop, once the user inputs the keyword 'done'

    if len(students) == 0:#if they have not chosen option 1 and there are not entered records, then the following options (2 and 3) cannot be processed
        print('No records were entered. Please choose option 1 first.')
        continue #restart the main loop

    if option == 2:
        print('Class Average = {}'.format(class_avg()))
        continue #restart the main loop
    
    if option == 3:
        raw_query = input('Enter the name and ID of the student: ')
        query = validate_query(raw_query) #from the user inputed query string, the function will return a 2-item list consisting of both comma separated values in order, where the name as a str is first and the ID cast to an int is second 
        
        if not query: #if the above validate_query() function returned False (when the raw_query fails any of the validation tests)
            print('Invalid query.')
            continue #restart the main loop

        student_name = query[0]
        student_ID = query[1]
        student_average = student_avg(student_ID)
        letter_grade = letter_grade(student_average)
        class_average = class_avg()
        deviation_pts, deviation_dir = deviation(student_average, class_average)
        
        print('Grade for {} ID = {}: {} {}, {} points {} average.'.format(student_name, student_ID, student_average, letter_grade, deviation_pts, deviation_dir), end='\n'*2)
        continue #restart the main loop
