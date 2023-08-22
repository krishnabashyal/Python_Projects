tasks=[]
hello ='' 
while True:
    what_u_want = input('add/show/edit/exit?/complete: ') 
    what_u_want == what_u_want.strip()
    
    match what_u_want:
        case "add":
            task= input("enter a task : ")
            tasks.append(task)
            
        case "show"|"gimme":  
            
            print ("o/ your tasks for today are:")         
            for index,items in enumerate(tasks):
                items = items.title()
                index=index+1
                sn=f"{index}.{items}" #fstring to eliminate :D extra spaces 
                print(sn)
        
        case 'edit':
            num = int(input("which number to edit?: "))
            #num= num-1
            given_task = tasks[num-1]
            new_task =input("enter the new task ")
            tasks[num]=new_task
            # print("the new list is ")
         
        case "complete"|"completed"|"finished"|"remove":
            comp_num= int(input("which numebr task did you complete?: "))
            tasks.pop(comp_num-1)
            print("successfully removed",tasks[comp_num-1],"from the todo list")   
        
        case "exit":
            break
        case _:
            print("you entered an unknown command ")
print ("good luck working. ")
#dir(list) to see functions. good luck exploring 
   
  
