# Generated by Django 2.0.1 on 2019-03-04 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(on_delete=True, to='web.Customer', verbose_name='关联客户'),
        ),
    ]
