# Generated by Django 5.1 on 2024-08-25 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='assingment',
            field=models.ManyToManyField(blank=True, null=True, related_name='assignments', to='bank.question'),
        ),
        migrations.AlterField(
            model_name='class',
            name='lesson',
            field=models.ManyToManyField(blank=True, null=True, related_name='lessons', to='bank.lesson'),
        ),
    ]
