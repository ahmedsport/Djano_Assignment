# Generated by Django 3.1.5 on 2021-05-27 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fresher', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
