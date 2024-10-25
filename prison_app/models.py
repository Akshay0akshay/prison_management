from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Login(AbstractUser):
    user_type=models.CharField(max_length=30)
    view_password=models.CharField(max_length=30)

class PoliceReg(models.Model):
    policelog=models.ForeignKey(Login,on_delete=models.CASCADE)
    doj=models.DateField(blank=True,null=True)
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    degree=models.IntegerField()
    rank=models.CharField(max_length=30)
    p_age=models.CharField(max_length=30,null=True,blank=True)
    dob=models.DateField()
    address=models.TextField()
    police_image=models.ImageField(null=True)
    p_status=models.CharField(max_length=30,default='Pending')

class Prisoner(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    address=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=30,null=True)
    aadhar=models.CharField(max_length=30)
    crimes=models.CharField(max_length=30,null=True)
    prisoner_image=models.ImageField(null=True)
    from_date=models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=30,default='Active')
    # visitor_status=models.CharField(max_length=30,default='Disallowed')

class Duty(models.Model):
    duty_name=models.CharField(max_length=30)
    prison=models.ForeignKey(Prisoner,on_delete=models.CASCADE,null=True)
    jailor=models.ForeignKey(Login,on_delete=models.CASCADE)
    police=models.ForeignKey(PoliceReg,on_delete=models.CASCADE,null=True)
    created_date=models.DateField(auto_now_add=True)
    dutyenddate = models.DateField(null=True)
    dutystartdate = models.DateField(null=True)

class Remarks(models.Model):
    prison=models.ForeignKey(Prisoner,on_delete=models.CASCADE,null=True)
    police=models.ForeignKey(PoliceReg,on_delete=models.CASCADE,null=True)
    created_date=models.DateField(auto_now_add=True)
    action=models.CharField(max_length=30)
    remarks=models.CharField(max_length=30)
    rating = models.CharField(max_length=10,null=True)

class Parole(models.Model):
    prison=models.ForeignKey(Prisoner,on_delete=models.CASCADE,null=True)
    police=models.ForeignKey(PoliceReg,on_delete=models.CASCADE,null=True)
    created_date=models.DateField(auto_now_add=True)
    from_date=models.DateField()
    to_date=models.DateField()
    reason=models.CharField(max_length=30)
    status=models.CharField(max_length=30,default='Pending')

class Visitor(models.Model):
    prison=models.ForeignKey(Prisoner,on_delete=models.CASCADE,null=True)
    police=models.ForeignKey(PoliceReg,on_delete=models.CASCADE,null=True)
    created_date=models.DateField(auto_now_add=True)
    visitor_name=models.CharField(max_length=30)
    visitor_phone=models.CharField(max_length=30)
    visitor_alloted_time = models.CharField(max_length=30,null=True)
    visitor_time=models.TimeField(auto_now_add=True,null=True)
    visitor_relation=models.CharField(max_length=30,null=True)
    visitor_image=models.FileField(null=True)

