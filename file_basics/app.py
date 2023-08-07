
# Read File in Python
def readFile():
    fhandle = open("data/employees.txt","r")
    content = fhandle.readlines()
    for line in content:
        print(line.strip())
    fhandle.close()

# Write File in Python using input with infinite loop

def writeFile():
    fhandle = open("data/employees.txt","a")
    name = None
    while True:
        name = input("Enter the employee name to add: ")
        if( name == "exit"): break
        fhandle.write(name+"\n")
    fhandle.close()

writeFile()