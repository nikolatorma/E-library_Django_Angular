# Generated by Django 3.1.1 on 2020-10-01 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20201001_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='knjigaslika',
            name='filename',
            field=models.CharField(default='slika', max_length=32),
            preserve_default=False,
        ),
    ]
