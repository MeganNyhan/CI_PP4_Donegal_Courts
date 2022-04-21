# Generated by Django 3.2 on 2022-04-21 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220420_1814'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
        migrations.RemoveField(
            model_name='post',
            name='featured_image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='header_image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_on',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
