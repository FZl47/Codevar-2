# Generated by Django 3.2.4 on 2021-07-08 19:19

import MemberGroup.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MemberGroup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membergroup',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=MemberGroup.models.UploadSrcImageInfo),
        ),
        migrations.CreateModel(
            name='WorkSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=150)),
                ('TimeElapsed', models.CharField(max_length=20)),
                ('Technologies', models.CharField(max_length=300)),
                ('Description', models.TextField()),
                ('Image', models.ImageField(upload_to=MemberGroup.models.UploadSrcImageWorkSample)),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MemberGroup.membergroup')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('ValueSkill', models.IntegerField(max_length=10)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MemberGroup.membergroup')),
            ],
        ),
    ]
