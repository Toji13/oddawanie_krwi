# Generated by Django 3.2.5 on 2021-11-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='email',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='phone',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]
