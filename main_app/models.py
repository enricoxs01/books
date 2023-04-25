from django.db import models
from django.urls import reverse

STATUS = (
    ('S','Started'),
    ('P', 'In Progress'),
    ('C', 'Completed')
)

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    date = models.IntegerField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})

class Chapter (models.Model):
    title = models.CharField(max_length = 200)
    date = models.DateField()
    status = models.CharField(
        max_length = 1,
        choices = STATUS,
        default= STATUS[0][0])
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    
    def __str__(self):
       return f"{self.get_status_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Bookmark (models.Model):
    page = models.PositiveIntegerField()
    note = models.CharField(max_length = 100)