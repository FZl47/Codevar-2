# Generated by Django 3.2.4 on 2022-03-28 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MemberGroup', '0010_alter_membergroup_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='membergroup',
            name='Github',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='membergroup',
            name='Is_Checked',
            field=models.BooleanField(default=False),
        ),
    ]
