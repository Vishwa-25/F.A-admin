# Generated by Django 3.1.1 on 2020-09-15 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend', '0008_auto_20200915_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='emp_id',
            field=models.TextField(),
        ),
    ]
