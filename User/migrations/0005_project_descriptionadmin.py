# Generated by Django 3.2.4 on 2021-08-02 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20210802_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='DescriptionAdmin',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
