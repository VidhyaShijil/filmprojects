
from django.shortcuts import render, redirect
from django.http import HttpResponse
from  .models import Addmovie
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import AddmovieForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from .models import Review
from .forms import ReviewForm
from django.urls import reverse


def index(request):
    addmovie=Addmovie.objects.all()
    context={
        'Addmovie_list':addmovie
    }
    return  render(request,'index.html',context)

@login_required
def addedmoviesbyuser(request):
    user_id = request.session.get('user_id')
    if user_id:
        
        # Fetch data from the table based on the user ID
        Addmovies = Addmovie.objects.filter(userid=user_id)
        context={
            'Addmovie_list':Addmovies
        }
        return  render(request,'addedmoviesbyuser.html',context)
        
    return  render(request,'addedmoviesbyuser.html')

def detail(request,getmovie_id):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            getmovie = Addmovie.objects.get(id=getmovie_id, userid=6)
            return render(request,"addedmoviebyuserdetail.html",{'getmovie':getmovie})
        except Addmovie.DoesNotExist:
            getmovie = Addmovie.objects.get(id=getmovie_id)
            reviews = Review.objects.filter(movieid=getmovie_id)
            context={
            'getmovie':getmovie,
            'reviews':reviews
            }
            return render(request,"detail.html",context)
        
    getmovie=Addmovie.objects.get(id=getmovie_id)
    reviews = Review.objects.filter(movieid=getmovie_id)
    context={
            'getmovie':getmovie,
            'reviews':reviews
    }
    return render(request,"detail.html",context)

def addmovie(request):
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
        addmovie=Addmovie(name=name,desc=desc,year=year,actor=actor,date=r_date,link=link,category=category,img=img,userid=userid)
        addmovie.save()
        return redirect('/')
    if request.user.is_authenticated:
            return render(request, 'add.html')
    else:
        return redirect( 'login')
            
   

@login_required
def update(request,id):
    Addmovies=Addmovie.objects.get(id=id)
    form=AddmovieForm(request.POST or None,request.FILES,instance=Addmovies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'Addmovie':Addmovies})

@login_required
def delete(request,id):
    if request.method=='POST':
        Addmovies=Addmovie.objects.get(id=id)
        Addmovies.delete()
        return redirect('/')
    else:
        return render(request, 'delete.html')
       
def detailbycategory(request, category):

    catmovie= Addmovie.objects.filter(category=category)
    context={
        'Addmovie_list':catmovie
    }
    return  render(request,'index.html',context)

def search_results(request):
    query = request.GET.get('query')
    catmovie = Addmovie.objects.filter(
        Q(category__icontains=query) |  # Filter by category containing the query
        Q(name__icontains=query) |      # Filter by name containing the query
        Q(actor__icontains=query)       # Filter by actor containing the query
    )
    context={
        'Addmovie_list':catmovie
    }  # Example query, adjust as needed
    return  render(request,'index.html',context)


def post_review(request,id):
     if request.method=="POST":
        stars=request.POST.get('stars',)
        desc = request.POST.get('description',)
        review=Review(stars=stars,description=desc,movieid=id)
        review.save()
        return redirect('/')
        
    
        
    