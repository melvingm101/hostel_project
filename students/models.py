from django.db import models

# Create your models here.
class Other_Charges(models.Model):
    charge_name=models.CharField(max_length=50)
    charge_value=models.FloatField(default=0)


class Charges(models.Model):
    breakage_charges=models.FloatField(default=0)
    laundry_charges=models.FloatField(default=0)
    lost_key_charges=models.FloatField(default=0)
    other_charges=models.ForeignKey(Other_Charges,on_delete=models.CASCADE)
    guest_charges=models.FloatField(default=0)


class Student(models.Model):
    name=models.CharField(max_length=50)
    id_no=models.CharField(max_length=20)
    room_no=models.IntegerField()
    joining_date=models.DateField()
    leaving_date=models.DateField()
    block=models.CharField(max_length=1)
    charges=models.ForeignKey(Charges,on_delete=models.CASCADE)
    mob_no=models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    date_added=models.DateTimeField()

    def __str__(self):
        return self.name


class Guest(models.Model):
    name=models.CharField(max_length=50)
    CATEGORY=(('PL','Placement'),
              ('INT','Internship'),
              ('OINT','Outside Internship'),
              ('OVS','Overstay'),
              ('BFR','Before Registration'),
              ('STM','Summer Term'),
              ('PS1','PS1'),
              ('PS2E','PS2 Early'),
              ('PS2L','PS2 Late'),
              ('PRO','Project'),
              ('SG','Student Guests'),
              ('WG','WILP Guests'))
    category=models.CharField(max_length=1,choices=CATEGORY)
    room_no=models.IntegerField()
    joining_date=models.DateField()
    leaving_date=models.DateField()
    mob_no=models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    date_added=models.DateTimeField()
    charges=models.FloatField(default=0)