# Generated by Django 4.2.2 on 2023-07-11 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prison_app', '0007_rename_page_policereg_p_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prisoner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('aadhar', models.CharField(max_length=30)),
            ],
        ),
    ]
