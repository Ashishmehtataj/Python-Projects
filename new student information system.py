import csv

def write_csv(info_list):
    with open('student_information.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Mobile Number","Email ID","Branch"])


        writer.writerow(info_list)
if __name__=='__main__':
    condition  = True
    student_number = 1
    while(condition):
        student_info = input("Enter student details in format : Name, Sem,Mobile_number ,Roll_number,Branch :  (Without comma's seprated values)" )
        print("Enter information " + student_info)

        information_list  = (student_info.split(' '))
        print("Enter infromation is " + str(information_list))

        print("Enter information is : \nName : ",information_list[0],"\nSem : ",information_list[1],"\nMobile number : ",information_list[2],"\nRoll number : ",student_info[3],"\nBranch : ",student_info[4])

        enter_information_check = input("Is the entered information is correct?(yes or no) : ")
        if enter_information_check == "yes":    
            write_csv(information_list)
            check_condition = input("Enter (yes or no) if you went to enter more students data ")
            if check_condition == "yes":
                condition = True
                student_number = student_number+1
            elif check_condition == "no":
                condition = False
        elif enter_information_check=="no":
                print("Please re-enter the student information")
