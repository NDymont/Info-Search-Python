from django import forms
from .models import University, Student
from datetime import date


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['full_name', 'short_name', 'creation_date']
        widgets = {
            "full_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Полное название университета'
            }),
            "short_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сокращенное название университета'
            }),
            "creation_date": forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'mm/dd/yyyy',
                'autocomplete': "off",
                'value': date.today().strftime('%m/%d/%Y'),
            })
        }
        input_formats = {
            'creation_date': ['%d/%m/%Y']
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'university', 'birth_date', 'enrollment_year']
        widgets = {
            "full_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            "birth_date": forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'mm/dd/yyyy',
                'autocomplete': "off",
                'value': date.today().strftime('%m/%d/%Y'),
            }),
            "enrollment_year": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год выпуска'
            }),

            "university": forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите университет',
                # Дополнительные настройки, если необходимо
            }),

        }
