# Generated by Django 3.1.7 on 2021-08-07 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymall', '0003_auto_20210807_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploadpics/'),
        ),
    ]
