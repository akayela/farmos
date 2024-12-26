from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('complete', 'Complete'),
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('incomplete', 'Incomplete')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    point = models.CharField(max_length=100)
    due = models.DateField()

    def __str__(self):
        return self.title

class TaskStatusChange(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    previous_status = models.CharField(max_length=20)
    current_status = models.CharField(max_length=20)
    changed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.current_status

class Why(models.Model):
    task = models.ForeignKey(Task, related_name='whys', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class Answer(models.Model):
    why = models.ForeignKey(Why, on_delete=models.CASCADE)
    answer = models.TextField()
    given_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.answer