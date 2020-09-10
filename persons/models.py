from django.db import models

class Specialty(models.Model):
    specialty = models.CharField('Назва спеціальності', max_length=200)
    
    def __str__(self):
        return self.specialty
    
    class Meta:
        verbose_name = 'Спеціальність'
        verbose_name_plural = 'Спеціальності'


class ProjectImage(models.Model):
    image = models.ImageField('Картинка проекту', upload_to='persons')
    name = models.CharField('Короткий опис картинки', max_length=100)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'Картинка проекту'
        verbose_name_plural = 'Картиники проекту'


class Project(models.Model):
    name = models.CharField('Назва проекту', max_length=200)
    description = models.TextField('Опис проекту')
    specialty = models.ManyToManyField(Specialty, help_text='Спеціальності проетку', related_name='project_specialty')
    images = models.ManyToManyField(ProjectImage, help_text='Картинки проекту', related_name='project_images')
    start_time = models.DateTimeField('Час початку проекту', blank=True, null=True)
    end_time = models.DateTimeField('Час закінчення проекту', blank=True, null=True)
    ended = models.BooleanField('Проект закрито', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекти'


class Teacher(models.Model):
    name = models.CharField('ПІБ', max_length=200)
    email = models.EmailField('Електронна адреса викладача', blank=True, null=True)
    image = models.ImageField('Профільна фотографія викладача', upload_to='persons/')
    credo = models.CharField('Життєве кредо', max_length=200, blank=True, null=True)
    description = models.TextField('Інформація про викладача')
    specialty = models.ManyToManyField( Specialty, help_text='Спеціальності викладача', related_name='teacher_specialty')
    projects = models.ManyToManyField(Project, help_text='Наукові роботи, проекти викладача', related_name='teacher_projects')
    channel = models.CharField('Канал комунікації з викладачем', help_text='в форматі: facebook.com/osint0', max_length=300, blank=True, null=True)
    slug = models.SlugField('Посилання на викладача')
    city = models.CharField('Місто народження', max_length=100, blank=True, null=True)
    date_of_birth = models.DateField('Дата народження', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Викладач'
        verbose_name_plural = 'Викладачі'


class Alumni(models.Model):
    name = models.CharField('ПІБ', max_length=200)
    image = models.ImageField('Профільна фотографія випускника', upload_to='persons/')
    description = models.TextField('Інформація про випускника')
    specialty = models.ManyToManyField(Specialty,help_text='Спеціальність, яку вивчав випускник', related_name='alumni_specialty')
    channel= models.CharField('Канал комунікації з випускником', max_length=300, blank=True, null=True)
    slug = models.SlugField('Посилання на випускника')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Випускник'
        verbose_name_plural = 'Випускники'



