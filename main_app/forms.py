from django.forms import ModelForm
from .models import Chapter

class ChapterForm(ModelForm):
  class Meta:
    model = Chapter
    fields = ['title', 'date','status']