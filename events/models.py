from django.db import models


class EventTag(models.Model):
    tag = models.CharField('Теги', max_length=100)

    def __str__(self):
        return self.tag
    
    class Meta:
        verbose_name = 'Тег івенту'
        verbose_name_plural = 'Теги івенту'

class EventImage(models.Model):
    image = models.ImageField('Картинка для івенту', upload_to='images/event')
    description = models.CharField('Опис картинки', max_length=100)

    class Meta:
        verbose_name = 'Картинка події'
        verbose_name_plural = 'Картинки подій'

    def __str__(self):
        return self.description

class EventPartner(models.Model):
    name = models.CharField('Імя партнера', max_length=200)
    image = models.ImageField('Фото партнера/Логотип компанії',upload_to='images/event/partner')
    description = models.CharField('Коротко про партнера', max_length=200)
    link = models.CharField('Посилання на детальнішу інформацію', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Партнер події'
        verbose_name = 'Партнери подій'


class Event(models.Model):
    name = models.CharField('Назва', max_length=200)
    description = models.TextField('Опис')
    location = models.CharField('Локація', help_text='Місто/Вулиця/Номер будинку', max_length=200, blank=True, null=True)
    date = models.DateTimeField('Час початку', blank=True, null=True)
    tags = models.ManyToManyField(EventTag, related_name='event_tags', blank=True, null=True)
    images = models.ManyToManyField(EventImage, related_name='event_images', blank=True, null=True)
    top_image = models.ImageField('Головне зображення події', upload_to='events/images', blank=True, null=True)
    partner = models.ManyToManyField(EventPartner, related_name='event_partner', blank=True, null=True)
    fb_event = models.CharField('Посилання на подію у fb', max_length=200, blank=True, null=True)
    slug = models.SlugField('Посилання')
    conducted = models.BooleanField('Відбулася', default=False)

    def conducted_event(self):
        import datetime
        if self.date > datetime.datetime.now:
            self.conducted = True
            return self.conducted
        else:
            self.conducted = False
            return self.conducted

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Подія'
        verbose_name_plural = 'Події'

    
