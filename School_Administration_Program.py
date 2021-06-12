#OBTAIN INFORMATIONM FROM THE USER

con = True
student_num=1

import csv

#Write the heading of each columns for the csv file

file = open('Student_Admin_list.csv','w')
with open('Student_Admin_list.csv','a',newline='') as csv_file:
          writer =csv.writer(csv_file)
          writer.writerow(["Name","Age","Contact_info","Email_ID"])


#Define function to write as csv file

def write_csv(info_list): #provide the split info into the file as comma separated values(CSV)
      with open('Student_Admin_list.csv','a',newline='') as csv_file:
          writer =csv.writer(csv_file)
          writer.writerow(info_list)

#Declare the code after this as our entry point

if __name__=='__main__':

 while(con):
    student_info = input("Enter the student information in the format (name Age Contact_number Email_ID): ")
    student_num
    #split function
    split_list = student_info.split(" ") #split the string every time a space is observed
    
    #To check the enterd values manually
    
    print("\nThe Entered information of student number {} is-\nNmae: {}\nAge: {}\nContact_info: {}\nEmail_ID: {}".format(student_num,split_list[0],split_list[1],split_list[2],split_list[3] ))

    #Ask the user if the information printed above is true or not
    
    check = input("\nIs the Entered Information Correct:(y/n): ")
    if check =='y':
      write_csv(split_list)
      student_num+=1
      con_check =input("\nEnter yes or no (y/n) if you want to enter information for another student:")
    
      if (con_check == "y"):
        con = True
      elif (con_check == "n"): 
        con = False
    elif check=='n':
          print("\nPlease Re-Enter the Student Information Again.")
