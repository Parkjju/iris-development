# Generated by Django 4.0.3 on 2022-06-07 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0003_alter_predresults_ml_param'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predresults',
            name='ml_param',
            field=models.TextField(default='default', max_length=256),
        ),
    ]
