
while True:
    what_u_want = input('add/show/edit/exit?/complete: ') 
    what_u_want == what_u_want.strip()
    
    match what_u_want:
        case "add":
            task= input("enter a task : ") +"\n"
        
            with open("todos.txt","r") as file:
                tasks=file.readlines() #no need to close file
                
            tasks.append(task)
            
            with open("todos.txt","w") as file:
                file.writelines(tasks)
            
            
        case "show"|"gimme":  
            
            print ("o/ your tasks for today are:")  
            with open("todos.txt", 'r') as file:
                tasks = file.readlines()
            
            #list comphrehension 
            new_tasks= [items.strip("\n") for items in tasks] #this makes new list removing \n from items of list 
            
            for index,items in enumerate(new_tasks):
                #items= items.strip("\n").. can also use this to remove \n 
                items = items.title()
                index=index+1
                sn=f"{index}.{items}" #fstring to eliminate :D extra spaces 
               # sn=sn.strip()
                print(sn)
                       
        case 'edit':
            
            with open("todos.txt","r") as file:
                tasks= file.readlines()
           
            num = int(input("which number to edit?: "))
            num= num-1
           
            new_task =input("enter the new task: ") +"\n"
            tasks[num]=new_task
            
            with open("todos.txt","w") as file:
                tasks=file.writelines(tasks)
            
        case "complete"|"completed"|"finished"|"remove":
            with open("todos.txt","r") as file:
                tasks=file.readlines()
            
            comp_num= int(input("which numebr task did you complete?: "))
            comp_task= tasks.pop(comp_num-1).strip()
            with open("todos.txt","w") as file:
            
                file.writelines(tasks)
            
            print("successfully removed",r"(comp_task)","from the todo list")   
        
        case "exit":
            break
        case _:
            print("you entered an unknown command ")
print ("good luck working. ")
