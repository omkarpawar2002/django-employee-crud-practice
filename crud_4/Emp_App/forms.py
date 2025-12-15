from django import forms
from .models import Employee

gender_choices = [
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHER','OTHER')
]

dept_choices = [
    ('DEVELOPER','DEVELOPER'),
    ('ADMIN','ADMIN'),
    ('HR','HR'),
    ('SALES','SALES'),
    ('OPERATION','OPERATION'),
    ('MANAGEMENT','MANAGEMENT'),
    ('FINANCE','FINANCE')
]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'emp_id':'EMPLOYEE ID',
            'first_name':'FIRST NAME',
            'last_name':'LAST NAME',
            'gender':'GENDER',
            'mobile':'MOBILE NO',
            'dob':'DATE OF BIRTH',
            'city':'CITY',
            'address':'ADDRESS',
            'dept':'DEPARTMENT',
            'sal':'SALARY',
            'email':'EMAIL ID',
            'password':'PASSWORD',
            'eligible':'ELIGIBILITY'
        }
        widgets = {
            'emp_id':forms.NumberInput(attrs={
                'placeholder':'E.g.,101',
            }),
            'first_name':forms.TextInput(attrs={
                'placeholder':'Enter First Name',
            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'Enter Last Name',
            }),
            'gender':forms.RadioSelect(choices=gender_choices),
            'mobile':forms.TextInput(attrs={
                'placeholder':'+91 **********',
            }),
            'dob':forms.DateInput(attrs={
                'type':'date',
            }),
            'city':forms.TextInput(attrs={
                'placeholder':'E.g., Mumbai',
            }),
            'address':forms.Textarea(attrs={
                'placeholder':'E.g., Mumbai , Maharashtra',
                'rows':'2',
            }),
            'dept':forms.Select(choices=dept_choices),
            'email':forms.EmailInput(attrs={
                'placeholder':'youremail@gmail.com',
            }),
            'password':forms.PasswordInput(attrs={
                'type':'password',
            })            
            }
