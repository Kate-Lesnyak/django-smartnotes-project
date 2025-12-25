from django import forms
from django.core.exceptions import ValidationError

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
      model = Note
      fields=('title','text')
      widgets={
          'title': forms.TextInput(attrs={'class':'form-control my-5'}),
          'text': forms.Textarea(attrs={'class':'form-control mb-5'}),
      }
      labels={
          'text': "Write your thoughts here"
      }


    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise ValidationError('The title must be at least 5 characters long.')
        return title
    
    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 10:
            raise ValidationError('The note text must be at least 10 characters long.')
        return text