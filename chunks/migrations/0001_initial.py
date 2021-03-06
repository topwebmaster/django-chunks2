# Generated by Django 1.10.2 on 2016-11-10 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chunk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(help_text='A unique name for this chunk of content', max_length=255, unique=True, verbose_name='key')),
                ('content', models.TextField(blank=True, verbose_name='content')),
            ],
            options={
                'ordering': ('key',),
                'abstract': False,
                'verbose_name_plural': 'Text Chunks',
                'verbose_name': 'Text Chunk',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(help_text='A name for chunks group', max_length=255, verbose_name='key')),
                ('content', models.TextField(blank=True, verbose_name='content')),
            ],
            options={
                'ordering': ('key',),
                'verbose_name_plural': 'Group Chunks',
                'verbose_name': 'Group Chunk',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(help_text='A unique name for this chunk of content', max_length=255, unique=True, verbose_name='key')),
                ('image', models.ImageField(max_length=255, upload_to='chunks/images', verbose_name='image')),
            ],
            options={
                'ordering': ('key',),
                'abstract': False,
                'verbose_name_plural': 'Image Chunks',
                'verbose_name': 'Image Chunk',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(help_text='A unique name for this chunk of content', max_length=255, unique=True, verbose_name='key')),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('desc', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('media', models.FileField(blank=True, max_length=256, null=True, upload_to='chunks/media', verbose_name='Media')),
            ],
            options={
                'ordering': ('key',),
                'abstract': False,
                'verbose_name_plural': 'Media Chunks',
                'verbose_name': 'Media Chunk',
            },
        ),
    ]
