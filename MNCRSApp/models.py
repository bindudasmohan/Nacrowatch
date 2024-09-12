from django.db import models
# Create your models here.
class Registration(models.Model):
    Nick_Name=models.CharField(max_length=50)
    Pass_Word = models.IntegerField()
    Security_Question = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Contact_Num = models.CharField(max_length=50)
    Blocked = models.CharField(max_length=50)
    #Image = models.CharField(max_length=50)

class Investigator_Registration(models.Model):
     Nick_Name = models.CharField(max_length=50)
     Pass_Word = models.IntegerField()
     District = models.CharField(max_length=50)
     State = models.CharField(max_length=50)
     Email = models.CharField(max_length=50)
     Office_Code = models.CharField(max_length=50)
     Contact_Num = models.CharField(max_length=50)
     Image =  models.CharField(max_length=50)


class Login(models.Model):
    Email = models.CharField(max_length=50)
    Pass_Word = models.IntegerField()

class Reporter_Form(models.Model):
    Reporter_ID = models.ForeignKey(Registration, on_delete=models.CASCADE)
    Date_and_time = models.DateField()
    Report_text = models.TextField()
    Proof_Image = models.CharField(max_length=100)
    Proof_clip = models.CharField(max_length=100)
    Status = models.CharField(max_length=50)


class Crime_Reporting(models.Model):
    Reporter_ID = models.ForeignKey(Registration, on_delete=models.CASCADE)
    Date_and_time = models.DateField()
    Report_text = models.TextField()
    Proof_Image = models.CharField(max_length=100)
    Proof_clip = models.CharField(max_length=100)
    Status = models.CharField(max_length=50)
    Investigator_ID = models.IntegerField(null=True)


class Investigation_Process(models.Model):
    CASE_ID = models.IntegerField()
    Status = models.CharField(max_length=50)
    Investigator_ID = models.IntegerField()
    Investigator_Name = models.CharField(max_length=50)
    Investigator_Office_Code = models.CharField(max_length=50)
    Investigator_Report = models.TextField()
    Date_and_time = models.DateField()

class Feedback_form(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    sub = models.CharField(max_length=50)
    message = models.CharField(max_length=50)

class authentication(models.Model):
    email = models.CharField(max_length=50)