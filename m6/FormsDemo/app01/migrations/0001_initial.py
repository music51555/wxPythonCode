# Generated by Django 2.0.1 on 2018-11-22 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=5)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=11)),
            ],
        ),
    ]
