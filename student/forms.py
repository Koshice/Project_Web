from django import forms
from .models import Student, Result


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = "__all__"

        widgets = {
            "student_code": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter student_code...",
                    "id": "student_code",
                },
            ),
            "name": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter last name...",
                    "id": "name",
                },
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter address...",
                    "id": "address",
                },
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter email...",
                    "id": "email",
                },
            ),
            "dob": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter date of birth...",
                    "id": "dob",
                },
            ),
            "course_name": forms.Select(
                attrs={
                    "class": "form-select border-success mt-1 mb-4",
                    "id": "course_name",
                },
            ),
            "classroom_name": forms.Select(
                attrs={
                    "class": "form-select border-success mt-1 mb-4",
                    "id": "classroom_name",
                },
            ),
        }


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result

        fields = "__all__"

        widgets = {
            "student_name": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter name...",
                    "id": "student_name",
                },
            ),
            "mark": forms.Select(
                choices={
                    ('Distinction', 'Distinction'),
                    ('Merit', 'Merit'),
                    ('Pass', 'Pass'),
                }
            ),
            "course_name": forms.Select(
                attrs={
                    "class": "form-select border-success mt-1 mb-4",
                    "id": "course_name",
                },
            ),
            "classroom_name": forms.Select(
                attrs={
                    "class": "form-select border-success mt-1 mb-4",
                    "id": "classroom_name",
                },
            ),
        }
