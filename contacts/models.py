from django.db import models
from events.models import Event

class Contact(models.Model):
    name = models.CharField('ПІБ', max_length=200)
    email = models.EmailField('Пошта', max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Подія')

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакти'
    
