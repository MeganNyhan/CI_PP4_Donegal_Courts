# Generated by Django 3.2 on 2022-05-04 19:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_rename_profile_userprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='UserProf',
        ),
    ]
