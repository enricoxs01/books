from django.forms import ModelForm
from .models import Chapter, Bookmark

class ChapterForm(ModelForm):
  class Meta:
    model = Chapter
    fields = ['title', 'date','status']


class BookmarkForm(ModelForm):
  class Meta:
    model = Bookmark
    fields = ['color', 'material']