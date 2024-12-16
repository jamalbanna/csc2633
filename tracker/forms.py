from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Category
from .models import FinancialEntry
from .models import ExpenseType

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'budget_limit']


class FinancialEntryForm(forms.ModelForm):
    class Meta:
        model = FinancialEntry
        fields = ['title', 'entry_type', 'category', 'value', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  
        }

class ExpenseTypeForm(forms.ModelForm):
    class Meta:
        model = ExpenseType
        fields = ['name']


