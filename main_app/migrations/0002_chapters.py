# Generated by Django 4.2 on 2023-04-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cTitle', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('S', 'Started'), ('P', 'In Progress'), ('C', 'Completed')], default='S', max_length=1)),
            ],
        ),
    ]
