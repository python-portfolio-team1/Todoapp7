from django.db import models

# Create your models here.

class Category(models.Model): # The Category table name that inherits models.Model
    name= models.CharField(max_length=100) #Like a varchar
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name #name to be shown when called
 
class ToDo(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    Description = models.TextField(blank = False)
    Date = models.DateTimeField(blank=False)
    Category = models.ForeignKey(Category, default="general",on_delete=models.PROTECT)
    Completed = models.BooleanField(default=False)
    class Meta:
        ordering = ["-Date"]

    def __str__(self):
        return self.Title
