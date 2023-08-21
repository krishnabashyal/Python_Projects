tasks=[]
hello ='' 
while True:
    what_u_want = input('add/show/edit/exit?: ') 
    what_u_want == what_u_want.strip()
    
    match what_u_want:
        case "add":
            task= input("enter a task : ")
            tasks.append(task)
            
        case "show"|"gimme":           
            for items in tasks:
                items = items.title()
                print(items) 
                   
        case "exit":
            break
        
        case 'edit':
            num = int(input("which number to edit?: "))
            num= num-1
            given_task = tasks[num]
            new_task =input("enter the new task ")
            tasks[num]=new_task
            # print("the new list is ")
        case _:
            print("you entered an unknown command ")
print ("good luck working. ")
#dir(list) to see functions. good luck exploring 
   
  
