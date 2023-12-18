from django.shortcuts import render, redirect
from .models import University, Student
from .forms import UniversityForm
from .forms import StudentForm
from django.views.generic import UpdateView, DeleteView


class UniversitiesUpdateView(UpdateView):
    model = University
    template_name = 'first/add_item.html'
    form_class = UniversityForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать университет'
        return context


class UniversitiesDeleteView(DeleteView):
    model = University
    template_name = 'first/delete_item.html'
    success_url = '/universities'

    # form_class = UniversityForm
    #
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить университет'
        context['name'] = self.object.full_name
        context['subject'] = 'Удалить университет'


        return context


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'first/index.html', data)  # Create your views here


def universities_view(request):
    data = {
        'title': 'Университеты'
    }
    universities = University.objects.all()
    return render(request, 'first/university.html', {'universities': universities})


def universities_add(request):
    error = ''
    form = UniversityForm()
    if request.method == 'POST':
        form = UniversityForm(request.POST)
        # form = UniversityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/universities')
        else:
            error = 'Введите корректные данные'
    data = {
        'title': "Создать университет",
        'form': form,
        'error': error
    }

    return render(request, 'first/add_item.html', data)


# --------------------------------------------------------------------------------------------------------

def students_view(request):
    students = Student.objects.all()
    data = {
        'title': 'Студенты',
        'students': students
    }
    return render(request, 'first/students.html', data)


def students_add(request):
    error = ''
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/students')
        else:
            error = 'Введите корректные данные'
    data = {
        'title': "Создать студента",
        'form': form,
        'error': error
    }

    return render(request, 'first/add_item.html', data)

class StudentsUpdateView(UpdateView):
    model = Student
    template_name = 'first/add_item.html'
    form_class = StudentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать университет'
        return context


class StudentsDeleteView(DeleteView):
    model = Student
    template_name = 'first/delete_item.html'
    success_url = '/students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить университет'
        context['subject'] = 'Удалить студента'
        context['name'] = self.object.full_name

        return context
