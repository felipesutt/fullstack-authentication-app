# Generated by Django 5.1.2 on 2024-10-09 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='access_level',
            field=models.IntegerField(default=1),
        ),
    ]
