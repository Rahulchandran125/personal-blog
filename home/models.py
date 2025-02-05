from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Category model 
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Blog Post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    img = models.ImageField(upload_to='profile_picture/', null=True, blank=True)
    us= models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cate=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True) 


    def __str__(self):
        return self.title



class profile(models.Model):
   user=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
   bio = models.TextField(blank=True)
   image=models.ImageField(upload_to='profilepic')
  

   def __str__(self):
     return str(self.user)
   
class ViewPost1(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    imag = models.ImageField(upload_to='profile_picture/', null=True, blank=True)
    us= models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cate=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True) 
    liked = models.ManyToManyField(User, default=None, blank=True,related_name='likes')
   
  

    def __str__(self):
        return self.title
    
    @property
    def num_likes(self):
        return self.liked.all().count()
    

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(ViewPost1, on_delete=models.CASCADE)  # Corrected to ViewPost1
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)

    
class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=255, blank=True, null=True)
 
  
def __str__(self):
    return self.image

   
