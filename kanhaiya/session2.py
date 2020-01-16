print("Hello")

a = 10
b = 20
sum = a + b
print("sum is:",sum);

# whatever we write in our program is by default part of main
print(__name__) # main
def main():
    print("Hello")

    a = 10
    b = 20
    sum = a + b
    print("sum is:", sum);

    # whatever we write in our program is by default part of main
    print(__name__)  # main

# you have to execute main yourself now
if __name__ == "__main__":
    main()
    # Single Value Container

    # Container Creation Statement
    age = 20

    # Read/Print Statement
    # type -> class
    # id   -> HashCode
    print("Age:", age, type(age), id(age))
    print(age, type(age), hex(id(age)))
    print(age, type(age), oct(id(age)))
    print(age, type(age), bin(id(age)))

    # Container Creation Statement
    johnsAge = 20
    print("johnsAge:", age, type(johnsAge), id(johnsAge))

    # Container Update Statement
    age = 30
    print("Age:", age, type(age), id(age))

    # PS: Containers in memory are stored as Data Structure: HashTable with algorithm called Hashing

    fionnasAge = age  # Reference Copy Operation
    print("fionnasAge:", fionnasAge, type(fionnasAge), id(fionnasAge))

    # Delete operation
    del age
    # print("Age:", age, type(age), id(age)) # error
    print("fionnasAge:", fionnasAge, type(fionnasAge), id(fionnasAge))

    del fionnasAge

    # PS:  age, johnsAge and fionnasAge are known as REFERENCE VARIABLES
    # REFERENCE VARIABLES will hold HashCodes 