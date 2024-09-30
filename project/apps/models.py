from django.db import models


class Phone(models.Model):
    STATUS = (
        ('kelishiladi', 'kelishiladi'),
        ('barter', 'barter'),
        ('tekin', 'tekin'),
        ('naxt', 'naxt')
    )
    XOTIRA = (
        ('8 GB', '8GB'),
        ('16 GB', '16GB'),
        ('32 GB', '32GB'),
        ('64 GB', '64 GB'),
        ('128 GB', '128 GB'),
        ('256 GB', '256 GB')
    )
    RANGI = (
        ('black', 'black'),
        ('titanium', 'titanium'),
        ('pink', 'pink'),
        ('yellow', 'yellow'),
        ('grey', 'grey'),
        ('blue', 'blue'),
        ('white', 'white')
    )
    name = models.CharField(max_length=100)
    narxi = models.IntegerField(default=0)
    rangi = models.CharField(max_length=50, null=True, choices=RANGI, default='pink')
    holati = models.CharField(max_length=50,  choices=STATUS, default='naxt')
    xotira = models.CharField(max_length=50, choices=XOTIRA, default=0)
    rasm = models.ImageField(null=True)

    def __str__(self):
        return self.name + ' -> ' + str(self.narxi) + '$' + ' ' + self.rangi
    


from django import forms

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['name', 'narxi', 'rangi', 'holati', 'xotira', 'rasm']