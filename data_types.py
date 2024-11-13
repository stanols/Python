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
