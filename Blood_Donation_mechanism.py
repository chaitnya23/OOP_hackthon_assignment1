class Donor:

    def __init__(self ,name,group) :
        self.name = name
        self.group = group 
        

exit = False

blood_groups=['AB-','AB+','O-','O+','A+','A-','B-','B+']
exit_admin = False
blood_requests={'O-':0 ,'A-':0 ,'AB+':0 ,'B-':0 ,'B+':0 ,'AB-':0 ,'A+':0 ,'O+':0}
Donors_list={}
hospitals=[]
requests_from_admin={}
available_blood_groups={'O-':0 ,'A-':0 ,'AB+':0 ,'B-':0 ,'B+':0 ,'AB-':0 ,'A+':0 ,'O+':0}

print("welcome to the blood bank automatic system ")

while(exit!=True):
    flag=0
    print("please choose an option")
    print("1 .admin panal")
    print("2 .Donor panal")
    print("3 .Make emergency Request")
    print("4 .Add hopital name having blood camp(for only admins)")
    print("5 .exit\n\n")    
    n=int(input()) 

    if(n==1):
        while(exit_admin==False):
            print("1. get the donors list") 
            print("2. get avalaible blood info")
            print("3. get blood requests")
            print("4. get list of hospitals conducting blood donating camps")
            print("5. exit\n\n")
            n1=int(input())
            if(n1==1):
                print(Donors_list)

            elif(n1==2):
                print(available_blood_groups)    

            elif(n1==3):
                print(blood_requests)
                print("1. want to notify the donor")
                print("2. exit\n\n")
                n3 = int(input())
            
                if(n3==1):
                    print(Donors_list)
                    notify_to=input("enter name :")
                    bg2 = input("enter blood group :")
                    requests_from_admin.update({notify_to:bg2})

            else:
                break        


    elif(n==2):
       
        print("1. want to donate blood")
        print("2. see the requests \n\n")
        n2=input()
        if(n2=='1'):
            d_name = input("enter your name :")
            d_blood_group = input("Enter your blood group :")
            d_age = input("Enter your age: ")
            d_gender = input("Enter your gender: ")
            for bg in blood_groups:
                if(bg==d_blood_group):
                    flag=1
            if(flag!=1):
                print("enter a valid blood group\n")        
                continue
            d1 = Donor(d_name,d_blood_group)
            Donors_list.update({d1.name:d_blood_group})
            available_blood_groups[d1.group]+=1
        elif(n2=='2'):
            person = input("Enter Your Name :")
            print("Request for you from blood bank....\n")
            print(requests_from_admin[person])
            temp = int(input("1. accept 2.deny"))
            if(temp==1):
                del requests_from_admin[person]
        else:
            print("Enter a valid option...\ntry again\n")
            continue
              


    elif(n==3):
        print("Make a request for the blood group: ")
        bg = input()
        blood_requests[bg]+=1

    elif(n==4):
        hospital_name = input("enter name of hospital :")   
        hospitals.append(hospital_name)

    elif(n==5):
        break
    else:
        print("Enter a valid option...\ntry again\n")
        continue
      






