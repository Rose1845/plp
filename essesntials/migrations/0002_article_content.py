# Generated by Django 4.1.1 on 2022-09-16 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essesntials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default=''),
        ),
    ]