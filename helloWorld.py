print("Hello World")
#Second line of Hello World program
#Extensiton of git to Spyder
#Putting a random python homework to the hello world program.
#Question1
#List Defenition. Using a hard coded list given in the question.
def main():
    a =  [1, 11, 2, 3, 5, 8, 13, 10, 21, 34, 55, -1] 
    #a
    lenA = len(a)
    for i in range(lenA):
        if a[i] < 10:
            print(a[i],end=' ')
    
    #b
    aPrint = [print(i,end=' ') for i in a if i<10]
    print(aPrint)
    
    #c
    aNew = [i for i in a if i<10]
    print(aNew)
    
    #d
    userLimit = int(input("Enter a number : "))
    aUser = [i for i in a if i>userLimit]
    print(aUser)

if "__name" == __main__:
    main()