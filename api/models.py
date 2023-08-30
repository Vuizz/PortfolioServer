from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Projects'

class WorkExperiences(models.Model):
    year = models.IntegerField()
    company = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.company
    
    class Meta:
        verbose_name_plural = 'Work Experiences'