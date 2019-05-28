import sys #used only for sys.exit() in option 6

FILENAME = 'students.txt' #name of the file from where the student records will be read
DELIM = ',' #delimiter that the program should expect, both in the (CSV) file and user inputs
PRECISION = 2 #digits after the decimal point for the round() function
LETTERS = ('A', 'B', 'C', 'D') #possible letter grades
TEST_MAX_GRADE = 20
ASSIGN_MAX_GRADE = 15

students_list = []

def menu():
    while True:
        print(
"""\nWelcome to the Teacher’s Simple Class Calculator. Here’s the list of options:
    1- Read and process all students’ records
    2- Display All student records including total and letter grades and class average
    3- Display the complete record of a particular student
    4- Update a student’s grade
    5- Display the letter grade distribution and a list of students who achieved a particular letter grade
    6- Exit"""
            )
        
        try:
            option = int(input().strip())
            if (option >= 1) and (option <= 6): return option
            else: print('Please enter a number between 1 and 6.')
        except:
            print('Please enter an integer.')
            continue

def display_table(part):
    '''Formatting the table that displays the records. Accounts for longer and shorter names by using padding to extend or shorten the table rows. Is called in option2,3 and 4().'''
    padding = Student.max_name_len - len('Names')
    if part == 'record': #the function is called with an argument that determines what to display
        print('\n+{}------------|-----------------------------|----------------+'.format('-'*padding))
        print('| {:^{}} |            GRADE            |     REPORT     |'.format('INFO', len(' - ID ') + max(len('Name'), Student.max_name_len) ))
        print('>{}------------|-----------------------------|---------------<'.format('-'*padding))
        print('| {}Name - ID  | T1 | T2 | A1 | A2 | A3 | A4 | Total | Letter |'.format(' '*padding))
        print('>{}------------|----|----|----|----|----|----|-------|--------<'.format('-'*padding))
    elif part == 'record footer':
        print('+{}------------|-----------------------------|----------------+\n'.format('-'*padding))
    elif part == 'letter':
        print('\n+--------------|-----------------------+')
        print('| Letter Grade |  {}  |  {}  |  {}  |  {}  |'.format(*LETTERS)) #unpack the global constant tuple into each placeholder
        print('>--------------|-----------------------<')
    elif part == 'letter footer':
        print('+--------------|-----------------------+\n')

class Student:
    count, max_name_len = 0, 0 #class variables
    
    def __init__(self, name, ID, T1, T2, A1, A2, A3, A4):
        self.name = name
        if len(self.name) > Student.max_name_len: #updates the max_name_len class variable each time a name is read that is longer than the previous max
            Student.max_name_len = len(self.name)
        self.ID = ID
        
        self.T1 = T1
        self.T2 = T2
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.A4 = A4
        
        self.set_total()
        self.set_letter()

        Student.count += 1 #increment the amount of student instances everytime __init__ is called (upon each instance creation)

    def __repr__(self): return "{} - {}: {} {}".format(self.name, self.ID, self.total, self.letter)

    def __str__(self): return "| {:>{}} - {:<3} | {:2} | {:2} | {:2} | {:2} | {:2} | {:2} |  {:>3}  |   {:>2}   |".format(self.name, Student.max_name_len, self.ID, self.T1, self.T2, self.A1, self.A2, self.A3, self.A4, self.total, self.letter)

    def __del__(self): Student.count -= 1 #not necessary, no UI to delete instance
    
    def get_total(self):
        total = self.T1 + self.T2 + self.A1 + self.A2 + self.A3 + self.A4
        max_grade = TEST_MAX_GRADE*2 + ASSIGN_MAX_GRADE*4
        if max_grade != 100:
            total = round((total / max_grade)*100, PRECISION) #make the grade out of 100
        return total

    def set_total(self): self.total = self.get_total()

    def get_letter(self):
        if self.total >= 87: return 'A'
        elif self.total >= 75: return 'B'
        elif self.total >= 65: return 'C'
        else: return 'F'

    def set_letter(self): self.letter = self.get_letter()

    def update_grade(self, grade_name, grade_value):
        setattr(self, grade_name, grade_value)
        
        self.set_total()
        self.set_letter()

        

def is_unique(ID):
    for instance in students_list:
        if instance.ID == ID:
            return False
    return True

def instance_exists(query):
    for instance in students_list:
        if (instance.name == query[0]) and (instance.ID == query[1]):
            return True
    return False

def validate_record(record):
    if DELIM in record:
        record = record.split(DELIM) #split the record on the DELIM character to return a list of CSV items
    else:
        print('Please separate items in the record by commas, no spaces.', end=' ')
        return False

    if len(record) != 8:
        print('Record {}.'.format('incomplete' if len(record) < 8 else 'has too many items'), end=' ')
        return False
            
    for i in range(1, 8): #try to cast the ID and all grades to integer
        try:
            record[i] = int(record[i])
        except:
            print(record[i] + ' must be an integer.', end=' ')
            return False
            
    if (record[1] < 0) or (record[1] > 999): #ID
        print('ID must be between 000 and 999.', end=' ')
        return False
    for i in range(2,4): #tests
        if (record[i] < 0) or (record[i] > TEST_MAX_GRADE):
            print('Test grades must be between 0 and {}.'.format(TEST_MAX_GRADE), end=' ')
            return False
    for i in range(4,8): #assignments
        if (record[i] < 0) or (record[i] > ASSIGN_MAX_GRADE):
            print('Asignment grades must be between 0 and {}.'.format(ASSIGN_MAX_GRADE), end=' ')
            return False

    if not (is_unique(record[1])): #check if the inputed ID is unique
        print('Duplicate ID number.', end=' ')
        return False
        
    return record #if record is valid and the function has gone through all previous validation tests without returning False


def validate_query(query): #query is a string
    if DELIM in query:
        query = query.split(DELIM)
    else:
        print('Please separate the name and ID by a comma, no spaces.', end=' ')
        return False
    
    if len(query) != 2:
        print('Please enter {} the name and ID.'.format('both' if len(query) < 2 else 'only'), end=' ')
        return False
    
    try: #try to cast the query ID to int
        query[1] = int(query[1])
    except:
        print('The ID must be an integer.', end=' ')
        return False

    if (query[1] < 0) or (query[1] > 999):
        print('ID must be between 000 and 999.', end=' ')
        return False

    if not (instance_exists(query)): #check if there are any instances matching the query
        print('No student records matching that query.', end=' ')
        return False

    return query #if query is valid and the function has gone through all previous validation tests without returning False


def validate_grade(grade):
    if DELIM in grade:
        grade = grade.split(DELIM)
    else:
        print('Please separate the grade name and grade value by a comma, no spaces.', end=' ')
        return False
    
    if len(grade) != 2:
        print('Please enter {} the grade name and grade value.'.format('both' if len(query) < 2 else 'only'), end=' ')
        return False
    
    try:
        grade[1] = int(grade[1])
    except:
        print('New grade must be an integer.', end=' ')
        return False

    try:
        grade[0] = grade[0][0].upper() + grade[0][1]
    except:
        return False
    
    if grade[0] in ['T'+str(i) for i in range(1,3)]: #T1 T2
        if (grade[1] < 0) or (grade[1] > TEST_MAX_GRADE):
            print('Test grades must be between 0 and {}.'.format(TEST_MAX_GRADE), end=' ')
            return False
    elif grade[0] in ['A'+str(i) for i in range(1,5)]: #A1 A2 A3 A4
        if (grade[1] < 0) or (grade[1] > ASSIGN_MAX_GRADE):
            print('Assignment grades must be between 0 and {}.'.format(ASSIGN_MAX_GRADE), end=' ')
            return False
    else:
        print('Grade names must be either T1 or T2 for tests, or A1, A2, A3, A4 for assignments.', end=' ')
        return False

    return grade

def validate_letter(letter):
    try:
        letter = letter.strip()
        letter = letter.upper()
    except:
        return False

    if letter not in LETTERS:
        print('Letter must be either {} or {}'.format(', '.join(LETTERS[:-1]), LETTERS[-1]))
        return False

    return letter

def class_average():
    class_total = 0
    for instance in students_list:
        class_total += instance.total

    return round(class_total/Student.count, PRECISION)

def find_student(query): #the query necessarily corresponds to a specific instance, since the validate_query() function ensures the query matches an instance
    for instance in students_list: 
        if (instance.name == query[0]) and (instance.ID == query[1]):
            return instance
        

while True:
    option = menu()

    if option == 1:
        try:
            with open(FILENAME, 'r') as f: #file context manager
                for line in f: #iterate through each line in file (until it automatically stops at EOF)                
                    line = line.strip() #remove leading and trailing whitespace

                    record = validate_record(line) #ensure the record is valid and cast the appropriate items in the list to int

                    if not record: #if the above validate_record() function returned False (when the raw_record fails any of the validation tests)
                        print('Record rejected.')
                        continue #continue to parse next record (doesn't break out to main loop)
                    
                    instance = Student(*record) #create a student instance by unpacking the record list into the 8 positional arguments of the constructor
                    students_list.append(instance) #append the newly created instance to the students_list, the instance variable will then hold the next instance at the next iteration
        except FileNotFoundError:
            print("No file '{}' found in the same directory as this script.".format(FILENAME)) #error msg then restart main loop
            
        continue  #restart the main loop, once all records in the file have been parsed
    
    if len(students_list) == 0: #if they have not chosen option 1 and there are no entered records, then the following options cannot be processed
        print('No records were entered. Please choose option 1 first.')
        continue #restart the main loop
        
    if option == 2:
        display_table('record')
        for instance in students_list:
            print(str(instance))
        display_table('record footer')

        print('Class Average: {}'.format(class_average()))

        continue #restart the main loop 

    if option == 3:
        raw_query = input('Enter the name and ID of the student (separated by a comma, no spaces): ')
        query = validate_query(raw_query) #from the user inputed query string, the function will return a 2-item list consisting of both comma separated values in order, where the name as a str is first and the ID cast to an int is second 
        
        if not query: #if the above validate_query() function returned False (when the raw_query fails any of the validation tests)
            print('Invalid query.')
            continue #restart the main loop

        instance = find_student(query)

        display_table('record')
        print(str(instance))
        display_table('record footer')

    if option == 4:
        raw_query = input('Enter the name and ID of the student (separated by a comma, no spaces): ')
        query = validate_query(raw_query) #from the user inputed query string, the function will return a 2-item list consisting of both comma separated values in order, where the name as a str is first and the ID cast to an int is second 
        
        if not query: #if the above validate_query() function returned False (when the raw_query fails any of the validation tests)
            print('Invalid query.')
            continue #restart the main loop

        instance = find_student(query)

        raw_grade = input('Enter the name of the new grade and its value (separated by a comma, no spaces): ')
        grade = validate_grade(raw_grade)

        if not query: #if the above validate_grade() function returned False (when the raw_grade fails any of the validation tests)
            print('Invalid grade.')
            continue #restart the main loop

        instance.update_grade(*grade)

        continue #restart main loop

    if option == 5:
        letter_occurrence = dict.fromkeys(LETTERS, 0)
        for instance in students_list:
            letter_occurrence[instance.letter] += 1

        display_table('letter')
        print('| #of students |{:^5}|{:^5}|{:^5}|{:^5}|'.format(*[letter_occurrence[key] for key in LETTERS]))
        display_table('letter footer')
        
        raw_letter = input('Enter the letter grade: ')
        letter = validate_letter(raw_letter)

        display_table('record')
        for instance in students_list:
            if instance.letter == letter:
                print(str(instance)) #__str__
        display_table('record footer')
        
        continue #restart main loop

    if option == 6:
        sys.exit()
        
        
