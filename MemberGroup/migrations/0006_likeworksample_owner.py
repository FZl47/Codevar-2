# Generated by Django 3.2.4 on 2021-07-09 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
        ('MemberGroup', '0005_likeworksample'),
    ]

    operations = [
        migrations.AddField(
            model_name='likeworksample',
            name='Owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='User.user'),
            preserve_default=False,
        ),
    ]
