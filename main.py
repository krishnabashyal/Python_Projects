
while True:
    what_u_want = input('add/show/edit/exit?/complete: ') 
    what_u_want == what_u_want.strip()
    
    match what_u_want:
        case "add":
            task= input("enter a task : ") +"\n"
            file = open("todos.txt","r")
            tasks= file.readlines()
            file.close()
            tasks.append(task)
            
            file= open("todos.txt","w")
            file.writelines(tasks)
            file.close()
            
        case "show"|"gimme":  
            
            print ("o/ your tasks for today are:")  
            file = open("todos.txt", 'r')
            tasks = file.readlines()
            file.close()
            
            for index,items in enumerate(tasks):
                items = items.title()
                index=index+1
                sn=f"{index}.{items}" #fstring to eliminate :D extra spaces 
               # sn=sn.strip()
                print(sn)
                       
        case 'edit':
            # file = open("todos.txt","r")
            # tasks= file.readlines()
            # file.close()
            
            num = int(input("which number to edit?: "))
            num= num-1
            # given_task = tasks[num-1]
            new_task =input("enter the new task: ") +"\n"
            tasks[num]=new_task
            file = open("todos.txt","w")
            tasks=file.writelines()
            file.close()
            
            # print("the new list is ")
         
        case "complete"|"completed"|"finished"|"remove":
            file = open("todos.txt","r")
            tasks=file.readlines()
            file.close()
            
            comp_num= int(input("which numebr task did you complete?: "))
            comp_task= tasks.pop(comp_num-1).strip()
            
            
            file= open("todos.txt","w")
            file.writelines(tasks)
            file.close()
           
            print("successfully removed",r"(comp_task)","from the todo list")   
        
        case "exit":
            break
        case _:
            print("you entered an unknown command ")
print ("good luck working. ")
#dir(list) to see functions. good luck exploring   