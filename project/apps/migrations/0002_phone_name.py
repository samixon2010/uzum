# Generated by Django 5.0.4 on 2024-05-01 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='name',
            field=models.CharField(default=20, max_length=100),
            preserve_default=False,
        ),
    ]
