# Implement a todo list manager program using files
import sys #Importing command line parameters
filename = (str(sys.argv[1]))#Name of the file
print(filename)

Flists=open(filename,"r") #Opening the file
#testo = Flists.read()
#print("FILE CONTENT:\n",testo)
print("")
print("Todo_Manager")
init = 0
i=0
list=[]
for line in Flists:#NEED TO FIND A KIND OF EOF CONDITION TO END THE CYCLE
    list.append(line)
Flists.close()#Closing the file
Flists=open(filename,"w") #reopening the file for writing
while init!=10:

    print("1. Insert a new task (a string of text);")
    print("2. Remove a task (by typing its content, exactly);")
    print("3. Show all the existing tasks, sorted in alphabetical order")
    print("4. Close the program")
    print("")
    print("Your choice:")
    choice=input()
    if int(choice) == 1:
        print("Enter the new task:")
        list.append(input()+"\n")
        print("Task inserted.")
    elif int(choice) == 2:
        print("Enter the name of the task you want to remove:")
        string_del=input()
        list.remove(string_del+"\n")
    elif int(choice) == 3:
        print("These are all the task, sorted in alphabetical order:")
        #print(sorted(list))
        for x in sorted(list):
            print(x,end='')
        print("End of the printing")
    else:
        print("closing the program and saving the task file")
        #save the list in the file
        for string in sorted(list):
            Flists.write(string)
        Flists.close()#Closing the file
        init=10
    print("")