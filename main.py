import sys, signal
from re import search as search_for_regex


# Prompt a client
def prompt(file_writer):
    confirmed = False
    retry = False
    while not confirmed:
        name = prompt_name(retry)
        email = prompt_email()
        possible_back = ['back', 'b', 'Back', 'BACK', '"back"', '"Back"', '"BACK"']
        # Keyword to end the program
        if email == 'apple':
            end(file_writer)
        while email in possible_back:
            retry = True
            name = prompt_name(retry)
            email = prompt_email()
        confirmed = confirm(name, email)
        retry = not confirmed
    file_writer.write(name + ' ' + email + '\n')

# validate email
def email(em):
    match = search_for_regex(r'[\w.-]+@[\w.-]+.\w+', em)
    if match:
        return True
    else:
        return False

# Confirm the name and email
def confirm(name, email):
    print '\nYou have entered the name: ' + name + ' and the email: ' + email + '.'
    print 'If this is correct, press the return key.'
    confirm = raw_input('If this is incorrect, type any character and hit return: ')
    return True if confirm == '' else False

def prompt_email():
    return raw_input('Please enter your email (or type "back" to change your name): ')

def prompt_name(retry):
    if retry:
        return raw_input('Please re-enter your name: ')
    else:
        return raw_input('Please enter your name: ')

# Divide between clients
def divide():
    print '\n--------------------------------------------------------------\n'

# Begin the program
def begin():
    file_writer = open('info.txt', 'a')
    print 'Welcome to TACS!'
    while (True):
        prompt(file_writer)
        divide()

def end(file_writer):
    file_writer.close()
    sys.exit(0)

# Boiler Plate
if __name__=='__main__':
    # Handle potential ^C's
    def sigint_handler(signal, frame):
        sys.stdout.write('\nCaught ^C, please do not do that.\n')
    signal.signal(signal.SIGINT, sigint_handler)
    begin()




