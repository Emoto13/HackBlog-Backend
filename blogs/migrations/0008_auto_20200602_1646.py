# Generated by Django 3.0.6 on 2020-06-02 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20200530_0829'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['date', 'title']},
        ),
    ]
