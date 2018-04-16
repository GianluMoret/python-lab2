
task1 = {'todo': 'call John for AmI project organization' , 'urgent': True}
task2 = {'todo': 'buy a new mouse', 'urgent': True}
task3 = {'todo': 'find a present for Angelina’s birthday', 'urgent': False}
task4 = {'todo': 'organize mega party (last week of April)', 'urgent': False}
task5 = {'todo': 'book summer holidays', 'urgent': False}
task6 = {'todo': 'whatsapp Mary for a coffee', 'urgent': False}
#dictlist = [dict() for x in range(n)] to create a list of dictionaries???

#creating the 2D dictionary
task=[task1,task2,task3,task4,task5,task6]

task_urgent=["","","","","",""]
#Its length has to be equal to the length of task list
print(task[1]['urgent'])
#create a list of dictionary containing only 'urgent= true' tasks
i=0#index
j=0
while(i<len(task)):
    if (task[i]['urgent'] == True):
        task_urgent[j]=task[i]['todo']
        print(task_urgent[j])
        j=j+1
    i=i+1
print(task_urgent)