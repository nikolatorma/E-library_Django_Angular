# Generated by Django 3.1.1 on 2020-10-01 18:27

import biblioteka.api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20201001_2015'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KnjigaSlika',
        ),
        migrations.AddField(
            model_name='knjiga',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=biblioteka.api.models.upload_path),
        ),
    ]
