# Generated by Django 3.2 on 2022-05-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20220525_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=2550, null=True),
        ),
    ]
