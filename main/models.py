from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False, verbose_name='FirstName')
    last_name = models.CharField(max_length=255, null=False, blank=False, verbose_name='LastName')
    phone_number = models.CharField(max_length=255, null=False, blank=False, verbose_name='PhoneNumber')
    address = models.TextField(null=False, blank=False, verbose_name='Address')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date', )
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Updated Date', )

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ('id',)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
