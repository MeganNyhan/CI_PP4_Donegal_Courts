# Generated by Django 3.2 on 2022-04-20 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220416_1644'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Carausel',
        ),
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
