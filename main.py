print('Tell me what you wanna do today ')
Num = int(input("enter the number of tasks you wanna do today: "))
x,y = 0,1
tasks=[] #list skipped on day 1 lol 

#print("your tasks are: ")
while (Num > x):
    task1 = input('enter your first task: ')   
    Num = Num-1
    tasks.append(task1)
     # print(y,". ", task1,)
    # y=y+1
    #think i need nested loop for the code in comments 
print ("Your tasks for today are ", tasks) 

#well got the output i wanted with this  proud proud lol
while (y<=len(tasks)):
    print(y,". ", tasks[x],)
    y=y+1
    x=x+1
