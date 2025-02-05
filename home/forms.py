from django import forms
from django.contrib.auth.models import User
from.models import ViewPost1,profile,Category,Post



class ProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        exclude=['user']

class ViweForm(forms.ModelForm):
    class Meta:
        model=ViewPost1
        exclude=['us'] 

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['us'] 

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['username', 'email']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields ="__all__"

