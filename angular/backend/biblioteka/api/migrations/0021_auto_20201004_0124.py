# Generated by Django 3.1.1 on 2020-10-03 23:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_rezervacija'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezervacija',
            name='datum_rezervacije',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
