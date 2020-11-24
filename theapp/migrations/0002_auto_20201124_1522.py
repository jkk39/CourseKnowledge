# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-11-24 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseID', models.IntegerField(primary_key=True, serialize=False)),
                ('coursename', models.CharField(max_length=50)),
                ('credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EnrollsIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('grade', models.FloatField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theapp.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theapp.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('profID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theapp.Professor'),
        ),
    ]
