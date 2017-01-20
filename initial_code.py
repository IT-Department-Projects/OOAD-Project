Skip to content
This repository
Search
Pull requests
Issues
Gist
 @aimananees
 Unwatch 1
  Star 0
 Fork 1 aimananees/OOAD-Project
forked from IT-Department-Projects/OOAD-Project
 Code  Pull requests 0  Projects 0  Wiki  Pulse  Graphs  Settings
Branch: patch-1 Find file Copy pathOOAD-Project/initial_program.py
0e7c1c0  4 hours ago
@aimananees aimananees Create initial_program.py
1 contributor
RawBlameHistory     
910 lines (649 sloc)  27.6 KB
class PATIENT:
    
    
    def get_registration(self):
        import random
        reg_num = ""

        e = open("c:\\Datafile\\Existing_Reg_Numbers.txt","r")
        existing_nos = []
        for line in e:
            existing_nos.append(line.strip())
        e.close()

        a= open("c:\\Datafile\\Pass.txt","r")
        
        b=[]
        for str1 in a:
            b.append(str1.strip())
          
        a.close()

        ### This snippet below checks if the random reg_no being generated has not already been generated earlier
        ### All registration numbers are stored in the file Existing_Reg_Numbers.txt
        ### When a new Doctor/Patient is newly registered, then the reg_no is stored in the file Existing_Reg_Numbers.txt
        
        while True:
            for i in range(3):
                i=random.randint(0,len(b))
                reg_num=reg_num+b[i]
            
            if reg_num not in existing_nos:
                break

        return reg_num
        
    

    def input_details(self):
       
        print "Step 1 of 2: Patient Information: "
        self.name= raw_input("Patient's Name: ")
        self.gender= raw_input("Gender: ")
        while True:
            if self.gender.lower() == "male" or self.gender.lower() == "female":
                break
            else:
                print 
                print
                print "Enter a valid gender.."
                self.gender=raw_input("Gender: ")
            
        self.nationality= raw_input("Nationality: ")
        self.birth= raw_input("Date of Birth(dd/mm/yyyy): ")
        while True:
            
            if self.birth[2]== "/" and self.birth[5]== "/":
                break
            else:
                print
                print
                print "Please enter a valid date.."
                self.birth=raw_input("Date of Birth(dd/mm/yyyy): ")
                
        self.street= raw_input("Street Address: ")
        self.mobile= input("Mobile number: ")
        a=str(self.mobile)
        while True:
            if len(a)==10:
                break
            else:
                print
                print
                print "Please enter a valid number.."
                self.mobile= raw_input("Mobile number: ")
                

           
        self.email= raw_input("Email: ")
        while True:
            if "@" in self.email and ".com" in self.email:
                break
            else:
                print
                print
                print "Enter a valid email id.."
                self.email=raw_input("Email: ")
        self.pro=raw_input("Enter profession: ")
        
        print
        print
        print
        print "Person to contact in case of emeregency."
        self.name1= raw_input("Name: ")
        self.mobile1= input("Mobile number: ")
        b=str(self.mobile1)
        while True:
            if len(b) == 10:
                break
            else:
                print
                print
                print "Enter a valid number.."
                self.mobile1= input("Mobile number: ")
        print
        print
        print
        

        print "Step 2 of 2: Insurance Information: "
        self.insure= raw_input("Insurance Name: ")
        self.insure_registration= raw_input("Registration number: ")

        while True:
            if self.insure_registration.isdigit():
                break
            else:
                print
                print
                print "Please enter a valid registration number.."
                self.insure_registration= raw_input("Registration number: ")
        
                
        self.expiry= raw_input("Expiry Date: ")

        self.reg_no = self.get_registration()

        reg_file = open("c:\\Datafile\\Existing_Reg_Numbers.txt","a")
        reg_file.write(self.reg_no+"\n")
        reg_file.close()

        
        self.f = open("c:\\Datafile\\"+self.reg_no+".txt",'a')
        self.f.write("Name: "+self.name+'\n')
        self.f.write("Gender: "+self.gender+'\n')
        self.f.write("Nationality: "+self.nationality+'\n')
        self.f.write("D.O.B: "+str(self.birth)+'\n')
        self.f.write("Street Address: "+self.street+'\n')
        self.f.write("Mobile Number: "+str(self.mobile)+'\n')
        self.f.write("Email id: "+self.email+'\n')
        self.f.write("Profession: "+self.pro+'\n')
        self.f.write("---------------------In Case Of Emergency------------------------------+'\n'")
        self.f.write("Name: "+self.name1+'\n')
        self.f.write("Mobile Number: "+str(self.mobile1)+'\n')
        self.f.write("---------------------Insurance Information-----------------------------+'\n'")
        self.f.write("Insurance Name: "+self.insure+'\n')
        self.f.write("Registration Number: "+str(self.insure_registration)+'\n')
        self.f.write("Expiry: "+str(self.expiry)+'\n')

    
        
        self.f.close()
        

        
        
        print "Congratulations!! You have successfully registered..."
        print "Your File number is:",self.reg_no


    

    def edit_details(self):
        self.open1=raw_input("Re-Enter your File Number: ")
        self.open2=open("c:\\Datafile\\"+self.open1+".txt","r")
        self.e1=[]

        for line in self.open2:
            line = line.rstrip('\n')
            self.e1.append(line)
        self.open2.close()

       
        
        
        self.open3=open("c:\\Datafile\\"+self.open1+".txt","w")
        self.open3.write(self.e1[0]+'\n')
        self.open3.write(self.e1[1]+'\n')
        self.open3.write(self.e1[2]+'\n')
        self.open3.write(self.e1[3]+'\n')
              

        self.f1=raw_input("Press 'yes' to change street: ")
        if self.f1 == "yes":
            self.f2=raw_input("Enter street: ")
            self.open3.write("Street Address: "+self.f2+'\n')
        else:
            self.open3.write(self.e1[4]+'\n')
            
        

        self.g1=raw_input("Press 'yes' to change mobile number: ")
        if self.g1 == "yes":

            
            self.g12=raw_input("Enter mobile number: ")
            while True:
                if len(self.g12) == 10:
                    break
                else:
                    print
                    print
                    print "Enter a valid number: "
                    self.g12=raw_input("Enter mobile number: ")
                    
            self.open3.write("Mobile Number: "+self.g12+'\n')
        else:
            self.open3.write(self.e1[5]+'\n')
            
            

        self.k1=raw_input("Press 'yes' to change email id: ")
        if self.k1 == "yes":
            self.k2=raw_input("Enter email id: ")
            while True:
                if "@" in self.k2 and ".com" in self.k2:
                    break
                else:
                    print
                    print
                    print "Enter a valid email id.."
                    self.k2=raw_input("Enter email id: ")
                    
            self.open3.write("Email id: "+self.k2+'\n')
        else:
            self.open3.write(self.e1[6]+'\n')
            

        self.l1=raw_input("Press 'yes' to change profession: ")
        if self.l1 == "yes":
            self.l2=raw_input("Enter profession: ")
            self.open3.write("Profession: "+self.l2+'\n')
        else:
            self.open3.write(self.e1[7]+'\n')

        self.open3.write("---------------------In Case Of Emergency------------------------------+'\n'")
            
            

        print
        print

        print "In Case of Emergency"

        self.m1=raw_input("Press 'yes' to change name: ")
        if self.m1 == "yes":
            self.l2 = raw_input("Enter name: ")
            self.open3.write("Name: "+self.l2+'\n')
        else:
            self.open3.write(self.e1[9]+'\n')
            
            

        self.n1=raw_input("Press 'yes' to change mobile number: ")
        if self.n1 == "yes":
            self.n2 = raw_input("Enter number: ")
            while True:
                if len(self.n2) == 10:
                    break
                else:
                    print
                    print
                    print "Please enter a valid number.."
                    self.n2 = raw_input("Enter number: ")
                    
            self.open3.write("Mobile Number: "+self.n2+'\n')
        else:
            self.open3.write(self.e1[10]+'\n')

        
        self.open3.write("---------------------Insurance Information-----------------------------+'\n'")
        print
        print
        print "Insurance Section"


        self.o1=raw_input("Press 'yes' to make any changes in Insurance Section: ")
        if self.o1 == "yes":
            self.o2=raw_input("Enter Insurance Name: ")
            self.open3.write("Insurance Name: "+self.o2+'\n')
        
        
            self.p2=raw_input("Enter registration number: ")
            self.open3.write("Registration Number: "+self.p2+'\n')
            
            

        
            self.q2=raw_input("Enter expiry date(dd/mm/yyyy): ")
            while True:
                if self.q2[2]== "/" and self.q2[5]== "/":
                    break
            else:
                print
                print
                print "Please enter a valid date.."
                self.q2=raw_input("Enter expiry date(dd/mm/yyyy): ")
                
            self.open3.write("Expiry: "+self.q2+'\n')
        else:
            self.open3.write(self.e1[12]+'\n')
            self.open3.write(self.e1[13]+'\n')
            self.open3.write(self.e1[14]+'\n')
            
            
            
            
            

        self.open3.close()


class DOCTOR:
    
    
    def get_registration(self):
        import random
        reg_num = ""

        e = open("c:\\Datafile\\Existing_Reg_Numbers.txt","r")
        existing_nos = []
        for line in e:
            existing_nos.append(line.strip())
        e.close()

        a= open("c:\\Datafile\\Pass.txt","r")
        
        b=[]
        for str1 in a:
            b.append(str1.strip())
          
        a.close()

        ### This snippet below checks if the random reg_no being generated has not already been generated earlier
        ### All registration numbers are stored in the file Existing_Reg_Numbers.txt
        ### When a new Doctor/Patient is newly registered, then the reg_no is stored in the file Existing_Reg_Numbers.txt
        
        while True:
            for i in range(3):
                i=random.randint(0,len(b))
                reg_num=reg_num+b[i]
            
            if reg_num not in existing_nos:
                break

        return reg_num
        
    

    def input_details(self):
       
        print "Step 1 of 2: Doctor Information: "
        self.name= raw_input("Doctor's Name: ")
        self.gender= raw_input("Gender: ")
        while True:
            if self.gender.lower() == "male" or self.gender.lower() == "female":
                break
            else:
                print 
                print
                print "Enter a valid gender.."
                self.gender=raw_input("Gender: ")
            
        self.nationality= raw_input("Nationality: ")
        self.birth= raw_input("Date of Birth(dd/mm/yyyy): ")
        while True:
            
            if self.birth[2]== "/" and self.birth[5]== "/":
                break
            else:
                print
                print
                print "Please enter a valid date.."
                self.birth=raw_input("Date of Birth(dd/mm/yyyy): ")
        
        
        self.street= raw_input("Street Address: ")
        self.mobile= input("Mobile number: ")
        a=str(self.mobile)
        while True:
            if len(a)==10:
                break
            else:
                print
                print
                print "Please enter a valid number.."
                self.mobile= raw_input("Mobile number: ")
                

           
        self.email= raw_input("Email: ")
        while True:
            if "@" in self.email and ".com" in self.email:
                break
            else:
                print
                print
                print "Enter a valid email id.."
                self.email=raw_input("Email: ")
        self.pro=raw_input("Enter Speciality: ")
        
        print
        print
        print
        print "Person to contact in case of emeregency."
        self.name1= raw_input("Name: ")
        self.mobile1= input("Mobile number: ")
        b=str(self.mobile1)
        while True:
            if len(b) == 10:
                break
            else:
                print
                print
                print "Enter a valid number.."
                self.mobile1= input("Mobile number: ")
        print
        print
        print
        

        '''
        print "Step 2 of 2: Insurance Information: "
        self.insure= raw_input("Insurance Name: ")
        self.insure_registration= raw_input("Registration number: ")
        while True:
            if self.insure_registration.isdigit():
                break
            else:
                print
                print
                print "Please enter a valid registration number.."
                self.insure_registration= raw_input("Registration number: ")
        
                
        self.expiry= raw_input("Expiry Date: ")
        '''

        self.reg_no = self.get_registration()
        
        reg_file = open("c:\\Datafile\\Existing_Reg_Numbers.txt","a")
        reg_file.write(self.reg_no+"\n")
        reg_file.close()
        
        self.f = open("c:\\Datafile\\"+self.reg_no+".txt",'a')
        self.f.write("Name: "+self.name+'\n')
        self.f.write("Gender: "+self.gender+'\n')
        self.f.write("Nationality: "+self.nationality+'\n')
        self.f.write("D.O.B: "+str(self.birth)+'\n')
        self.f.write("Street Address: "+self.street+'\n')
        self.f.write("Mobile Number: "+str(self.mobile)+'\n')
        self.f.write("Email id: "+self.email+'\n')
        self.f.write("Profession: "+self.pro+'\n')
        self.f.write("---------------------In Case Of Emergency------------------------------+'\n'")
        self.f.write("Name: "+self.name1+'\n')
        self.f.write("Mobile Number: "+str(self.mobile1)+'\n')
        
        '''
        self.f.write("---------------------Insurance Information-----------------------------+'\n'")
        self.f.write("Insurance Name: "+self.insure+'\n')
        self.f.write("Registration Number: "+str(self.insure_registration)+'\n')
        self.f.write("Expiry: "+str(self.expiry)+'\n')
        '''
    
        
        self.f.close()
        

        
        
        print "Doctor has been successfully registered..."
        print "Employee Id is :",self.reg_no


    

    def edit_details(self):
        self.open1=raw_input("Re-Enter Employee Id: ")
        self.open2=open("c:\\Datafile\\"+self.open1+".txt","r")
        self.e1=[]

        for line in self.open2:
            line = line.rstrip('\n')
            self.e1.append(line)
        self.open2.close()

       
        
        
        self.open3=open("c:\\Datafile\\"+self.open1+".txt","w")
        self.open3.write(self.e1[0]+'\n')
        self.open3.write(self.e1[1]+'\n')
        self.open3.write(self.e1[2]+'\n')
        self.open3.write(self.e1[3]+'\n')
              

        self.f1=raw_input("Press 'yes' to change street: ")
        if self.f1 == "yes":
            self.f2=raw_input("Enter street: ")
            self.open3.write("Street Address: "+self.f2+'\n')
        else:
            self.open3.write(self.e1[4]+'\n')
            
        

        self.g1=raw_input("Press 'yes' to change mobile number: ")
        if self.g1 == "yes":

            
            self.g12=raw_input("Enter mobile number: ")
            while True:
                if len(self.g12) == 10:
                    break
                else:
                    print
                    print
                    print "Enter a valid number: "
                    self.g12=raw_input("Enter mobile number: ")
                    
            self.open3.write("Mobile Number: "+self.g12+'\n')
        else:
            self.open3.write(self.e1[5]+'\n')
            
            

        self.k1=raw_input("Press 'yes' to change email id: ")
        if self.k1 == "yes":
            self.k2=raw_input("Enter email id: ")
            while True:
                if "@" in self.k2 and ".com" in self.k2:
                    break
                else:
                    print
                    print
                    print "Enter a valid email id.."
                    self.k2=raw_input("Enter email id: ")
                    
            self.open3.write("Email id: "+self.k2+'\n')
        else:
            self.open3.write(self.e1[6]+'\n')
            

        self.l1=raw_input("Press 'yes' to change speciality: ")
        if self.l1 == "yes":
            self.l2=raw_input("Enter speciality: ")
            self.open3.write("Speciality: "+self.l2+'\n')
        else:
            self.open3.write(self.e1[7]+'\n')

        self.open3.write("---------------------In Case Of Emergency------------------------------+'\n'")
            
            

        print
        print

        print "In Case of Emergency"

        self.m1=raw_input("Press 'yes' to change name: ")
        if self.m1 == "yes":
            self.l2 = raw_input("Enter name: ")
            self.open3.write("Name: "+self.l2+'\n')
        else:
            self.open3.write(self.e1[9]+'\n')
            
            

        self.n1=raw_input("Press 'yes' to change mobile number: ")
        if self.n1 == "yes":
            self.n2 = raw_input("Enter number: ")
            while True:
                if len(self.n2) == 10:
                    break
                else:
                    print
                    print
                    print "Please enter a valid number.."
                    self.n2 = raw_input("Enter number: ")
                    
            self.open3.write("Mobile Number: "+self.n2+'\n')
        else:
            self.open3.write(self.e1[10]+'\n')

        '''
        self.open3.write("---------------------Insurance Information-----------------------------+'\n'")
        print
        print
        print "Insurance Section"
        self.o1=raw_input("Press 'yes' to make any changes in Insurance Section: ")
        if self.o1 == "yes":
            self.o2=raw_input("Enter Insurance Name: ")
            self.open3.write("Insurance Name: "+self.o2+'\n')
        
        
            self.p2=raw_input("Enter registration number: ")
            self.open3.write("Registration Number: "+self.p2+'\n')
            
            
        
            self.q2=raw_input("Enter expiry date(dd/mm/yyyy): ")
            while True:
                if self.q2[2]== "/" and self.q2[5]== "/":
                    break
            else:
                print
                print
                print "Please enter a valid date.."
                self.q2=raw_input("Enter expiry date(dd/mm/yyyy): ")
                
            self.open3.write("Expiry: "+self.q2+'\n')
        else:
            self.open3.write(self.e1[12]+'\n')
            self.open3.write(self.e1[13]+'\n')
            self.open3.write(self.e1[14]+'\n')
            
         
        '''    
            
            

        self.open3.close()   
            

                
import os
import os.path


e="yes"
while e == "yes":
    s1= PATIENT()
    
    print "--------------------------------------------------------------------------------------------------------------------------"
    print "Welcome to ABC Hospital"
    print "--------------------------------------------------------------------------------------------------------------------------"
    print
    print
    print "1.Doctor's Section"
    print "2.Patient's Section"
    print "--------------------------------------------------------------------------------------------------------------------------"
    print
    print


    c= input("Enter your choice: ")
    cd= [1,2]
    while True:
        if c in cd:
            break
        else:
            print
            print
            print "Enter a valid choice.."
            c= input("Enter your choice: ")
    
    if c == 1:
        print "Doctor's Section"
        print "1.Add Patient"
        print "2.View Doctor's Information"
        print "3.Edit Doctor's Information"
        print "4.Delete Doctor"
        print "-------------------------------------------------------------------------------------------------------------------------"
        print
        print
        
        
        g=input("Enter your choice: ")
        gd=[1,2,3,4]
        while True:
            if g in gd:
                break
            else:
                print
                print
                print "Enter a valid choice.."
                g=input("Enter your choice: ")
                

        if g == 1:
            
            ####First Option-Add Doctor####
            print "Welcome to Doctor Registration Portal.."
            s1.input_details()
            
            print "Added the details..."
            
        elif g == 2:
            s2=DOCTOR()
            ####Second Option-View Doctor####
            z=raw_input("File Number: ")
            


            
            while True:
                PATH="c:\\Datafile\\"+z+".txt"    

                if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
                
                    ifile=open("c:\\Datafile\\"+z+".txt","r")

                    for line in ifile:
                        print line
                    ifile.close()
                    break
                else:
                    print
                    print
                    print "Please enter a valid file number.."
                    z=raw_input("File Number: ")
                    
        elif g == 3:
            ####Third Option-Edit Doctor####
            z1=raw_input("Enter File Number: ")
            
            

            while True:
                PATH=("c:\\Datafile\\"+z1+".txt")
                
                if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
                    ofile=open("c:\\Datafile\\"+z1+".txt","r")
                    s1.edit_details()
                    
                    break
                else:
                    print
                    print
                    print "Please enter a valid file number.."
                    z1=raw_input("Enter File Number: ")

            
            
                    
           

        elif g == 4:
            ####Forth Option-Delete File####
            z1=raw_input("Enter Employee Id number: ")
            
            

            while True:
                PATH=("c:\\Datafile\\"+z1+".txt")
                
                if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
                    os.remove("c:\\Datafile\\"+z1+".txt")

                    ### Removing the reg number from the Existing_Reg_Numbers.txt file
                    reg_file = open("c:\\Datafile\\Existing_Reg_Numbers.txt","r")
                    reg_nos = []
                    for line in reg_file:
                        reg_nos.append(line.strip())
                    reg_file.close()

                    ### Creating a new list which does not have z1
                    new_reg_nos = []
                    for rno in reg_nos:
                        if rno == z1:
                            pass
                        else:
                            new_reg_nos.append(rno)

                    reg_file = open("c:\\Datafile\\Existing_Reg_Numbers.txt","w")
                    for rno in new_reg_nos:
                        reg_file.write(rno+"\n")
                    reg_file.close()



                    print "You have successfully deleted the file..."
                    break
                else:
                    print
                    print
                    print "Please enter a valid file number.."
                    z1=raw_input("Enter File Number: ")
        
    
    if c == 2:
        print "Patient's Section"
        print "1.Add Patient"
        print "2.View Patient's Information"
        print "3.Edit Patient's Information"
        print "4.Delete Patient"
        print "5.View Patient's Name and File number"
        print "-------------------------------------------------------------------------------------------------------------------------"
        print
        print
        
        
        g=input("Enter your choice: ")
        gd=[1,2,3,4]
        while True:
            if g in gd:
                break
            else:
                print
                print
                print "Enter a valid choice.."
                g=input("Enter your choice: ")
                

        if g == 1:
            
            ####First Option-Add Patient####
            print "Welcome to Patient Registration Portal.."
            s1.input_details()
            
            print "Added the details..."
            
        elif g == 2:
            s2=PATIENT()
            ####Second Option-View Patient####
            z=raw_input("File Number: ")
            


            
            while True:
                PATH="c:\\Datafile\\"+z+".txt"    

                if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
                
                    ifile=open("c:\\Datafile\\"+z+".txt","r")

                    for line in ifile:
                        print line
                    ifile.close()
                    break
                else:
                    print
                    print
                    print "Please enter a valid file number.."
                    z=raw_input("File Number: ")
                    
        elif g == 3:
            ####Third Option-Edit Patient####
            z1=raw_input("Enter File Number: ")
            
            

            while True:
                PATH=("c:\\Datafile\\"+z1+".txt")
                
                if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
                    ofile=open("c:\\Datafile\\"+z1+".txt","r")
                    s1.edit_details()
                    
                    break
                else:
                    print
                    print
                    print "Please enter a valid file number.."
                    z1=raw_input("Enter File Number: ")

            
            
                    
           

        elif g == 4:
            ####Forth Option-Delete File####
            z1=raw_input("Enter File Number: ")
            
            

            while True:
                PATH=("c:\\Datafile\\"+z1+".txt")
                
                if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
                    os.remove("c:\\Datafile\\"+z1+".txt")

                    ### Removing the reg number from the Existing_Reg_Numbers.txt file
                    reg_file = open("c:\\Datafile\\Existing_Reg_Numbers.txt","r")
                    reg_nos = []
                    for line in reg_file:
                        reg_nos.append(line.strip())
                    reg_file.close()

                    ### Creating a new list which does not have z1
                    new_reg_nos = []
                    for rno in reg_nos:
                        if rno == z1:
                            pass
                        else:
                            new_reg_nos.append(rno)

                    reg_file = open("c:\\Datafile\\Existing_Reg_Numbers.txt","w")
                    for rno in new_reg_nos:
                        reg_file.write(rno+"\n")
                    reg_file.close()



                    print "You have successfully deleted the file..."
                    break
                else:
                    print
                    print
                    print "Please enter a valid file number.."
                    z1=raw_input("Enter File Number: ")
        

    e = raw_input("Press 'yes' to continue else..'no': ")

Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help
