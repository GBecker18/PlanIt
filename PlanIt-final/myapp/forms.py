from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import Shift, Employee
from django.forms import TimeInput


# create user


class CreateUserForm(UserCreationForm):
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone = forms.CharField(validators=[phone_regex], max_length=11)

    class Meta:
        model = Employee

        fields = ["username", "email", "phone"]


# authenticating a user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())

    password = forms.CharField(widget=PasswordInput())

    class Meta:
        model = Employee


class ShiftAssignmentForm(forms.ModelForm):
    employee = forms.ModelChoiceField(
        label="Employee",
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        to_field_name="userID",  # Set the field to use for display and value
        empty_label="Select an employee",
    )

    class Meta:
        model = Shift
        fields = ["employee", "start_time", "end_time", "date"]
        widgets = {
            "employee": forms.TimeInput(
                attrs={"type": "time", "class": "form-control"}
            ),
            "start_time": forms.TimeInput(
                attrs={"type": "time", "class": "form-control"}
            ),
            "end_time": forms.TimeInput(
                attrs={"type": "time", "class": "form-control"}
            ),
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }

    def save(self, commit=True):
        shift = super().save(commit=False)
        if commit:
            shift.save()
        return shift


class UpdateUserForm(forms.ModelForm):
    password = None

    class Meta:
        model = Employee
        fields = [
            "username",
            "email",
        ]
        exclude = [
            "password1",
            "password2",
        ]
