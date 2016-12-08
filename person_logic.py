from person import Person
import sys
import pickle



try:
    ''' Outputs a string if the error of not having a file to load when the programe starts '''
    
    with open('people_save', 'rb') as f:
        people = pickle.load(f)
except FileNotFoundError as e:
    people = []
    print('File not found error: ' + str(e) + '\nA new file will be created at closure.')          


def pickle_save():
    ''' Function which saves the data into a file '''
    
    with open('people_save', 'wb') as f:
        pickle.dump(people, f, protocol=pickle.HIGHEST_PROTOCOL)

def print_people():
    ''' Iterates through the people list and prints out details '''

    for person in people:
        print('{0} {1} is {2} years old, is a {3} and has {4} eyes. \n Also their postcode is {5} \n Their email address is {6} \n Their phone number is {7} '.format(person.firstname, person.surname, person.age, person.gender, person.eyecolor, person.address, person.email, person.number))



def create_new_person():
    ''' Creates a new person to add to the list '''
    
    
    firstname = input('Please enter firstname \n')
    surname = input('Please enter surname \n')
    dob = input('Please enter date of birth in the format of MMM DD YYYY \n')
    gender = input('Are you Male or Female? \n')
    eyecolor = input('What color are your eyes? \n')
    address = input('What is your postcode? \n')
    email = input('What is your email address? \n')
    number = input('What is your phone number?')
    
    new_person = Person(firstname, surname, dob, gender, eyecolor, address, email, number)
    people.append(new_person)



def loop():
    ''' The loop that creates new people over and over until user tells it to stop '''
    while True:
        
        create_new_person()
        answer = input('Would you like to add a new person to the list? \n')
        if answer == 'no':
            print_people()
            sys.exit()

def menu():
    ''' The logic controling the menu '''

    choices = input('What would you like to do?')
   
    
    if choices == '1':
        create_new_person()

    elif choices == '2':
        print_people()

    else:
        pickle_save()
        sys.exit() 




