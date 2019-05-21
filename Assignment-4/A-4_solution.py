import sys

FILENAME = 'students.txt'
DELIM = ','
LETTERS = ('A', 'B', 'C', 'D')

students_list = []

def menu():
    while True:
        print('\n')
        print(
"""Welcome to the Teacher’s Simple Class Calculator. Here’s the list of options:
    1- Read and process all students’ records
    2- Display All student records including total and letter grades and class average
    3- Display the complete record of a particular student
    4- Update a student’s grade
    5- Display a list of all students who achieved a particular letter grade
    6- Exit"""
            )
        
        try:
            option = int(input())
            if (option >= 1) and (option <= 6): return option
            else: print('Please enter a number between 1 and 5.')
        except:
            print('Please enter an integer.')
            continue

def display_table(part):
    '''Formatting the table that displays the records. Accounts for longer and shorter names by using padding to extend or shorten the table rows. Is called in option2,3 and 4().'''
    padding = Student.max_name_len - len('Names')
    if part == 'header': #the function is called with an argument that determines what to display
        print('+{}------------|-----------------------------|----------------+'.format('-'*padding))
        print('| {:^{}} |            GRADE            |     REPORT     |'.format('INFO', len(' - ID ') + Student.max_name_len))
        print('>{}------------|-----------------------------|---------------<'.format('-'*padding))
        print('| {}Name - ID  | T1 | T2 | A1 | A2 | A3 | A4 | Total | Letter |'.format(' '*padding))
        print('>{}------------|----|----|----|----|----|----|-------|--------<'.format('-'*padding))
    elif part == 'footer':
        print('+{}------------|-----------------------------|----------------+'.format('-'*padding))
    elif part == 'letter':
        print('+--------------|-----------------------+')
        print('| Letter Grade |  {}  |  {}  |  {}  |  {}  |'.format(*LETTERS)) #unpack the global constant tuple into each placeholder
        print('>--------------|-----------------------<')


class Student:
    student_count, max_name_len = 0, 0 #class variables
    
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
        self.total = self.get_total()
        self.letter = self.get_letter()

        Student.student_count += 1 #increment the amount of student instances everytime __init__ is called (upon each instance creation)

    def __repr__(self):
        return "{} - {}: {} {}".format(self.name, self.ID, self.total, self.letter)

    def __str__(self):
        return "| {:>{}} - {:<3} | {:2} | {:2} | {:2} | {:2} | {:2} | {:2} |  {:>3}  |   {:>2}   |".format(self.name, Student.max_name_len, self.ID, self.T1, self.T2, self.A1, self.A2, self.A3, self.A4, self.total, self.letter)

    def __del__(self):
        student_count -= 1
    
    def get_total(self):
        return (self.T1 + self.T2 + self.A1 + self.A2 + self.A3 + self.A4)

    def get_letter(self):
        if self.total >= 87: return 'A'
        elif self.total >= 75: return 'B'
        elif self.total >= 65: return 'C'
        else: return 'F'

    def update_grade(self, grade_name, grade_value):
        if grade_name == 'T1': self.T1 = grade_value
        elif grade_name == 'T2': self.T2 = grade_value
        elif grade_name == 'A1': self.A1 = grade_value
        elif grade_name == 'A2': self.A2 = grade_value
        elif grade_name == 'A3': self.A3 = grade_value
        elif grade_name == 'A4': self.A4 = grade_value

def is_unique(ID):
    for instance in students_list:
        if instance.ID == ID:
            return False
    return True

def validate_record(record):
    if ',' in record:
        record = record.split(DELIM) #split the record on the comma character to return a list of CSV items
    else:
        print('Please separate items in the record by commas, no spaces.', end='')
        return False

    if len(record) < 8:
        print('Record incomplete.', end='')
        return False
    if len(record) > 8:
        print('Record has too many items.', end='')
        return False
            
    for i in range(1, 8): #try to cast the ID and all grades to integer
        try:
            record[i] = int(record[i])
        except:
            print(record[i] + ' must be an integer.', end='')
            return False
            
    if (record[1] < 0) or (record[1] > 999): #ID
        print('ID must be between 000 and 999.', end='')
        return False
    for i in range(2,4): #tests
        if (record[i] < 0) or (record[i] > 20):
            print('Test grades must be between 0 and 20.', end='')
            return False
    for i in range(4,8): #assignments
        if (record[i] < 0) or (record[i] > 15):
            print('Asignment grades must be between 0 and 15.', end='')
            return False

    if not (is_unique(record[1])): #check if the inputed ID is unique
        print('Duplicate ID number.', end='')
        return False
        
    return record #if record is valid and the function has gone through all previous validation tests without returning False


def validate_grade(grade_name, grade_value):
    try:
        grade_value = int(grade_value)
    except:
        print('New grade must be an integer.', end='')
        return False
    
    if grade_name in ['T'+str(i) for i in range(1,3)]:
        if (grade_value < 0) or (grade_value > 20):
            print('Test grades must be between 0 and 20.', end='')
            return False
    elif grade_name in ['A'+str(i) for i in range(1,5)]:
        if (grade_value < 0) or (grade_value > 20):
            print('Asignment grades must be between 0 and 15.', end='')
            return False
    else:
        print('Grade names must be either T1 or T2 fór tests, or A1, A2, A3, A4 for assignments.', end='')
        return False

    return grade_name, grade_value


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
            print("No file '{}' found in the same directory as this script.".format(FILENAME)) #error msg then restar main loop
            
        continue  #restart the main loop, once all records in the file have been parsed
    
    if len(students_list) == 0: #if they have not chosen option 1 and there are not entered records, then the following options cannot be processed
        print('No records were entered. Please choose option 1 first.')
        continue #restart the main loop
        
    if option == 2:
        display_table('header')
        for instance in students_list:
            print(str(instance))
        display_table('footer')
        
