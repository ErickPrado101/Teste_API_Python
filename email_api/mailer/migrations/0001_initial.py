# Generated by Django 4.2.6 on 2023-10-14 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('recipient', models.EmailField(max_length=254)),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
    ]
