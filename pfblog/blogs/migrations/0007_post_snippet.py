# Generated by Django 4.2.6 on 2023-10-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='ve aqui para leer mas blogs', max_length=255),
        ),
    ]
