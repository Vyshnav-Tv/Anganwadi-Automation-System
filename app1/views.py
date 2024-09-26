from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from app1 import views
from django.core.files.storage import FileSystemStorage
from app1.models import id_gen,anganwadi_table,foodmaster_table,login_table,staf_table,student_table,women_table,infant_table,vaccine_table,article_table,notification_table,message_table,foodallotment_table,complaint_table
from django.conf import settings

# Create your views here.
def index(request):
    d=notification_table.objects.all().order_by('-not_dt')
    return render(request,'index.html',{'d':d})
def public_view_anganwadi(request):
    data=anganwadi_table.objects.all()
    return render(request,'public_view_anganwadi.html',{'data':data})    
def anganwadis_view(request,angan_id):
    data=anganwadi_table.objects.filter(angan_id=angan_id)
    return render(request,'anganwadis_view.html',{'data':data})
def anganwadi_view_notification_details(request,angan_id):
    data=anganwadi_table.objects.filter(angan_id=angan_id)
    da=notification_table.objects.filter(an_id=angan_id)
    return render(request,'anganwadi_view_notification_details.html',{'da':da, 'data':data})
def public_view_vaccination(request):
    data=vaccine_table.objects.all()
    return render(request,'public_view_vaccination.html',{'data':data})
def header(request):
    return render(request,'Header.html')

def footer(request):
    return render(request,'Footer.html')    
def registration(request):
    return render(request,'Registration.html')   
def add_complaint(request):
    x=id_gen.objects.get(id=1)
    id=x.compl_id
    id=int(id+1)
    comp="complaint_" + str(id)
    request.session['comp'] = id
    return render(request,'add_complaint.html',{'comp':comp}) 
def in_complaint(request):
    data1 = id_gen.objects.get(id=1)
    data1.compl_id= request.session['comp']
    data1.save() 
    if request.method == 'POST':
        data=complaint_table()
        data.cmpl_id=request.POST.get('i1')
        data.complaint=request.POST.get('i2')
        data.comp_dt=request.POST.get('i3')
        data.save()
        return render(request,'index.html')
        

#LOGING************************************************************************

def loging(request):    
    return render(request,'loging.html')  

def in_loging(request):
    if request.method=='POST':
        log=login_table.objects.all()
        un=request.POST.get('username')
        pw=request.POST.get('password')
        flag=0
        for da in log:
            if un==da.username and pw==da.password:
                typ=da.category
                print(typ)
                flag=1
                if typ=="admin":
                    request.session['admin']=un
                    return redirect('/admin1')
                elif typ=="anganwadi":
                    request.session['anganwadi']=un
                    return redirect('/homepage_anganwadi')
                elif typ=="preg_women":
                    request.session['women']=un
                    return redirect('/homepage_women') 
                elif typ=="parent":
                    request.session['stud']=un
                    return redirect('/homepage_parent')                     
#**************ADMIN PAGE******************************
def admin1(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        return render(request,'admin1.html')
    #**Anganwadi Management***
def add_anganwadi(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        x=id_gen.objects.get(id=1)
        id=x.anganwadi_id
        id=int(id+1)
        angan="ANGANWADI_" + str(id)
        request.session['angan'] = id
        return render(request,'add_anganwadi.html',{'angan':angan})  
def in_anganwadi(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        data1 = id_gen.objects.get(id=1)
        data1.anganwadi_id= request.session['angan']
        data1.save() 
        if request.method == 'POST':
            data=anganwadi_table()
            data.angan_id=request.POST.get('i1')
            data.name=request.POST.get('i2')
            data.dist=request.POST.get('i3')
            data.location=request.POST.get('i4')
            data.build_num=request.POST.get('i5')
            data.owner_name=request.POST.get('i6')
            data.phone=request.POST.get('i7')
            data.email=request.POST.get('i8')
            data.status=request.POST.get('i9')
            data.save()

            data2=login_table()
            data2.username=data.angan_id
            data2.password=data.phone
            data2.category="anganwadi"
            data2.save()

            return render(request,'admin1.html')
        
def anganwadi(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        data=anganwadi_table.objects.all()    
        return render(request,'anganwadi.html',{'data':data})
def remove_anganwadi(request,angan_id):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        data=anganwadi_table.objects.get(angan_id=angan_id)
        data.delete()
        return redirect('/anganwadi')
def edit_anganwadi(request,angan_id):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        data=anganwadi_table.objects.get(angan_id=angan_id)
        return render(request,'edit_anganwadi.html',{'data':data})
def update_anganwadi(request,angan_id):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        data=anganwadi_table.objects.get(angan_id=angan_id)
        if request.method == 'POST':
            data.name=request.POST.get('i2')
            data.dist=request.POST.get('i3')
            data.location=request.POST.get('i4')
            data.build_num=request.POST.get('i5')
            data.owner_name=request.POST.get('i6')
            data.phone=request.POST.get('i7')
            data.save() 
            return redirect('/anganwadi')

            data2=login_table(stud_id=stud_id)
            data2.password=data.phone
            data2.save()
    #**Food Management***
def add_foodmaster(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        x=id_gen.objects.get(id=1)
        id=x.foodM_id
        id=int(id+1)
        food="F-MASTER_" + str(id)
        request.session['food'] = id
        return render(request,'add_foodmaster.html',{'food':food})  
def in_foodmaster(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        data1 = id_gen.objects.get(id=1)
        data1.foodM_id= request.session['food']
        data1.save() 
        if request.method == 'POST':
            data=foodmaster_table()
            data.food_id=request.POST.get('i1')
            data.item_name=request.POST.get('i2')
            data.qty=request.POST.get('i3')
            data.category=request.POST.get('i4')
            data.discription=request.POST.get('i5')
            data.save()
            return render(request,'admin1.html')
        
def foodmaster(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        data=foodmaster_table.objects.all()    
        return render(request,'foodmaster.html',{'data':data})
def remove_foodmaster(request,food_id):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        data=foodmaster_table.objects.get(food_id=food_id)
        data.delete()
        return redirect('/foodmaster')    

    #**Vaccine Management***
def add_vaccination(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        x=id_gen.objects.get(id=1)
        id=x.vaccine_id
        id=int(id+1)
        v="VACC_" + str(id)
        request.session['v'] = id
        return render(request,'add_vaccination.html',{'v':v})  
def in_vaccination(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        data1 = id_gen.objects.get(id=1)
        data1.vaccine_id= request.session['v']
        data1.save() 
        if request.method == 'POST':
            data=vaccine_table()
            data.vac_id=request.POST.get('i1')
            data.name=request.POST.get('i2')
            data.category=request.POST.get('i3')
            data.discription=request.POST.get('i4')
            data.save()
            return render(request,'admin1.html')
        
def vaccination(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        data=vaccine_table.objects.all()    
        return render(request,'vaccination.html',{'data':data})
def remove_vaccination(request,vac_id):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        data=vaccine_table.objects.get(vac_id=vac_id)
        data.delete()
        return redirect('/vaccination')    

 
    #**staf Management***
def add_staf(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        x=id_gen.objects.get(id=1)
        id=x.staf_id
        id=int(id+1)
        staf="STAF_" + str(id)
        request.session['staf'] = id
        data=anganwadi_table.objects.values('angan_id').distinct()
        return render(request,'add_staf.html',{'staf':staf, 'data':data})  
def in_staf(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        data1 = id_gen.objects.get(id=1)
        data1.staf_id= request.session['staf']
        data1.save() 
        if request.method == 'POST':
            photo=request.FILES['photo']
            fs=FileSystemStorage()
            filename=fs.save(photo.name,photo)
            uploaded_file_url=fs.url(filename)
            data=staf_table()
            data.photo=uploaded_file_url
            data.stf_id=request.POST.get('i1')
            data.staf_name=request.POST.get('i2')
            data.id_angan=request.POST.get('i3')
            data.category=request.POST.get('i4')
            data.phone=request.POST.get('i5')
            data.address=request.POST.get('i6')
            data.dob=request.POST.get('i7')
            data.status=request.POST.get('i8')
            data.save()
            return render(request,'admin1.html')
        
def staf(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        data=staf_table.objects.all()    
        return render(request,'staf.html',{'data':data})
def edit_staf(request,stf_id):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        data=staf_table.objects.get(stf_id=stf_id)
        return render(request,'edit_staf.html',{'data':data})        
def remove_staf(request,stf_id):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        data=staf_table.objects.get(stf_id=stf_id)
        data.delete()
        return redirect('/staf')  

def update_staf(request,stf_id):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        data=staf_table.objects.get(stf_id=stf_id)
        if request.method == 'POST':
            
            data.category=request.POST.get('i4')
            data.phone=request.POST.get('i5')
            data.address=request.POST.get('i6')
            data.save()
            return redirect('/staf')

           
    #Report******
def ad_anganwadi(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        ad=anganwadi_table.objects.all()
        return render(request,'ad_anganwadi.html',{'ad':ad})
def ad_infant(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        ad=infant_table.objects.all()
        return render(request,'ad_infant.html',{'ad':ad})    
def ad_student(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        ad=student_table.objects.all()
        return render(request,'ad_student.html',{'ad':ad})            
#View*******
def view_complaint(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        ad=complaint_table.objects.all()
        return render(request,'view_complaint.html',{'ad':ad})
def view_article(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        ad=article_table.objects.all()
        return render(request,'view_article.html',{'ad':ad})    
def view_notification(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        ad=notification_table.objects.all()
        return render(request,'view_notification.html',{'ad':ad})       
    
#*HOME PAGES*******************************************************************************************


#**********ANGANWADI**************************

def homepage_anganwadi(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        return render(request,'homepage_anganwadi.html')

    #**Students Management***
def add_student(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        x=id_gen.objects.get(id=1)
        id=x.student_id
        id=int(id+1)
        stud="STUD_" + str(id)
        request.session['stud'] = id
        data=anganwadi_table.objects.values('angan_id').distinct()
        return render(request,'add_student.html',{'stud':stud, 'data':data})  
def in_student(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data1 = id_gen.objects.get(id=1)
        data1.student_id= request.session['stud']
        data1.save() 
        if request.method == 'POST':
            data=student_table()
            data.stud_id=request.POST.get('i1')
            data.anganw_id=request.POST.get('i2')
            data.stud_name=request.POST.get('i3')
            data.gender=request.POST.get('i4')
            data.dob=request.POST.get('i5')
            data.age=request.POST.get('i6')
            data.save()

            data2=login_table()
            data2.username=data.stud_id
            data2.password=data.dob
            data2.category="parent"
            data2.save()

            return render(request,'homepage_anganwadi.html')
        
def student(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data=student_table.objects.all()    
        return render(request,'student.html',{'data':data})
def remove_student(request,stud_id):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data=student_table.objects.get(stud_id=stud_id)
        data.delete()
        return redirect('/student')
def edit_student(request,stud_id):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data=student_table.objects.get(stud_id=stud_id)
        return render(request,'edit_student.html',{'data':data})
def update_student(request,angan_id):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data=student_table.objects.get(stud_id=stud_id)
        if request.method == 'POST':
            data.stud_name=request.POST.get('i3')
            data.age=request.POST.get('i6')
            data.save() 
            return redirect('/student')

    #**Womens Management***

def add_women(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        x=id_gen.objects.get(id=1)
        id=x.prg_women_id
        id=int(id+1)
        w="WOMEN_" + str(id)
        request.session['w'] = id
        data=anganwadi_table.objects.values('angan_id').distinct()
        return render(request,'add_women.html',{'w':w, 'data':data})  
def in_women(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data1 = id_gen.objects.get(id=1)
        data1.prg_women_id= request.session['w']
        data1.save() 
        if request.method == 'POST':
            data=women_table()
            data.women_id=request.POST.get('i1')
            data.agn_id=request.POST.get('i2')
            data.name=request.POST.get('i3')
            data.address=request.POST.get('i4')
            data.d_date=request.POST.get('i5')
            data.status=request.POST.get('i6')
            data.phone=request.POST.get('i8')
            data.save()

            data2=login_table()
            data2.username=data.women_id
            data2.password=data.phone
            data2.category="preg_women"
            data2.save()

            return render(request,'homepage_anganwadi.html')
        
def women(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data=women_table.objects.all()    
        return render(request,'women.html',{'data':data})
def remove_women(request,women_id):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data=women_table.objects.get(women_id=women_id)
        data.delete()
        return redirect('/women')
            
    #**Infant Management***

def add_infant(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        x=id_gen.objects.get(id=1)
        id=x.infant_id
        id=int(id+1)
        inf="INFANT_" + str(id)
        request.session['inf'] = id
        return render(request,'add_infant.html',{'inf':inf})  
def in_infant(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data1 = id_gen.objects.get(id=1)
        data1.infant_id= request.session['inf']
        data1.save() 
        if request.method == 'POST':
            data=infant_table()
            data.inf_id=request.POST.get('i1')
            data.name=request.POST.get('i2')
            data.address=request.POST.get('i3')
            data.gender=request.POST.get('i4')
            data.dob=request.POST.get('i5')
            data.phone=request.POST.get('i6')
            data.F_name=request.POST.get('i7')
            data.M_name=request.POST.get('i8')
            data.save()

            data2=login_table()
            data2.username=data.inf_id
            data2.password=data.phone
            data2.category="infant"
            data2.save()

            return render(request,'homepage_anganwadi.html')
        
def infant(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data=infant_table.objects.all()    
        return render(request,'infant.html',{'data':data})
def remove_infant(request,inf_id):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data=infant_table.objects.get(inf_id=inf_id)
        data.delete()
        return redirect('/infant')

    #**Article Management***

def add_article(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        x=id_gen.objects.get(id=1)
        id=x.art_id
        id=int(id+1)
        art="article_" + str(id)
        request.session['art'] = id
        data=anganwadi_table.objects.values('angan_id').distinct()
        return render(request,'add_article.html',{'art':art, 'data':data})  
def in_article(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data1 = id_gen.objects.get(id=1)
        data1.art_id= request.session['art']
        data1.save() 
        if request.method == 'POST':
            photo=request.FILES['photo']
            fs=FileSystemStorage()
            filename=fs.save(photo.name,photo)
            uploaded_file_url=fs.url(filename)
            data=article_table()
            data.photo=uploaded_file_url
            data.arti_id=request.POST.get('i1')
            data.id_ang=request.POST.get('i2')
            data.name=request.POST.get('i3')
            data.num_of_items=request.POST.get('i4') 
            data.save()
            return render(request,'homepage_anganwadi.html')
        
def article(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data=article_table.objects.all()    
        return render(request,'article.html',{'data':data})
def remove_article(request,arti_id):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data=article_table.objects.get(arti_id=arti_id)
        data.delete()
        return redirect('/article')

    #**Notification Management***

def add_notification(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        x=id_gen.objects.get(id=1)
        id=x.noti_id
        id=int(id+1)
        noti="notification_" + str(id)
        request.session['noti'] = id
        data=anganwadi_table.objects.values('angan_id').distinct()
        return render(request,'add_notification.html',{'noti':noti, 'data':data})  
def in_notification(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data1 = id_gen.objects.get(id=1)
        data1.noti_id= request.session['noti']
        data1.save() 
        if request.method == 'POST':
            data=notification_table()
            data.notifi_id=request.POST.get('i1')
            data.notification=request.POST.get('i2')
            data.not_dt=request.POST.get('i3')
            data.an_id=request.POST.get('i4')  
            data.save()
            return render(request,'homepage_anganwadi.html')
        
def notification(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data=notification_table.objects.all()    
        return render(request,'notification.html',{'data':data})
def remove_notification(request,notifi_id):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data=notification_table.objects.get(notifi_id=notifi_id)
        data.delete()
        return redirect('/notification')                    


  

    #**Foodallotment Management***

def add_foodallotment(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        x=id_gen.objects.get(id=1)
        id=x.allot_id
        id=int(id+1)
        allot="F_ALLOTMENT" + str(id)
        request.session['allot'] = id
        data=foodmaster_table.objects.all() 
        return render(request,'add_foodallotment.html',{'allot':allot, 'data':data})  
def in_foodallotment(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data1 = id_gen.objects.get(id=1)
        data1.allot_id= request.session['allot']
        data1.save() 
        if request.method == 'POST':
            data=foodallotment_table()
            data.allot_num=request.POST.get('i1')
            data.angwadi_id=request.POST.get('i2')
            data.category=request.POST.get('i3')
            data.month=request.POST.get('i4') 
            data.year=request.POST.get('i5') 
            data.allot_dt=request.POST.get('i6') 
            data.food_id_id=request.POST.get('i7') 
            data.save()
            return render(request,'homepage_anganwadi.html')
        
def foodallotment(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data=foodallotment_table.objects.all()    
        return render(request,'foodallotment.html',{'data':data})
def remove_foodallotment(request,allot_num):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data=foodallotment_table.objects.get(allot_num=allot_num)
        data.delete()
        return redirect('/foodallotment ')
def angn_view_complaint(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        data=complaint_table.objects.all()    
        return render(request,'angn_view_complaint.html',{'data':data})

#**********WOMEN**************************

def homepage_women(request):
    if 'women' not in request.session:
        return redirect('/loging')
    else:
        return render(request,'homepage_women.html')

def women_view_vaccination_details(request):
    if 'women' not in request.session:
        return redirect('/loging')
    else:
        
        da=vaccine_table.objects.filter(category='Pregnant Women').values()
        return render(request,'women_view_vaccination_details.html',{'da':da})
        
def women_view_notification_details(request):
    if 'women' not in request.session:
        return redirect('/loging')
    else:
        da=notification_table.objects.all()
        return render(request,'women_view_notification_details.html',{'da':da})
def view_women_foodallotment(request):
    if 'women' not in request.session:
        return redirect('/loging')
    else:
        if request.method == 'POST':
            
            mth=request.POST.get('m')
            yr=request.POST.get('y')
            print(mth)
            daa=foodallotment_table.objects.filter(category='Pregnant Women', month=mth,  year=yr).values()
            return render(request,'view_women_foodallotment.html',{'daa':daa})
        
            


#**********PARENT/STUDENT**************************

def homepage_parent(request):
    if 'stud' not in request.session:
        return redirect('/loging')
    else:
        da=message_table.objects.all()
        data=notification_table.objects.all()
        d=vaccine_table.objects.filter(category='children').values()
        return render(request,'homepage_parent.html',{'da':da, 'data':data, 'd':d})
def view_parent_foodallotment(request):
    if 'stud' not in request.session:
        return redirect('/loging')
    else:
        if request.method == 'POST':
            
            mth=request.POST.get('m')
            yr=request.POST.get('y')
            print(mth)
            daa=foodallotment_table.objects.filter(category='infant', month=mth,  year=yr).values()
            return render(request,'view_parent_foodallotment.html',{'daa':daa})

#LOGOUT**********************************************************

def admin_logout(request):
    if 'admin' not in request.session:
        return redirect('/loging')
    else:
        del request.session['admin']
        return redirect('/index')        

def anganwadi_logout(request):
    if 'anganwadi' not in request.session:
        return redirect('/loging')
    else:
        del request.session['anganwadi']
        return redirect('/index')

def women_logout(request):
    if 'women' not in request.session:
        return redirect('/loging')
    else:
        del request.session['women']
        return redirect('/index')

def women_logout(request):
    if 'stud' not in request.session:
        return redirect('/loging')
    else:
        del request.session['stud']
        return redirect('/index')     