"""anganawadi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('index/',views.index),
    path('public_view_anganwadi/',views.public_view_anganwadi),
    path('anganwadis_view/<str:angan_id>',views.anganwadis_view),
    path('anganwadi_view_notification_details/<str:angan_id>',views.anganwadi_view_notification_details),
    path('public_view_vaccination/',views.public_view_vaccination),
    path('header/',views.header),
    path('footer/',views.footer),
    path('registration/',views.registration),
    path('add_complaint/',views.add_complaint),
    path('in_complaint/',views.in_complaint),
    ##**********LOGING*************************
    path('loging/',views.loging),
    path('in_loging/',views.in_loging),
    #**********ADMIN****************************
    path('admin1/',views.admin1),
    #**Anganwadi Management**
    path('add_anganwadi/',views.add_anganwadi),
    path('in_anganwadi/',views.in_anganwadi),
    path('anganwadi/',views.anganwadi),
    path('remove_anganwadi/<str:angan_id>',views.remove_anganwadi),
    path('edit_anganwadi/<str:angan_id>',views.edit_anganwadi),
    path('update_anganwadi/<str:angan_id>',views.update_anganwadi),
    #**Food Management**
    path('add_foodmaster/',views.add_foodmaster),
    path('in_foodmaster/',views.in_foodmaster),
    path('remove_foodmaster/<str:food_id>',views.remove_foodmaster),
    path('foodmaster/',views.foodmaster),

    #**staf Management**
    path('add_staf/',views.add_staf),
    path('in_staf/',views.in_staf),
    path('remove_staf/<str:stf_id>',views.remove_staf),
    path('staf/',views.staf),
    path('edit_staf/<str:stf_id>',views.edit_staf),
    path('update_staf/<str:stf_id>',views.update_staf),
     #**Vccine Management**
    path('add_vaccination/',views.add_vaccination),
    path('in_vaccination/',views.in_vaccination),
    path('remove_vaccination/<str:vac_id>',views.remove_vaccination),
    path('vaccination/',views.vaccination),
    
    #Report*********
    path('ad_infant/',views.ad_infant),
    path('ad_student/',views.ad_student),
    path('ad_anganwadi/',views.ad_anganwadi),

    #View********
    path('view_complaint/',views.view_complaint),
    path('view_article/',views.view_article),
    path('view_notification/',views.view_notification),
    #****HOMEPAGES******************************************************

    #Anganwadi***************************************
    #*************************************************

    path('homepage_anganwadi/',views.homepage_anganwadi),
    #******Student Management******
    path('add_student/',views.add_student),
    path('in_student/',views.in_student),
    path('remove_student/<str:stud_id>',views.remove_student),
    path('student/',views.student),
    path('update_student/<str:stud_id>',views.update_student),
    
    #******Women Management******
    path('add_women/',views.add_women),
    path('in_women/',views.in_women),
    path('remove_women/<str:women_id>',views.remove_women),
    path('women/',views.women),
    #******Infant Management******
    path('add_infant/',views.add_infant),
    path('in_infant/',views.in_infant),
    path('remove_infant/<str:inf_id>',views.remove_infant),
    path('infant/',views.infant),
    #******Article Management******
    path('add_article/',views.add_article),
    path('in_article/',views.in_article),
    path('remove_article/<str:arti_id>',views.remove_article),
    path('article/',views.article),
    #******Notification  Management******
    path('add_notification/',views.add_notification),
    path('in_notification/',views.in_notification),
    path('remove_notification/<str:notifi_id>',views.remove_notification),
    path('notification/',views.notification),
    
     #******Foodallotment Management******
    path('add_foodallotment/',views.add_foodallotment),
    path('in_foodallotment/',views.in_foodallotment),
    path('remove_foodallotment/<str:Falo_id>',views.remove_foodallotment),
    path('foodallotment/',views.foodallotment),
    path('angn_view_complaint/',views.angn_view_complaint),
    
#Women***************************************
    #*************************************************
path('homepage_women/',views.homepage_women),
path('women_view_vaccination_details/',views.women_view_vaccination_details),  
path('women_view_notification_details/',views.women_view_notification_details),
path('view_women_foodallotment/',views.view_women_foodallotment),

#Parent/student***************************************
    #*************************************************
path('homepage_parent/',views.homepage_parent),
path('view_parent_foodallotment/',views.view_parent_foodallotment),

#**Logout****
    path('admin_logout/',views.admin_logout),
    path('anganwadi_logout/',views.anganwadi_logout),
    path('women_logout/',views.women_logout),
    
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)    


