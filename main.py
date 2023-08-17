tasks=[]
hello =''
while True:
    what_u_want = input('You wanna add more tasks or see or exit?: ') 
    what_u_want == what_u_want.strip()
    
    match what_u_want:
        case "add":
            task= input("enter a task : ")
            tasks.append(task)
        case "show"| "gimme":
            
            for items in tasks:
                items = items.title() # this capatilizes the first letter of word 
                print(items)    
        case "exit":
            break
        case _: # can use any word after case but its our language to use _ case "yoo" was also fine 
            print("you entered an unknown command ")
print ("good luck working. ")
   
  
