from django.db import models

# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

class TeacherModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    student = models.IntegerField()
    clas = models.ForeignKey(StudentModel, on_delete=models.CASCADE)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

