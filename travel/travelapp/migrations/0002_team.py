# Generated by Django 4.2 on 2023-04-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_Team', models.CharField(max_length=250)),
                ('img_Team', models.ImageField(upload_to='pics')),
                ('dese_Team', models.TextField()),
            ],
        ),
    ]