from django.db import models
from persons.models import Teacher

class Group(models.Model):
    name = models.CharField('Назва групи', max_length=100)
    image = models.ImageField('Лого групи', upload_to='images/group_logo', blank=True, null=True)

    class Meta:
        verbose_name = 'Група'
        verbose_name_plural ='Групи'

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField('Назва предмету', max_length=100)
    teacher = models.ManyToManyField(Teacher, related_name='teachers')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмети'

class StudentHW(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    name = models.CharField('Назва домашнього завдання', max_length=200)
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    done_task = models.FileField('Домашнє завдання', upload_to='homeworks/', blank=True, null=True)
    passed = models.BooleanField('Здано', default=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Домашня робота'
        verbose_name_plural = 'Домашні роботи'

class Student(models.Model):
    name = models.CharField('ПІБ студента', max_length=100)
    image = models.ImageField('Портретне фото студента', upload_to='images/student_profile_photo')
    slug = models.SlugField('Посилання на студента')
    group = models.ForeignKey(Group, help_text='Група студента', on_delete=models.CASCADE)
    about = models.TextField('Про студента')
    subjects = models.ManyToManyField(Subject, related_name='student_subjects')

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенти'





    
