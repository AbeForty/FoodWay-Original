# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-28 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zipcode', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
        migrations.RemoveField(
            model_name='user',
            name='street',
        ),
        migrations.RemoveField(
            model_name='user',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='delivery',
            name='address',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_address', to='food_app.Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='food_app.Address'),
            preserve_default=False,
        ),
    ]
