from django.shortcuts import render

# Create your views here.
from .models import StudentInfo,DeptDetails,Feed,FAC,COU
def userreg(request):
    return render(request,"register.html",{})

def insertuser(request):
    
    vrno=request.POST['rno']
    vname=request.POST['name']
    vemail=request.POST['email']
    vage=request.POST['age']
    vdept=request.POST['deptID']
    vcourse=request.POST['Course']
    vfaculty=request.POST['Facultyname']
    vq1=request.POST['q1']
    vq2=request.POST['q2']
    vq3=request.POST['q3']
    vq4=request.POST['q4']
    vq5=request.POST['q5']
    vcomment=request.POST['comment']
    
    
    
    us = StudentInfo(rno=vrno,name=vname,email=vemail,age=vage,deptID=DeptDetails.objects.get(deptID=vdept))    
    us.save()
    
    us2=Feed(q1=vq1,q2=vq2,q3=vq3,q4=vq4,q5=vq5,comment=vcomment,rno=StudentInfo.objects.get(rno=vrno),CID=COU.objects.get(CID=vcourse),FacultyID=FAC.objects.get(FacultyID=vfaculty))
    us2.save()
    
    
    return render(request,'submit.html',{})

def css(request):
    return render(request,'trialcss.css')
    return render(request,'ok.css'
)

