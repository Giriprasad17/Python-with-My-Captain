#Taking the number of elements in the list
size=int(input("Enter the size of the list:"))
#Declare an empty list
lst=[]
#Input numbers to the list
for i in range(0,size):
    lst.append(int(input()))
#Print the input
print("Input:list",lst)
#Remove negative numbers from the numpy array
newlst = list(filter(lambda x:x>0, lst))
#Print the list containing only postive numbers
print("Output:",newlst)
