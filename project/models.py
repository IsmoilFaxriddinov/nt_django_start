from django.db import models

class TeacherModel(models.Model):
    name = models.CharField(max_length=255, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

class StudentModel(models.Model):
    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

class GroupModel(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ManyToManyField(TeacherModel)
    students = models.ManyToManyField(StudentModel)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

class LessonModel(models.Model):
    name = models.CharField(max_length=50)
    groups = models.ForeignKey(GroupModel, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

class HomeworkModel(models.Model):
    info = models.TextField()
    lesson = models.OneToOneField(LessonModel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.info

    class Meta:
        verbose_name = 'Homework'
        verbose_name_plural = 'Homeworks'