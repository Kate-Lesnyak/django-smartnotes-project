from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
   list_display = ('title', 'created_at', 'likes', 'user')


admin.site.register(Note, NoteAdmin)