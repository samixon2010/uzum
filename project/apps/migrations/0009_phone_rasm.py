# Generated by Django 5.0.4 on 2024-05-13 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0008_alter_phone_rangi'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='rasm',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]