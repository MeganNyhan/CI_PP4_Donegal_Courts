# Generated by Django 3.2 on 2022-05-18 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(editable=False, max_length=200)),
                ('last_name', models.CharField(editable=False, max_length=200)),
                ('from_email', models.EmailField(editable=False, max_length=200)),
                ('subject', models.CharField(editable=False, max_length=200)),
                ('message', models.TextField(editable=False, max_length=2000)),
            ],
        ),
    ]
