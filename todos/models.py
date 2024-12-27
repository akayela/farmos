from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    point = models.CharField(max_length=100)
    due = models.DateField()
    
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title

class Status(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('complete', 'Complete'),
        ('incomplete', 'Incomplete')
    ])
    
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.status

class Analysis(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    question_1 = models.CharField(max_length=255)
    answer_1 = models.TextField()
    question_2 = models.CharField(max_length=255)
    answer_2 = models.TextField()
    question_3 = models.CharField(max_length=255)
    answer_3 = models.TextField()
    question_4 = models.CharField(max_length=255)
    answer_4 = models.TextField()
    question_5 = models.CharField(max_length=255)
    answer_5 = models.TextField()
    root_cause = models.TextField()
    solution = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Analysis"
        verbose_name_plural = "Analyses"

    def __str__(self):
        return self.solution
