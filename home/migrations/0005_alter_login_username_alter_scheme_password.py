# Generated by Django 4.2.6 on 2023-11-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_scheme_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='password',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
