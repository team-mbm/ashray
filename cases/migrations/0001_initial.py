# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-08 05:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_filer_name', models.CharField(blank=True, max_length=20, verbose_name='Complaintee Name')),
                ('name_child', models.CharField(max_length=20, verbose_name='Name of Child')),
                ('desc', models.TextField(blank=True, verbose_name='Description')),
                ('age_of_child', models.IntegerField(verbose_name='Age')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(blank=True, max_length=20, verbose_name='Contact Number')),
                ('email', models.CharField(blank=True, max_length=20, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_number', models.CharField(blank=True, max_length=20, verbose_name='Street Number')),
                ('city', models.CharField(blank=True, max_length=20, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=20, verbose_name='State')),
                ('pin_code', models.CharField(blank=True, max_length=20, verbose_name='Pin Code')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, verbose_name='Name')),
                ('desc', models.TextField(blank=True, verbose_name='Description')),
                ('max_age', models.IntegerField(verbose_name='Age')),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.Contact'),
        ),
        migrations.AddField(
            model_name='case',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.Location'),
        ),
        migrations.AddField(
            model_name='case',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.TypeOfCase'),
        ),
    ]
