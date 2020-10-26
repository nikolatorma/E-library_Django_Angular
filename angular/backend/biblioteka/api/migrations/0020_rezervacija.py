# Generated by Django 3.1.1 on 2020-10-03 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20201003_0429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rezervacija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum_rezervacije', models.DateField()),
                ('id_clana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
                ('inv_broj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.primerak')),
            ],
        ),
    ]