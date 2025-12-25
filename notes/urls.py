from django.urls import path
from . import views


urlpatterns = [
    path('notes', views.NotesListView.as_view(), name='notes_list'),
    path('notes/<int:pk>', views.NoteDetailView.as_view(), name='note_detail'),
    path('notes/<int:pk>/edit', views.NoteUpdateView.as_view(), name='note_update'),
    path('notes/<int:pk>/delete', views.NoteDeleteView.as_view(), name='note_delete'),
    path('notes/new', views.NoteCreateView.as_view(), name='note_new'),
    path('notes/<int:pk>/add_like', views.add_like_view, name='note_add_like'),
    path('notes/<int:pk>/change_visibility', views.change_visibility_view, name='note_change_visibility'),
    path('notes/<int:pk>/share', views.NotePublicDetailView.as_view(), name='note_share'),
]