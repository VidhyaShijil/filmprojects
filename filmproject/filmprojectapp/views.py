
from django.shortcuts import render, redirect
from django.http import HttpResponse
from  . models import Filmproject
from .forms import FilmprojectForm



def index(request):
    filmproject=Filmproject.objects.all()
    context={
        'filmproject_list':filmproject
    }
    return  render(request,'index.html',context)

def addedmoviesbyuser(request):
    user_id = request.session.get('user_id')
    if user_id:
        # Fetch data from the table based on the user ID
        filmprojects = Filmproject.objects.filter(user_id=user_id)
    context={
        'filmproject_list':filmproject
    }
    return  render(request,'index.html',context)
def detail(request,filmproject_id):
    filmproject=Filmproject.objects.get(id=filmproject_id)
    return render(request,"detail.html",{'filmproject':filmproject})

def add_filmproject(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        actor = request.POST.get('actor',)
        r_date = request.POST.get('date',)
        link = request.POST.get('link',)
        category = request.POST.get('category',)
        img = request.FILES['img']
        user_id = request.session.get('user_id')
        if user_id:
            userid=user_id
        else:
            userid=1 
        filmproject=Filmproject(name=name,desc=desc,year=year,actor=actor,date=r_date,link=link,category=category,img=img,userid=userid)
        filmproject.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    filmproject=Filmproject.objects.get(id=id)
    form=FilmprojectForm(request.POST or None,request.FILES,instance=filmproject)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'filmproject':filmproject})

def delete(request,id):
    if request.method=='POST':
        filmproject=Filmproject.objects.get(id=id)
        filmproject.delete()
        return redirect('/')
    return  render(request,'delete.html')


def registerorlogin(request):
    if request.method=='POST':
        filmproject=Filmproject.objects.get(id=id)
        filmproject.delete()
        return redirect('/')
    return  render(request,'register.html')

