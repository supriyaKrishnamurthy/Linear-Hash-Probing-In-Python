import sys


size=int(input("Enter the Hash Table size: "))
modfn=int(input("Enter the mod function: "))


newlist=[None for x in range(size)]
print(newlist)


def insert(listname,key):
    pos=key%modfn
    
    while(pos<=len(listname)):
            
            if listname[pos]!=None:
                pos=pos+1
                
                if pos==key%modfn:
                    print("Cannot insert!!!Hash table full")
                    break
                elif pos>=len(listname):
                    pos=0
            else:
                listname[pos]=key
                break
                
    return listname




def display(listname):
    for i in range(len(listname)):
        print(i,end=" ")
        print(listname[i])


def search(listname,key):
    pos=key%modfn
    flag=0
    while(pos<len(listname)):
            
            if listname[pos]==key:
                print("Successfully found",key," at ",pos)
                flag=1
                break
            else:
                pos=pos+1
    if flag==0:
        print("Element ",key ," not found")
        
#Driver program

while(1):
    
    print(" 1-> Insert\n 2-> Display\n 3-> Searching\n 4-> Exit\n")
    choice=int(input("Enter your Choice: "))
    
    if choice==1:
        ele=int(input("Enter key element to insert: \n"))
        insert(newlist,ele)
        
    elif choice==2:
        display(newlist)
        
    elif choice==3:
        ele=int(input("Enter key element to search: \n"))
        search(newlist,ele)
        
    else:
        sys.exit()
