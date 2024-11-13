import sys;
import math;
import hashlib;
import getpass;
import json;
import random;

#returns hash value for input string
def getHash(text):
    return hashlib.sha256(text.encode()).hexdigest();

def printDataTypes():
    #str
    name = 'Natalia';
    #int
    age = 18;
    #float
    height = 160;
    #complex
    iq = 100j
    #list
    pets = ['dog', 'cat'];
    #tuple
    fruits = ('banana', 'apple');
    #range
    score = range(10);
    #dict
    attributes = { 'boobs': 90, 'back': 90 };
    #set
    vegetables = { 'cucumber', 'tomato' };
    #frozenset
    frozenVegetables = ({ 'cherry' });
    #bool
    isWoman = True;
    #bytes
    array = b'hello';
    #bytearray
    byteArray = bytearray(5);
    #memoryview
    memory = memoryview(bytes(5));
    #None
    n = None;

    print(name);
    print(str(age));
    print(str(height));
    print(str(iq))
    print(str(pets));
    print(str(fruits));
    print(str(score));
    print(str(attributes));
    print(str(vegetables));
    print(str(frozenVegetables));
    print(str(isWoman));
    print(str(array));
    print(str(byteArray));
    print(str(memory));
    print(str(n));

printDataTypes();
print(random.randrange(1, 10));

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
