from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):#By inheriting from UserCreationForm, this custom form automatically includes fields for username, password, and password confirmation.
    email = forms.EmailField(required=True)#This adds an additional field called email to the form, which is an email input field. The required=True parameter indicates that this field is mandatory for form submission.
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('first_name','last_name','email','password1','password2')#we also need a username attribute that is mendatory, but we don't have a username. In our case, our username is going to be the email address

    def save(self,commit=True):#This method is responsible for saving the form data to the database.
        user = super(RegisterForm,self).save(commit=False) #Here, we call the save() method of the parent class (UserCreationForm) using super(). This creates a new user instance but doesn't save it to the database yet (commit=False).
        user.email = self.cleaned_data['email'] #The cleaned_data attribute contains the validated form input.
        user.username = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user


