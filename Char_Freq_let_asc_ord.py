#python program to get the frequency of characters in a string in ascending order of letters
#Input the string

word = input("Input:Please enter a string\n")

#create an empty dictionary
           
dic = {}
           
#getting characters from string

for ch in word:
    if ch in dic:
           dic[ch]+=1      #if character is already present in dict increse its count by one
    else:
           dic[ch]=1      #else assing it for the first time in the dictionary
           
lis = list(dic.items())    #convert given dictionary into list

lis.sort()                 #sort the letters in ascending order

print("Output:\n")
for i in range (0,len(lis)):
    for j in range(0,2):
          if j%2==0:
                print(lis[i][j],end=" = ")
          else:
                print(lis[i][j])
