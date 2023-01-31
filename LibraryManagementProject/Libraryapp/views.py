from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import request
from django.shortcuts import render, redirect

from Libraryapp.models import Course, Student, Books, Issue_book


# Create your views here.
def reg_fun(request):
    return render(request,'admin register.html',{'data':''})

def regdata_fun(request):
    user_name=request.POST['name']
    user_email=request.POST['email']
    user_pswd=request.POST['pass']

    if User.objects.filter(Q(username=user_name)|Q(email=user_email)).exists():
        return render(request,'admin register.html',{'data':'username,email and password are already exists'})
    else:
        u1=User.objects.create_superuser(username=user_name,email=user_email,password=user_pswd)
        u1.save()
        return redirect('log')



def regin_fun(request):
    c1=Course.objects.all()
    return render(request,'studentregister.html',{'data':c1,'d':''})

def regdata2_fun(request):
    stud_name = request.POST['name']
    stud_phno = request.POST['phnum']
    if Student.objects.filter(Q(Student_Name=stud_name) | Q(Student_Phno=stud_phno)).exists():
        return render(request,'studentregister.html',{'data':'','d':'the details are already exist..'})
    else:
        s=Student()
        s.Student_Name = request.POST['name']
        s.Student_Phno = request.POST['phnum']
        s.Student_Sem = request.POST['semester']
        s.Student_Pswd = request.POST['pass']
        s.Student_Course = Course.objects.get(Course_Name=request.POST['course'])
        s.save()
    return redirect('log')


def login_fun(request):
    return render(request,'login.html')

def logdata_fun(request):
    user_name=request.POST["txtuser"]
    user_pswd=request.POST['txtpass']
    user1 = authenticate(username=user_name, password=user_pswd)

    if user1 is not None:
        if user1.is_superuser:
            return render(request,'adminhome.html')
        else:
            return render(request,'login.html',{'data':''})
    elif Student.objects.filter(Q(Student_Name=user_name)& Q(Student_Pswd=user_pswd)).exists():
        request.session['n']=user_name
        return render(request,'studenthome.html',{'data':user_name})
    else:
        return render(request,'login.html',{'data':'username and password is wrong'})

def home_fun():
    return redirect('home')

def add_fun(request):
    c1 = Course.objects.all()
    return render(request,'addbooks.html',{'data': c1})

def readdata_fun(request):
    b1 = Books()
    b1.Book_Name=request.POST["bookname"]
    b1.Author_Name=request.POST["authorname"]
    b1.Course_id = Course.objects.get(Course_Name=request.POST["ddlcrc"])
    b1.save()
    return redirect('add')

def dis_fun(request):
    b1= Books.objects.all()
    return render(request,'displaybooks.html',{'data':b1})


def update_fun(request,id):
    b1=Books.objects.get(id=id)
    c1=Course.objects.all()
    if request.method=='POST':
        b1.Book_Name=request.POST['book_name']
        b1.Author_Name=request.POST['author_name']
        b1.Course_id= Course.objects.get(Course_Name=request.POST["course"])
        b1.save()
        return redirect('dis')
    else:
        return render(request,'update.html',{'data':c1,'d':b1})


def delete_fun(request,id):
    b1=Books.objects.get(id=id)
    b1.delete()
    return redirect('dis')


def assign_fun(request):
    c=Course.objects.all()
    return render(request,'assignbooks.html',{'data1':c})


def assigndata_fun(request):
    c1=Course.objects.all()
    s1=Student.objects.filter(Q(Student_Sem=request.POST['sem']) & Q(Student_Course=Course.objects.get(Course_Name=request.POST['course'])))
    b1=Books.objects.filter(Course_id=Course.objects.get(Course_Name=request.POST['course']))
    return render(request,'assignbooks.html',{'data':s1,'d':b1,'d1':'','data1':c1})


def readassign_fun(request):
    i=Issue_book()
    i.Stud_Name=Student.objects.get(Student_Name=request.POST['student'])
    i.Book_Name=Books.objects.get(Book_Name=request.POST['book'])
    i.Start_Date=request.POST['sdate']
    i.End_Date=request.POST['edate']
    i.save()
    return redirect('assign')


def display2(request):
    i=Issue_book.objects.all()
    return render(request,'displayissues.html',{'data':i})


def update2(request,id):
    i=Issue_book.objects.get(id=id)
    s=Student.objects.all()
    b=Books.objects.all()
    if request.method=='POST':
        i.Stud_Name=Student.objects.get(Student_Name=request.POST['sname'])
        i.Book_Name=Books.objects.get(Book_Name=request.POST['bname'])
        i.Start_Date=request.POST['sdate']
        i.End_Date=request.POST['edate']
        i.save()
        return redirect('issuebook')
    return render(request,'issuedupdate.html',{'data':i,'s':s,'b':b})


def delete2(request,id):
    i=Issue_book.objects.get(id=id)
    i.delete()
    return redirect('issuebook')


def sissue_fun(request):
    v=Issue_book.objects.filter(Stud_Name=Student.objects.get(Student_Name=request.session['n']))
    return render(request,'stuissuedbook.html',{'data':v})
def admin_fun(request):
    return render(request,'adminhome.html')


def stud_fun(request):
    return render(request,'studenthome.html',{'data':request.session['n']})


def profile_fun(request):
    s = Student.objects.get(Student_Name=request.session['n'])
    return render(request, 'profile.html', {'data':s})


def profupdate_fun(request):
    k=Student.objects.get(Student_Name=request.session['n'])
    return render(request,'profileupdate.html',{'data':k})

def updaetpro_fun(request):
    v = Student.objects.get(Student_Name=request.session['n'])
    v.Student_Name=request.POST['name']
    v.Student_Phno = request.POST['phno']
    v.Student_Pswd = request.POST['pass']
    v.Student_Sem = request.POST['sem']
    v.save()
    return redirect('pro')