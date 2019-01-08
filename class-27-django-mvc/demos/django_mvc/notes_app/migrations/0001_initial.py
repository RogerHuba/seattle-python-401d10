# Generated by Django 2.1.1 on 2019-01-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=48)),
                ('detail', models.CharField(max_length=4096)),
                ('status', models.CharField(choices=[('incomplete', 'Incomplete'), ('complete', 'Complete')], default='incomplete', max_length=48)),
            ],
        ),
    ]
