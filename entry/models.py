from django.db import models
from django.contrib.auth.models import User

#-------------------------------STUDENT PERSONAL DETAILS-------------------------
class Stud_PD(models.Model):
    Sid = models.AutoField(primary_key=True)
    Sname = models.CharField(max_length=50)
    USN = models.CharField(max_length=10, unique=True)
    Male = 'Male'
    Female = 'Female'
    Others = 'Others'
    Gender_Choices = [
        (Male, 'Male'),
        (Female, 'Female'),
        (Others, 'Others'),
    ]
    Gender = models.CharField(
        max_length=6,
        choices=Gender_Choices,
        default=Male,
    )
    DOB = models.DateField()
    POB = models.CharField(max_length=50)
    S_Pno = models.CharField(max_length=10)
    S_Add = models.TextField()
    b_2019 = '2019'
    b_2020 = '2020'
    b_2021 = '2021'
    b_2022 = '2022'
    b_2023 = '2023'
    Batch_Choices =[
        (b_2019,'2019'),
        (b_2020,'2020'),
        (b_2021,'2021'),
        (b_2022,'2022'),
        (b_2023,'2023'),
    ]
    Batch=models.CharField(
        max_length=4,
        choices=Batch_Choices,
        default=b_2019,
    )
    Added_by=models.ForeignKey(User,default=None,on_delete=models.SET_DEFAULT)
    Date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.USN
#---------------------------------FEE STRUCTURE----------------------
class Fee_Str(models.Model):
    Fid=models.AutoField(primary_key=True)
    y_2019=2019
    y_2020=2020
    y_2018=2018
    y_2017=2017
    Adm_Year_Choices=[
        (y_2017,'2017'),
        (y_2018,'2018'),
        (y_2019,'2019'),
        (y_2020,'2020'),
    ]
    Adm_Year=models.IntegerField(choices=Adm_Year_Choices,default=y_2019)
    Diploma='Dip'
    CET='CET'
    Management='Mgmt'
    ChangeOfCollege='COC'
    COMEDK='COMEDK'
    GATE='GATE'
    Adm_Type_Choices=[
        (Diploma,'Diploma'),
        (CET,'CET'),
        (Management,'Management'),
        (ChangeOfCollege,'Change Of College'),
        (COMEDK,'COMEDK'),
        (GATE,'GATE')
    ]
    Adm_type=models.CharField(max_length=10,choices=Adm_Type_Choices,default=CET)
    BE='BE'
    MTECH='ME'
    MBA='MBA'
    MCA='MCA'
    AFMA='AFMA'
    Course_Choices=[
        (BE,'Bachelor Of Engineering (BE)'),
        (MTECH,'Master of Technology (MTech)'),
        (MBA,'Master Of Business Administration (MBA)'),
        (MCA,'Master Of Computer Applications (MCA)'),
        (AFMA,'(AFMA)'),
    ]
    Course=models.CharField(max_length=10,choices=Course_Choices,default=BE)
    R='Rural'
    K='Kannada'
    HK='HK'
    N='None'
    SNQ='SNQ'
    Quota_Choices=[
        (R,'Rural'),
        (K,'Kannada'),
        (HK,'Hyderabad Karnataka'),
        (SNQ,'SNQ'),
        (N,'None'),
    ]   
    Quota=models.CharField(max_length=10,choices=Quota_Choices,default=N)
    CS ='CS'
    IS ='IS'
    EC ='EC'
    CV ='CV'
    ME ='ME'
    N ='None'
    Branch_Choices=[
        (CS,'Computer Science'),
        (IS,'Information Science'),
        (EC,'Electronics And Communication'),
        (CV,'Civil'),
        (ME,'Mechanical'),
        (N,'None'),
    ]
    Branch=models.CharField(max_length=10,choices=Branch_Choices,default=N)
    Apti_1=models.IntegerField(default=None)
    Tech_2=models.IntegerField(default=None)
    Book_3=models.IntegerField(default=None)
    IndP_4=models.IntegerField(default=None)
    IndV_5=models.IntegerField(default=None)
    Inte_6=models.IntegerField(default=None)
    Libr_7=models.IntegerField(default=None)
    Semi_8=models.IntegerField(default=None)
    Soft_9=models.IntegerField(default=None)
    Conf_10=models.IntegerField(default=None)
    Subj_11=models.IntegerField(default=None)
    Spor_12=models.IntegerField(default=None)
    Tran_13=models.IntegerField(default=None)
    Tuti_14=models.IntegerField(default=None)
    Volu_15=models.IntegerField(default=None)

    Total=models.IntegerField(default=None)
    
    def __str__(self):
        return str(self.pk)
#-------------------------STUDENT ADMISSION DETAILS----------------------    
class Stud_Admn(models.Model):
    Adm_No=models.CharField(primary_key=True,max_length=20)
    Sid=models.OneToOneField(Stud_PD,on_delete=models.SET_NULL,null=True)
    BE='BE'
    MTECH='ME'
    MBA='MBA'
    MCA='MCA'
    AFMA='AFMA'
    Course_Choices=[
        (BE,'Bachelor Of Engineering (BE)'),
        (MTECH,'Master of Technology (MTech)'),
        (MBA,'Master Of Business Administration (MBA)'),
        (MCA,'Master Of Computer Applications (MCA)'),
        (AFMA,'(AFMA)'),
    ]
    Course=models.CharField(max_length=10,choices=Course_Choices,default=BE)
    F=1
    S=2
    T=3
    Fo=4
    Fi=5
    Si=6
    Se=7
    E=8
    Sem_Choices=[
        (F,'1'),
        (S,'2'),
        (T,'3'),
        (Fo,'4'),
        (Fi,'5'),
        (Si,'6'),
        (Se,'7'),
        (E,'8'),
    ]
    Sem=models.IntegerField(choices=Sem_Choices,default=F,null=False,blank=False)
    y_2019=2019
    y_2020=2020
    y_2018=2018
    y_2017=2017
    Adm_Year_Choices=[
        (y_2017,'2017'),
        (y_2018,'2018'),
        (y_2019,'2019'),
        (y_2020,'2020'),
    ]
    Adm_Year=models.IntegerField(choices=Adm_Year_Choices,default=y_2019)
    CS ='CS'
    IS ='IS'
    EC ='EC'
    CV ='CV'
    ME ='ME'
    N ='None'
    Branch_Choices=[
        (CS,'Computer Science'),
        (IS,'Information Science'),
        (EC,'Electronics And Communication'),
        (CV,'Civil'),
        (ME,'Mechanical'),
        (N,'None'),
    ]
    Branch=models.CharField(max_length=10,choices=Branch_Choices,default=N)
    Diploma='Dip'
    CET='CET'
    Management='Mgmt'
    ChangeOfCollege='COC'
    COMEDK='COMEDK'
    GATE='GATE'
    Adm_Type_Choices=[
        (Diploma,'Diploma'),
        (CET,'CET'),
        (Management,'Management'),
        (ChangeOfCollege,'Change Of College'),
        (COMEDK,'COMEDK'),
        (GATE,'GATE')
    ]
    Adm_Type=models.CharField(max_length=10,choices=Adm_Type_Choices,default=CET)
    R='Rural'
    K='Kannada'
    HK='HK'
    N='None'
    SNQ='SNQ'
    Quota_Choices=[
        (R,'Rural'),
        (K,'Kannada'),
        (HK,'Hyderabad Karnataka'),
        (SNQ,'SNQ'),
        (N,'None'),
    ]   
    Quota=models.CharField(max_length=10,choices=Quota_Choices,default=N)
    Fid=models.ForeignKey(Fee_Str,on_delete=models.SET_DEFAULT,default=1)
    
    def __str__(self):
        return str(self.Adm_No)

# ----------------------- DESIGNATION TYPES -------------------------------------

class F_Teach_Nonteach(models.Model):
    HOD='HOD & Prof'
    PROF='Prof'
    AscP='Asc Prof'
    AsstP='Asst Prof'
    Atten='Attender'
    F='Foreman'
    W='Watchman'
    L='Lab Tech'
    I='Instructor'
    Designation_Choices=[
        (HOD,'HOD & Prof'),
        (PROF,'Prof'),
        (AscP,'Asc Prof'),
        (AsstP,'Asst Prof'),
        (Atten,'Attender'),
        (F,'Foreman'),
        (W,'Watchman'),
        (L,'Lab Tech'),
        (I,'Instructor'),
    ]
    Designation=models.CharField(max_length=20,choices=Designation_Choices,default=AsstP,unique=True)
    T='Teaching'
    N='Non_Teaching'
    Type_Choices=[
        (T,'Teaching'),
        (N,'Non-Teaching'),
    ]
    Type=models.CharField(max_length=20,choices=Type_Choices,default=T)

    def __str__(self):
        return self.Designation

#------------------------FACULTY TABLE-----------------------------------

class Faculty(models.Model):
    FID=models.AutoField(primary_key=True)
    F_Name=models.CharField(max_length=40)
    F_Designation=models.ForeignKey(F_Teach_Nonteach,on_delete=models.SET_NULL,null=True)
    CS='CS'
    IS='IS'
    EC='EC'
    CV='CV'
    ME='ME'
    MTECH='ME'
    MBA='MBA'
    MCA='MCA'
    AFMA='AFMA'
    O='Office'
    S='Security'
    Dept_Choices=[
        (CS,'CS'),
        (IS,'IS'),
        (EC,'EC'),
        (CV,'CV'),
        (ME,'ME'),
        (MTECH,'ME'),
        (MBA,'MBA'),
        (MCA,'MCA'),
        (AFMA,'AFMA'),
        (O,'Office'),
        (S, 'Security'),
    ]
    Dept=models.CharField(max_length=10,choices=Dept_Choices,default=CS)
    Qualification=models.CharField(max_length=50)
    Experience=models.IntegerField(default=0)
    Address=models.TextField()
    Email=models.EmailField(unique=True)
    Phone_No=models.CharField(max_length=10,unique=True)
    Date_Of_Join=models.DateField()
    Working_Status=models.BooleanField(default=True)
    
    Username=models.OneToOneField(User,default=None,on_delete=models.CASCADE,unique=True)

    def __str__(self):
        return self.F_Name

#----------------------STUDENT FEES----------------------------------------------

class Stud_Fees(models.Model):
    
    Adm_No_S=models.OneToOneField(Stud_Admn,on_delete=models.PROTECT)
    Apti_1_Paid=models.IntegerField(default=0)
    Tech_2_Paid=models.IntegerField(default=0)
    Book_3_Paid=models.IntegerField(default=0)
    IndP_4_Paid=models.IntegerField(default=0)
    IndV_5_Paid=models.IntegerField(default=0)
    Inte_6_Paid=models.IntegerField(default=0)
    Libr_7_Paid=models.IntegerField(default=0)
    Semi_8_Paid=models.IntegerField(default=0)
    Soft_9_Paid=models.IntegerField(default=0)
    Conf_10_Paid=models.IntegerField(default=0)
    Subj_11_Paid=models.IntegerField(default=0)
    Spor_12_Paid=models.IntegerField(default=0)
    Tran_13_Paid=models.IntegerField(default=0)
    Tuti_14_Paid=models.IntegerField(default=0)
    Volu_15_Paid=models.IntegerField(default=0)

    Total=models.IntegerField()
    Paid=models.IntegerField(default=0)
    Due=models.IntegerField()
    Last_Date_Paid=models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return str(self.Adm_No_S)

#--------------------------------FEE RECORD-------------------------------------------

class Fee_Record(models.Model):

    Stud_Fee_ID=models.ForeignKey(Stud_Fees,on_delete=models.PROTECT)
    Fee_Paid=models.IntegerField(default=0)
    Date_Paid=models.DateTimeField(auto_now_add=True,editable=False)
    
    Added_by=models.ForeignKey(User,default=None,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return str(self.Date_Paid)