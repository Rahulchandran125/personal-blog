from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
#<-------post shuffled--------->
from django.db.models.functions import Random
from django.core.cache import cache
import random
#  --- end------>.

# <------searchfun-------->
from django.db.models import Q
# from django.core.paginator import Paginator
# <------end------->
from.models import Post,Category,ViewPost1,Like,Image
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required




from django.contrib import messages

from.forms import ProfileForm,ViweForm,UserForm,CategoryForm

# Create your views here.


def indexfun(request):
   return render(request,'index.html') 

@login_required
def  post_view(request):
    h=ViewPost1.objects.order_by(Random())[:4]  # Get the latest 5 posts 
    photo=Post.objects.order_by(Random())[:3]

   #  <---gallery---->
    pic=ViewPost1.objects.order_by(Random())[:1]
    img=ViewPost1.objects.order_by(Random())[:1]
    prof=ViewPost1.objects.order_by(Random())[:1]
    image=ViewPost1.objects.order_by(Random())[:2]
    #<-----end----->

    y=Category.objects.all() 
    z=ViewPost1.objects.filter(us=request.user.id) 
    b=ViewPost1.objects.order_by(Random())[:6]
   #  shuffled_posts = cache.get('shuffled_posts')

   #  if not shuffle d_posts:
   #    b = list(ViewPost1.objects.all())[:6]
   #    random.shuffle(b)
   #    cache.set('shuffled_posts', b, timeout=10) 
    return render(request,'blog.html',{"new":b,"cat":y,'old':z,'front':h,'photo':photo,'pic':pic,'img':img,'prof':prof,'image':image})

  


def Dashboardfun(request):
   y=Category.objects.all()
   return render(request,'Dashboard.html',{"cat":y})
  


 
@login_required
def managepostfun(request):
    v=ViewPost1.objects.filter(us=request.user)
    
    return render(request,'manage-post.html', {'view':v}) 
  

def addcategoryfun(request):
   return render(request,'add-category.html') 

# LOGIN REGISTER

def registerfun(request):

    if request.method=='POST':
      username=request.POST['uname']
      email=request.POST['email']
      pw1=request.POST['pass1']
      pw2=request.POST ['pass2']
      
      if pw1==pw2:
      
      
         if User.objects.filter(username=username).exists():
             messages.error(request,"Oops! Invalid username.")
             return render(request,'register.html')
         
         elif User.objects.filter(email=email).exists():
            messages.error(request,"Invalid email address.")
            return render(request,'register.html')


         elif User.objects.filter(password=pw1).exists():
           
            return render(request,'register.html')  


         else:
            User.objects.create_user(username=username,email=email,password=pw1)
            # return render(request,'register.html')
            messages.success(request, 'Your Register has been updated successfully!') 
            return redirect('/login')
   
      else:
         messages.error(request,"Invalid password.")
         return render(request,'register.html')


    else:
      return render(request,'register.html')




def loginfun(request):
   if request.method=='POST':
      uname=request.POST['uname']
      pw1=request.POST['pass1']
          
      z=auth.authenticate(username=uname,password=pw1)
  
      if z:
         auth.login(request,z)
         return redirect('/blog')
      else:
         messages.error(request,"invalid user or password")
         return render(request,'login.html')
             
   else: 
      return render(request,'login.html') 

def logoutfun(request):
   auth.logout(request)
   return redirect('/login')    
 
   # END

   
# Category

def categoryfun(request,c_id):
   h=ViewPost1.objects.filter(cate=c_id) 
   return render(request,'category.html',{'ab':h,}) 

@login_required
def addcategoryfun(request):
   if request.method=='POST':
      f=CategoryForm(request.POST,request.FILES)
      if f.is_valid():
         x=f.save(commit=False)
         x.us=request.user
        
         x.save()
         return redirect('/Dashboard')
   else:   
      f=CategoryForm()
      return render(request,'add-category.html',{'category':f,'x':'Add Category'})

@login_required  
def editcategoryfun(request,c_id):
  if request.method=='POST':
     x=Category.objects.get(id=c_id)
     f=CategoryForm(request.POST,request.FILES,instance=x)
     if f.is_valid():
          a=f.save(commit=False)
          a.us=request.user
        
          a.save()
          return redirect('/Dashboard')  
  else: 
      x=Category.objects.get(id=c_id)
      f=CategoryForm(instance=x)
      return render(request,'add-category.html',{'category':f,'x':'Edit Category'})
  


def deletecategoryfun(request,c_id):
     x=Category.objects.get(id=c_id)
     x.delete()
     return redirect('/Dashboard')

#  END
 
def aboutfun(request):
   return render(request,'about.html') 
def gellaryfun(request):
   gallery=Image.objects.all()
   return render(request,'gellary.html',{'gallery':gallery}) 

   # POST
   
def postfun(request):
    v=ViewPost1.objects.all()
    return render(request,'post.html', {'view':v}) 

@login_required
def addpostfun(request):
  if request.method=='POST':
      f=ViweForm(request.POST,request.FILES)
      if f.is_valid():
         x=f.save(commit=False)
         x.us=request.user
         x.save()
         return redirect('/manage-post')
  else:
      f=ViweForm()
      return render(request,'addpost.html',{'data':f,'x':'Add Post'})

@login_required  
def editpostfun(request,e_id):
  if request.method=='POST':
     x=ViewPost1.objects.get(id=e_id)
     f=ViweForm(request.POST,request.FILES,instance=x)
     if f.is_valid():
          a=f.save(commit=False)
          a.us=request.user
        
          a.save()
          return redirect('/profile')  
  else: 
      x=ViewPost1.objects.get(id=e_id)
      f=ViweForm(instance=x)
      return render(request,'addpost.html',{'data':f,'x':'Edit Post'})
  
def deletepostfun(request,e_id):
     x=ViewPost1.objects.get(id=e_id)
     x.delete()
     return redirect('/profile')

# END POST
@login_required
def addprofilefun(request):  
   if request.method == 'POST':
      p = ProfileForm(request.POST, request.FILES)
      if p.is_valid():
         x=p.save(commit=False)
         x.user=request.user
         x.save()
         return redirect('/profile')
   else:
      p = ProfileForm()

      return render(request,'addprofile.html', {'image': p})
   
@login_required
def profilefun(request):

   d=ViewPost1.objects.filter(us=request.user.id) 
   count = ViewPost1.objects.filter(us=request.user).count() 
   return render(request,'profile.html',{'post':d,'count':count})  



@login_required
def editprofilefun(request):
   if request.method=='POST':
      uform = UserForm(request.POST, instance=request.user)
      pform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
      if uform.is_valid() and pform.is_valid():
         uform.save()
         pform.save()
         messages.success(request, 'Your profile has been updated successfully!')
         return redirect('/profile')
   else:
      uform = UserForm(instance=request.user)
      pform = ProfileForm(instance=request.user.profile)

   return render(request, 'editprofile.html',{'uform':uform,'pform':pform})


def searchfun(request):
     a= request.GET['ab']
     y=Category.objects.all() 
    
     c = ViewPost1.objects.filter(Q(title__icontains=a) | Q(content__icontains=a))
     count = ViewPost1.objects.filter(Q(title__icontains=a) | Q(content__icontains=a)).count()
     return render(request,'search.html',{'search':c,'cat':y,'count':count})



def userprofilefun(request,u_id):
   
   y=User.objects.get(id=u_id) 
   d=ViewPost1.objects.filter(us=u_id) 
   count = ViewPost1.objects.filter(us=u_id).count() 
   
 
   return render(request,'userprofile.html',{'post':d,'count':count,'u':y})  

   
def privacyfun(request):
  
   return render(request,'privacy.html')







# @login_required
# def like_post(request, post_id):
#     post = get_object_or_404(ViewPost1, id=post_id)
#     if request.user in post.liked.all():
#         post.liked.remove(request.user)
#     else:
#         post.liked.add(request.user)
#     return redirect('/blog', post_id=post_id)



@login_required
def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = get_object_or_404(ViewPost1, id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
            Like.objects.filter(user=user, post_id=post_id).delete()
        else:
            post_obj.liked.add(user)
            like, created = Like.objects.get_or_create(user=user, post_id=post_id)
            if not created:
                if like.value == 'Like':
                    like.value = 'Unlike'
                else:
                    like.value = 'Like'
                like.save()

    return redirect(reverse('home:post-list'))

