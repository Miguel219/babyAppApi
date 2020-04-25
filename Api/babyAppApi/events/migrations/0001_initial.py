# Generated by Django 3.0.5 on 2020-04-25 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('babies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventType', models.CharField(max_length=50)),
                ('notes', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('baby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='babies.Baby')),
            ],
        ),
    ]
