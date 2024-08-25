# Generated by Django 5.1 on 2024-08-25 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootcamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('start_date', models.DateField()),
                ('duration', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('assingment', models.ManyToManyField(related_name='assignments', to='bank.question')),
                ('lesson', models.ManyToManyField(related_name='lessons', to='bank.lesson')),
            ],
        ),
    ]
