from django import forms
from .models import Category, Course, ClassRoom


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

        fields = "__all__"

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter name...",
                    "id": "name",
                },
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter description...",
                    "id": "description",
                },
            ),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course

        fields = "__all__"

        widgets = {
            "code": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter code...",
                    "id": "code",
                },
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter description...",
                    "id": "description",
                },
            ),
            "name_vi": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter Vietnamese name...",
                    "id": "name_vi",
                },
            ),
            "name_en": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter English name...",
                    "id": "name_en",
                },
            ),
            "credit": forms.NumberInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter credit...",
                    "id": "credit",
                },
            ),
            "hour": forms.NumberInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter hour...",
                    "id": "hour",
                },
            ),
            "category_name": forms.Select(
                attrs={
                    "class": "form-select border-success mt-1 mb-4",
                    "id": "category_name",
                },
            ),
        }


class ClassRoomForm(forms.ModelForm):
    class Meta:
        model = ClassRoom

        fields = "__all__"

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter name...",
                    "id": "name",
                },
            ),
            "category_name": forms.Select(
                attrs={
                    "class": "form-select border-success mt-1 mb-4",
                    "id": "category_name",
                },
            ),
        }
