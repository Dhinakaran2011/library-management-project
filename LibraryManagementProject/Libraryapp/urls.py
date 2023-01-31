from django.urls import path

from Libraryapp import views


urlpatterns=[
    path('reg',views.reg_fun,name='reg'),
    path('regdata',views.regdata_fun),
    path('reg2',views.regin_fun,name='reg2'),
    path('regdata2',views.regdata2_fun),
    path('',views.login_fun,name='log'),
    path('logdata',views.logdata_fun),
    path('home',views.home_fun,name='home'),
    path('add_books',views.add_fun,name='add'),
    path('readdata',views.readdata_fun),
    path('display',views.dis_fun,name='dis'),
    path('update/<int:id>',views.update_fun,name='up'),
    path('delete/<int:id>',views.delete_fun,name='del'),
    path('assign',views.assign_fun,name='assign'),
    path('assign_data',views.assigndata_fun),
    path('readassign',views.readassign_fun,name='readas'),
    path('display2',views.display2,name='issuebook'),
    path('delete2/<int:id>', views.delete2,name ='dele'),
    path('update2/<int:id>',views.update2,name='upd'),
    path('sissue',views.sissue_fun,name='sissue'),
    path('ahome',views.admin_fun,name='ahome'),
    path('shome',views.stud_fun,name='shome'),
    path('pro',views.profile_fun,name='pro'),
    path('prof',views.profupdate_fun,name='prof'),
    path('updatepro',views.updaetpro_fun)


]