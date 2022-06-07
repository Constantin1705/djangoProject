from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from professor.forms import ProfessorForm
from professor.models import Professor


class ProfessorCreateView(LoginRequiredMixin, CreateView):
    template_name = 'professor/create_professor.html'
    model = Professor
    form_class = ProfessorForm
    success_url = reverse_lazy('home')


class ProfessorListView(LoginRequiredMixin, ListView):
    template_name = 'professor/list_of_professors.html'
    model = Professor
    context_object_name = 'all_professors'

    def get_queryset(self):
        return Professor.objects.filter(active=True)


class ProfessorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'professor/update_professor.html'
    model = Professor
    form_class = ProfessorForm
    success_url = reverse_lazy('list_of_professors')


class ProfessorDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'professor/delete_professor.html'
    model = Professor
    success_url = reverse_lazy('list_of_professors')


class ProfessorDetailView(LoginRequiredMixin, DetailView):
    template_name = 'professor/details_professor.html'
    model = Professor


@login_required
def inactivate_professor(request, pk):
    Professor.objects.filter(id=pk).update(active=False)
    return redirect('list_of_professors')


@login_required
def delete_professor(request, pk):
    Professor.objects.filter(id=pk).delete()
    return redirect('list_of_professors')
