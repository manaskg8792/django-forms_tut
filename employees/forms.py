from django import forms


class EmployeeForm(forms.Form):
    full_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    address = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    salary = forms.FloatField(label='Employee salary')
    is_married = forms.BooleanField()