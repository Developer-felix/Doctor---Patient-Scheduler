import time
doctors = {"Smith": "Anesthesiologist", 'Johnson': 'Cardiologist', "Williams":"Dermatologist", "Jones":"Neurologist", "Ugwonali":"Orthopedic Surgeon"}
timing =  ['9.00am', '9.30am', '10.00am','10.30am','11.00am','11.30am','12.00pm','12.30pm','1.00pm','3.00pm','3.30pm','4.00pm','4.30pm','5.00pm','5.30pm','6.00pm', '6.30pm', '7.00pm','7.30pm','8.00pm']
class Patient(object):
    def __int__(self,dc,sp,fn,ln,age,date):
        self.dc = dc
        self.sp = sp
        self.fn = fn
        self.ln = ln
        self.age = age
        self.date = date
    def schedule_time(self,dc,sp,fn,ln,age,date):
        duplicate_date = date
        date = timing
        print ("Doctor will be available in below time slots")
        for i in timing:
            print (i)
        while(True):
            a = input("Please enter required slot: ")
            if(a in date):
                date.remove(a)
                break
            else:
                print ("The required slot is not present Please select other slot")
        appointment_schedule = "Name of Doctor : {x} \t, Specalist_in: {y} \t, First_Name of Patient: {z} \t, Last_Name of Patient: {e} \t, Age of Patient : {b} \t, Date of Appoitment: {c} \t, Time of Appoitment: {d}".format(x = dc,y=sp,z=fn,e=ln,b=age,c=duplicate_date,d=a)
        return appointment_schedule

while(True):
    print ("Welcome to Kaiser Hospitals")
    print ("\n")
    print ("Here are the list of doctors and his/her specialists")
    print ("\n\n")
    for key, value in doctors.items():
        print ("Name: {x}  speciality: {y}".format(x=key,y=value))
        #print "Please enter the name and specialists of a doctor to choose"
    while(True):
        dc = input("Enter the name of doctor you want to visit: ")
        if(dc == ""):
            print ("Please enter correct name")
        else:
            break
    while(True):
        sp = input("Enter the specialists: ")
        if (sp == ""):
            print ("Please enter correct name")
        else:
            break
    while(True):
        fn = input("Enter your First Name: ")
        if(fn == ""):
            print ("Please enter correct name")
        else:
            break
    while(True):
        ln = input("Enter your Last Name: ")
        if (ln == ""):
            print ("Please enter correct name")
        else:
            break
    while(True):
        age = input("Enter your Age: ")
        if (age == ""):
            print ("Please enter correct Age")
        else:
            break
    while (True):
        date = input("Please enter your desired appointment date and time (Format of date : MM-DD-YEAR):")
        if (date == ""):
            print ("Please enter correct date")
        x = time.strftime("%A", time.strptime(date, "%m-%d-%Y"))
        if (x == 'Saturday' or x == 'Sunday'):
            print ("Weekend appointments are not available, Please choose an other date")
        else:
            break
    reference  =  Patient()
    a = reference.schedule_time(dc,sp,fn,ln,age,date)
    print ("Here is your record")
    print (a)
