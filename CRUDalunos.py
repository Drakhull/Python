import os
from datetime import datetime, timedelta

current_date = datetime.now()

class dateOfBirth:
  def __init__(self, day = 0, month = 0, year = 0, birth_date = None):
    self.birth_date = birth_date
    self.day = day
    self.month = month
    self.year = year

  def age(self):
    age = current_date.year - self.year - ((current_date.month, current_date.day) < 
                                           (self.month, self.day))
    return age


class Student:
  def __init__(self, name = 'Missing info', register = 'Missing info', 
               cpf = 'Missing info', gender = 'Missing info', 
               day = 0, month = 0, year = 0, birth_date = None):
      self.name = name
      self.birth = dateOfBirth(day, month, year, birth_date)
      self.gender = gender
      self.register = register
      self.cpf = cpf

  def show(self):
    print(f'Name: {self.name}, Gender: {self.gender}, Registration: {self.register}'
          f', CPF: {self.cpf}, Age: {self.birth.age()}')

  def showSpecific(self, number):
    print(f'student here {number}')

# Declarations

aCad = 0

students = []

# Declarations

############# Functions #############

# Menus
def menu():
  print("0 - Exit")
  print("1 - Create Student")
  print("2 - Read Students")
  print("3 - Update Student")
  print("4 - Delete Student")

  return input("Your choice: ")


def menu_update():
  print("What do you want to update?")
  print("0 - Exit")
  print("1 - Name")
  print("2 - Birth")
  print("3 - Gender")
  print("4 - Register")
  print("5 - CPF")
  print("6 - All")
  option = input("Your choice: ")
  return option


# Menus

# Switch case to choose options
def switch_case(option):
  global aCad

  match option:
    case '0':  # Exit
      return True

    case '1':  # Create
      aCad += create_student(students)
      clearS()
      return False

    case '2':  # Read
      print_students(students)
      clearS()
      return False

    case '3':  # Update
      if (aCad == 0):
        print('There are no students in the system.')
        pressEnter()
        return False

      register = input('Type the register of the student you want to update, or EXIT '
                      'to return: ')
      if (register == 'EXIT'):
        return False

      clearS()
      update_student(students, register)
      clearS()
      return False

    case '4':  # Delete
      register = input('Type the register of the student you want to delete: ')
      clearS()
      remove_student(students, register)
      clearS()
      return False

    case _:  # Case other option
      print('Invalid option!')
      pressEnter()


# Creates and validate the student
def QUIT(variable):
  if (variable == 'EXIT'):
    return True
  return False

def create_student(students):
  global aCad
  EXIT = False
  print('-' * 10,'Create Student', '-' * 10)
  print('' * 6, 'Type EXIT in any place to return', '' * 6)

  # Valid = 0

  NAME = input('Name: ')
  EXIT = QUIT(NAME)
  if (EXIT):
    return 0
  # Validations here

  BIRTH = input('Date of Birth(DD/MM/YYYY): ')
  EXIT = QUIT(BIRTH)
  if (EXIT):
    return 0
  BIRTH = datetime.strptime(BIRTH, '%d/%m/%Y')
  # Validations here

  REGISTER = input('Register: ')
  EXIT = QUIT(REGISTER)
  if (EXIT):
    return 0
  # Validations here

  GENDER = input('Gender (M/F/N): ')
  EXIT = QUIT(GENDER)
  if (EXIT):
    return 0
  # Validations here

  CPF = input('CPF: ')
  EXIT = QUIT(CPF)
  if (EXIT):
    return 0
  # Validations here

  new_student = Student(NAME, REGISTER, CPF, GENDER, BIRTH.day, BIRTH.month, 
                        BIRTH.year, BIRTH)

  students.append(new_student)

  students[aCad].show()
  pressEnter()

  return 1


# Update the student information
def update_student(students, register):
  global aCad

  found = False
  i = 0
  while (i < aCad):
    if (students[i].register == register):
      change_data(students , i)
      found = True

    i += 1

  clearS()
  if (not found):
    print('This student doesnt exists.')
    pressEnter()
  else:
    print('Student updated!')
    pressEnter()


def change_data(students, i):
  students[i].show()
  option = menu_update()
  match option:
    case '0': # Exit
      return

    case '1': # Name
      clearS()
      NAME = input('Name: ')
      students[i].name = NAME
      return

    case '2': # Birth
      clearS()
      BIRTH = input('Date of Birth(DD/MM/YYYY): ')
      BIRTH = datetime.strptime(BIRTH, '%d/%m/%Y')
      students[i].birth = dateOfBirth(BIRTH.day, BIRTH.month, 
      BIRTH.year, BIRTH)
      return

    case '3': # Gender
      clearS()
      GENDER = input('Gender (M/F/N): ')
      students[i].gender = GENDER
      return

    case '4': # Register
      clearS()
      REGISTER = input('Register: ')
      students[i].register = REGISTER
      return

    case '5': # CPF
      clearS()
      CPF = input('CPF: ')
      students[i].cpf = CPF

      return

    case '6': # All
      clearS()
      NAME = input('Name: ')
      students[i].name = NAME

      BIRTH = input('Date of Birth(DD/MM/YYYY): ')
      BIRTH = datetime.strptime(BIRTH, '%d/%m/%Y')
      students[i].birth = dateOfBirth(BIRTH.day, BIRTH.month, 
      BIRTH.year, BIRTH)

      GENDER = input('Gender (M/F/N): ')
      students[i].gender = GENDER

      REGISTER = input('Register (M/F/N): ')
      students[i].register = REGISTER

      CPF = input('CPF: ')
      students[i].cpf = CPF
      return


# Show the students
def print_students(students):
  if(aCad == 0):
    print('There aren’t any students registered.')

  else:  
    i = 0
    while(i < aCad):
      print(f'Student {i+1}')
      students[i].show()
      print('\n')
      i += 1

  input('Press enter to continue...')


def remove_student(students, register):
  global aCad

  name_copy = ''
  found = False
  i = 0
  while (i < aCad):
    if (students[i].register == register):
      name_copy = students[i].name
      del students[i]
      found = True
      aCad -= 1

    i += 1

  clearS()
  if (not found):
    print('This student doesnt exists.')
    pressEnter()
  else:
    print(f'Student {name_copy} deleted!')
    pressEnter()

# Press enter key to wait for 
def pressEnter():
  input('Press enter to continue...')


# Clear the screen
def clearS():
  os.system("clear")

############# Functions #############

# Program start
quit = False
while not quit:
  clearS()
  option = menu()
  clearS()
  quit = switch_case(option)

