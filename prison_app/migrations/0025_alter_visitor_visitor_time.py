# Generated by Django 4.2.2 on 2023-08-01 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prison_app', '0024_visitor_visitor_image_visitor_visitor_relation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='visitor_time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
