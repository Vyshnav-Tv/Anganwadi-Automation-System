from django.db import models

# Create your models here.
class id_gen(models.Model):  
    anganwadi_id= models.IntegerField()
    foodM_id= models.IntegerField()
    staf_id= models.IntegerField()
    student_id= models.IntegerField()
    prg_women_id= models.IntegerField()
    infant_id= models.IntegerField()
    vaccine_id= models.IntegerField()
    art_id= models.IntegerField()
    noti_id= models.IntegerField()
    mess_id= models.IntegerField()
    allot_id= models.IntegerField()
    compl_id=models.IntegerField()
    class Meta:
        db_table="id_gen" 

class login_table(models.Model):
    username=models.CharField(max_length=90)
    password=models.CharField(max_length=90)
    category=models.CharField(max_length=90)
    class Meta:

        db_table = "loging_table"

class anganwadi_table(models.Model):
    angan_id= models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=30)
    dist = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    build_num = models.CharField(max_length=30)
    owner_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    
    class Meta:
        db_table="anganwadi_table" 

class foodmaster_table(models.Model):
    food_id= models.CharField(primary_key=True, max_length=30)
    item_name = models.CharField(max_length=30)
    qty = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    discription= models.CharField(max_length=30)
    
    class Meta:
        db_table="foodmaster_table"

class vaccine_table(models.Model):
    vac_id= models .CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    discription= models.CharField(max_length=30)
    
    class Meta:
        db_table="vaccine_table"




class staf_table(models.Model):
    stf_id= models.CharField(primary_key=True, max_length=30)
    staf_name = models.CharField(max_length=30)
    id_angan = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    dob= models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    photo= models.CharField(max_length=30)
    class Meta:
        db_table="staf_table" 

class student_table(models.Model):
    stud_id= models.CharField(primary_key=True, max_length=30)
    anganw_id = models.CharField(max_length=30)
    stud_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    
    class Meta:
        db_table="student_table"

class women_table(models.Model):
    women_id= models.CharField(primary_key=True, max_length=30)
    agn_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    d_date = models.CharField(max_length=30)
    status= models.CharField(max_length=30)
    phone= models.CharField(max_length=30)
    class Meta:
        db_table="women_table"

class infant_table(models.Model):
    inf_id= models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    phone= models.CharField(max_length=30)
    F_name= models.CharField(max_length=30)
    M_name= models.CharField(max_length=30)
    class Meta:
        db_table="infant_table"

class article_table(models.Model):
    arti_id= models.CharField(primary_key=True, max_length=30)
    id_ang = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    photo= models.CharField(max_length=30)
    num_of_items = models.CharField(max_length=30)
    class Meta:
        db_table="article_table" 

class notification_table(models.Model):
    notifi_id= models.CharField(primary_key=True, max_length=30)
    notification=models.CharField(max_length=90)
    not_dt=models.CharField(max_length=90)
    an_id=models.CharField(max_length=90)
    class Meta:

        db_table = "notification_table"

class message_table(models.Model):
    messg_id= models.CharField(primary_key=True, max_length=30)
    subject=models.CharField(max_length=90)
    message=models.CharField(max_length=90)
    messg_dt=models.CharField(max_length=90)
    class Meta:

        db_table = "message_table"

class foodallotment_table(models.Model):
    allot_num= models.CharField(primary_key=True, max_length=30)
    angwadi_id = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    month = models.CharField(max_length=30)
    year= models.CharField(max_length=30)
    allot_dt= models.CharField(max_length=30)
    food_id= models.ForeignKey(foodmaster_table, on_delete=models.CASCADE)
    class Meta:
        db_table="foodallotment_table"

class complaint_table(models.Model):
    cmpl_id=models.CharField(max_length=90)
    complaint=models.CharField(max_length=90)
    comp_dt=models.CharField(max_length=90)
    class Meta:

        db_table = "complaint_table"

      