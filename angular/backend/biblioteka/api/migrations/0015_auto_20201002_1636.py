# Generated by Django 3.1.1 on 2020-10-02 14:36

import biblioteka.api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20201001_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnjigaSlika',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to=biblioteka.api.models.upload_path)),
            ],
        ),
        migrations.RemoveField(
            model_name='knjiga',
            name='img',
        ),
    ]