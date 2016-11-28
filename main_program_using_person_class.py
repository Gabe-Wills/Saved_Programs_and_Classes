from person import Person
import sys 

people = []

def Main():
    ''' Create test users and add them to the people list '''

    answer = True
    while answer:
        
        create_new_person()
        answer = input('Would you like to add a new person to the list? \n')
        if answer == 'no':
            print_people()
            sys.exit()
            
        
    
def print_people():
    ''' Iterates through the people list and prints out details '''

    for person in people:
        print('{0} {1} is {2} years old'.format(person.firstname, person.surname, person.age))
        

def create_new_person():
    ''' Creates a new person to add to the list '''
    
    
    firstname = input('Please enter firstname \n')
    surname = input('Please enter surname \n')
    dob = input('Please enter date of birth in the format of MM DD YYYY \n')
    new_person = Person(firstname, surname, dob)
    people.append(new_person)
    
    
    
if __name__ == '__main__':
    ''' This is the main code for the Program '''
    Main()
    



    
              
