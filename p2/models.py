from django.db import models
from django.utils.timezone import now

# Create your models here.
class DeptDetails(models.Model):
    depts = (
        ('CSE','CSE'),
        ('ICT','ICT'),
        ('ECE','ECE'),
        ('MECH','MECH')
    )

    # DEPT=models.CharField(max_length=50,choices=depts,primary_key=True)
    deptID=models.CharField(max_length=10,primary_key=True,choices=depts,default="CSE")
    
    DeptName=models.CharField(max_length=150)
    
    
    class Meta:
        db_table="Department"


class StudentInfo(models.Model):
    
    depts = (
        ('CSE','CSE'),
        ('ICT','ICT'),
        ('ECE','ECE'),
        ('MECH','MECH')
    )

    
    rno = models.CharField(max_length=15,primary_key=True)
    name = models.CharField(max_length=20)
    
    email=models.CharField(max_length=100)

    age=models.DecimalField(max_digits=5,decimal_places=2)
    
    #deptID=models.CharField(max_length=10,choices=depts,default="CSE")

    deptID=models.ForeignKey(DeptDetails,null=True,on_delete=models.CASCADE)

    class Meta:
        db_table="Student_Info"


class FAC(models.Model):
    
    
    fac= {

        ('F101','F101'),
        ('F102','F102'),
        ('F103','F103'),
        ('F104','F104'),
        ('F105','F105'),
        ('F106','F106'),
        
        ('F201','F201'),
        ('F202','F202'),
        ('F203','F203'),
        ('F204','F204'),
        ('F205','F205'),
        ('F206','F206'),

        ('F301','F301'),
        ('F302','F302'),
        ('F303','F303'),
        ('F304','F304'),
        ('F305','F305'),
        ('F306','F306'),


        ('F401','F401'),
        ('F402','F402'),
        ('F403','F403'),
        ('F404','F404'),
        ('F405','F405'),
        ('F406','F406')
        ,
    
    }
    
    FacultyID=models.CharField(max_length=10,primary_key=True,choices=fac,default="F101")
    Facultyname=models.CharField(max_length=50)

    deptID=models.ForeignKey(DeptDetails,null=True,on_delete=models.CASCADE)

    class Meta:
        db_table="Faculty_Info"

class COU(models.Model):
    depts = (
        ('CSE','CSE'),
        ('ICT','ICT'),
        ('ECE','ECE'),
        ('MECH','MECH')
    )
    
    course=(
        ('C101','C101'),
        ('C102','C102'),
        ('C103','C103'),
        
        ('C201','C201'),
        ('C202','C202'),
        ('C203','C203'),
        
        ('C301','C301'),
        
        ('C302','C302'),
        ('C303','C303'),

        ('C401','C401'),
        
        ('C402','C402'),
        ('C403','C403')
        
    )



    CID=models.CharField(max_length=10,primary_key=True,choices=course,default="C101")
    Course=models.CharField(max_length=50)
    

    deptID=models.ForeignKey(DeptDetails,null=True,on_delete=models.CASCADE)

    class Meta:
        db_table="Course_Info"


class Feed(models.Model):

    course=(
        ('C101','C101'),
        ('C102','C102'),
        ('C103','C103'),
        
        ('C201','C201'),
        ('C202','C202'),
        ('C203','C203'),
        
        ('C301','C301'),
        
        ('C302','C302'),
        ('C303','C303'),

        ('C401','C401'),
        
        ('C402','C402'),
        ('C403','C403')
        
    )
    rating=(
        ('0','0'),('1','1'),('2','2'),('3','3'),('4','4')
    )

    fac= {

        ('F101','F101'),
        ('F102','F102'),
        ('F103','F103'),
        ('F104','F104'),
        ('F105','F105'),
        ('F106','F106'),
        
        ('F201','F201'),
        ('F202','F202'),
        ('F203','F203'),
        ('F204','F204'),
        ('F205','F205'),
        ('F206','F206'),

        ('F301','F301'),
        ('F302','F302'),
        ('F303','F303'),
        ('F304','F304'),
        ('F305','F305'),
        ('F306','F306'),


        ('F401','F401'),
        ('F402','F402'),
        ('F403','F403'),
        ('F404','F404'),
        ('F405','F405'),
        ('F406','F406')
        ,
    
    }
    depts = (
        ('CSE','CSE'),
        ('ICT','ICT'),
        ('ECE','ECE'),
        ('MECH','MECH')
    )

    FacultyID = models.ForeignKey(FAC,null=True,on_delete=models.CASCADE)
    
    q1 = models.CharField(max_length=50,choices=rating,default='2')
    q2 = models.CharField(max_length=50,choices=rating,default='2')
    q3 = models.CharField(max_length=50,choices=rating,default='2')
    q4 = models.CharField(max_length=50,choices=rating,default='2')
    q5 = models.CharField(max_length=50,choices=rating,default='2')
    comment = models.CharField(max_length=100)
    
    CID=models.ForeignKey(COU,null=True,on_delete=models.CASCADE)

    rno=models.ForeignKey(StudentInfo,null=True,on_delete=models.CASCADE)
    
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)
    
    
    #deptID=models.CharField(max_length=10,choices=depts,default="CSE")

    

    class Meta:
        db_table="Feedback_Table"

