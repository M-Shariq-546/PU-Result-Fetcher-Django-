# Generated by Django 4.2.5 on 2023-09-22 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('institute', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('roll_no', models.CharField(max_length=20)),
                ('reg_no', models.CharField(max_length=20)),
            ],
        ),
    ]