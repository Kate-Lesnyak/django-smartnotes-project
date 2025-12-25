# from typing import List
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NoteForm
from .models import Note

# def notes_list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

# def note_detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
    
#     return render(request, 'notes/note_detail.html', {'note': note})


class NotesListView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
   
    def get_queryset(self):
        if self.request.user.is_authenticated:          
            return self.request.user.notes.all()
        else:
           return Note.objects.filter(is_public=True)

class NotesPopularListView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    queryset = Note.objects.filter(likes__gte=1)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class =  NoteForm
    success_url = '/smart/notes'
    login_url = "/accounts/login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NoteDetailView(LoginRequiredMixin,DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/note_detail.html'
    login_url = "/accounts/login"

class NotePublicDetailView(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/note_detail.html'
    queryset = Note.objects.filter(is_public=True)

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    success_url = '/smart/notes'
    form_class = NoteForm
    login_url = "/accounts/login"


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = '/smart/notes'
    template_name = 'notes/note_delete.html'
    login_url = "/accounts/login"

@login_required(login_url = "/accounts/login")
def add_like_view(request, pk):
    if request.method == "POST":
        note = get_object_or_404(Note, pk=pk)
        note.likes += 1
        note.save()
        return HttpResponseRedirect(reverse('note_detail', args=(pk,)))
    raise Http404()

@login_required(login_url = "/accounts/login")
def change_visibility_view(request, pk):
    if request.method == "POST":
        note = get_object_or_404(Note, pk=pk)
        note.is_public = not note.is_public
        note.save()
        return HttpResponseRedirect(reverse('note_detail', args=(pk,)))
    raise Http404()