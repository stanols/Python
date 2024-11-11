import sys;
import math;
import hashlib;
import getpass;
import json;

def getHash(text):
    return hashlib.sha256(text.encode()).hexdigest();

login = input('Login:');

if login != 'nmatch':
    print('Unknown user');
    sys.exit();

hash = '926db1abcfac5c99087179b74cc9c91388032656f1299fef1e637d20a548eed1';

attempts = 0;

while True:
    password = getpass.getpass('Password:');
    passwordConfirmation = getpass.getpass('Confirm Password:');

    if attempts > 2:
        print('You tried too many times... Exiting');
        sys.exit();

    if password != passwordConfirmation:
        print('Password does not match');
        attempts += 1;
        continue;

    passwordHash = getHash(passwordConfirmation);

    if passwordHash != hash:
        print('Unauthorized. Password is incorrect. Try again');
        attempts += 1;
        continue;

    break;      

print('Successfully authorized! Welcome, ' + login + '!');

while True:
    print("x * x = ");
    value = input('Enter x:');

    if value == 'exit':
        sys.exit();
    
    x = int(value);

    result = math.pow(x, 2);

    print(result);
