from django.db import models

PRIORITY = [
("LOW","low"),
("MEDIUM","medium"),
("HIGH","high")
]
  
# Create your models here.
class Question(models.Model):
    title =  models.CharField(max_length=100)
    question = models.TextField(max_length=400)
    priority = models.CharField(max_length=12, choices=PRIORITY)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Their Questions"
        verbose_name_plural = "People Questions"