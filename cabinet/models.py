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



class StudentSchedule(models.Model):
    WEEK = [
        ('Понеділок', "Понеділок"),
        ('Вівторок', 'Вівторок'),
        ('Середа', 'Середа'),
        ('Четвер', 'Четвер'),
        ("П'ятниця","П'ятниця"),
        ('Субота','Субота'),
    ]
    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    date = models.TimeField('Час уроку')
    teacher = models.ForeignKey(Teacher, verbose_name='Викладач', on_delete=models.CASCADE, blank=True, null=True )
    week_day = models.CharField('День тижня', max_length=20, choices=WEEK, default='Mon')
    group = models.ForeignKey(Group, verbose_name='Група', on_delete=models.CASCADE)

    def __str__(self):
        return self.week_day

    class Meta:
        verbose_name = 'Розклад'
        verbose_name_plural = 'Розклад'


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



class StudentHW(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField('Назва домашнього завдання', max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    done_task = models.FileField('Домашнє завдання', upload_to='homeworks/', blank=True, null=True, help_text='Залиште це поле пустим!')
    passed = models.BooleanField('Здано', default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    mark = models.SmallIntegerField('Оцінка', default=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Журнал оцінок'
        verbose_name_plural = 'Журнал оцінок'





    
