list=[]
def appending():
    l=input("Enter the item:")
    list.append(l)
    print("item is added")
def deleting():
    l=int(input("Enter the index"))
    del list[l]
    print("item in the index",l,'is deleted')
    print(list)
def poping():
    list.pop()
    print("Last entered item is deleted")
def display():
    print("Show the list",list)
def insertion():
    i=int(input("Enter the index:" ))
    j=input("Enter the item:")
    list.insert(i,j)
    print("item is inserted at",i)
while True:
  task=input("Enter 1.Create list\n2.append\n3.delete\n4.pop\n5.display\n6.insert\n7.Stop")
  if(task=="1"):
     n=int(input("Numbers of items in a list:"))
     for i in range(0,n):
         l=input("Enter the items:")
         list.append(l)
  elif(task=="2"):
     appending()
  elif(task=="3"): 
     deleting()
  elif(task=="4"):
     poping()
  elif(task=="5"):     
     display()  
  elif(task=="6"):
     insertion() 
  elif(task=="7"):
     break
  else:
     print("Enter correct task")


         
  