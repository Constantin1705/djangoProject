from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.forms import StudentForm
from student.models import Student


# LoginRequiredMixin, pentru a nu lasa utilizatorul sa creeze daca nu este logat
# vezi mai jos pentru functie
class StudentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'student/create_student.html'  # specificam calea catre fisierul html unde vom avea un formular
    model = Student
    # # fields = '__all__'  # formularul va contine toate field-urile din modelul Student(models.py)
    # fields = ['first_name', 'last_name', 'age', 'is_olympic',
    #           'email', 'description', 'start_date', 'end_date',
    #           'average', 'gender']  # putem schimba si ordinea field-urilor
    # ce este comentat deasupra, s-a mutat in student.forms
    # in loc de ce era deasupra, am pus form_class = StudentForm
    form_class = StudentForm
    success_url = reverse_lazy('home')  # dupa salvarea datelor din formular vom fi redirectonati catre pagina Home

    # ! reverse_lazy('home') -> home este name-ul url-ului din aplicatia home -> urls.py


class StudentListView(LoginRequiredMixin, ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'

    # def get_queryset(self):
    #     return Student.objects.filter(active=True,  # se pot pune si mai multe reguli de filtrare
    #                                   is_olympic=True)  # va afisa in interfata doar studentii care sunt activi

    def get_queryset(self):
        return Student.objects.filter(active=True)


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list_of_students')


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list_of_students')


class StudentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'student/details_student.html'
    model = Student


# asa se face pentru a nu putea accesa metoda, daca suntem logati
@login_required
def inactivate_student(request, pk):
    Student.objects.filter(id=pk).update(active=False)
    return redirect('list_of_students')


@login_required
def delete_student(request, pk):
    Student.objects.filter(id=pk).delete()
    return redirect('list_of_students')
