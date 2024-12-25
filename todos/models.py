from django.db import models

# Create your models here.

class Task(models.Model):
    assignment = models.CharField(max_length=255)
    assingee = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[
        ('complete', 'Complete'),
        ('pending', 'Pending'),
        ('in_progress', 'in_progress'),
        ('incomplete', 'Incomplete'),
    ])

    def __str__(self):
        return self.assignment
    
    
class TaskStatusChange(models.Model):
    assignment = models.ForeignKey(Task, on_delete=models.CASCADE)
    previous_status = models.CharField(max_length=20)
    current_status = models.CharField(max_length=20)

    def __str__(self):
        return self.current_status
    

class Why(models.Model):
    assignment = models.ForeignKey(Task, related_name='whys', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question
    

class Answer(models.Model):
    why = models.ForeignKey(Why, on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return self.answer