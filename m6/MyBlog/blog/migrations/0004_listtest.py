# Generated by Django 2.0.1 on 2018-12-28 15:53

import blog.My_field
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181228_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', blog.My_field.ListField()),
            ],
        ),
    ]