# Generated by Django 4.2.3 on 2023-08-07 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_userprofile_email_userprofile_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
