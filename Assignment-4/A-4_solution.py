FILENAME = 'students.txt'
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


class Student:
    def __init__(self, name, ID, T1, T2, A1, A2, A3, A4):
        self.name = name 
        self.ID = ID
        self.T1 = T1
        self.T2 = T2
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.A4 = A4
        self.total = self.get_total()
        self.lette = self.get_letter()

    def __repr__(self):
        text='{:8s} {:>8d} {:>6d} {:>6d} {:>6d} {:>6d} {:>6d} {:>6d} {:>6d} {:>6s}'
        return(text.format(self.name,self.id,self.t1,self.t2,self.a1,self.a2,self.a3,self.a4,self.tot,self.letter))

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


def validate_record(record):
    if ',' in record:
        record = record.split(',')
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
        with open(FILENAME, 'r') as f: #file context manager
            for line in f: #iterate through each line in file (until it automatically stops at EOF)
                if line.strip() == '':
                    print('EOF')
                    break
                
                line = line.strip() #remove leading and trailing whitespace
                raw_record = line.split(',') #split the line on the comma character to return a list of CSV items

                record = validate_record(raw_record) #ensure the record is valid and cast the appropriate items in the list to int

                if not record: #if the above validate_record() function returned False (when the raw_record fails any of the validation tests)
                    print('Record rejected.')
                    continue #continue to parse next record (doesn't break out to main loop)
                
                instance = Student(*record) #create a student instance by unpacking the record list into the 8 positional arguments of the constructor
                students_list.append(instance) #append the newly created instance to the students_list, the instance variable will then hold the next instance at the next iteration
        continue  #restart the main loop, once all records in the file have been parsed
    
    if len(students_list) == 0: #if they have not chosen option 1 and there are not entered records, then the following options cannot be processed
        print('No records were entered. Please choose option 1 first.')
        continue #restart the main loop
        
    if option == 2:
        print('todo')
        
