# Generated by Django 4.2.2 on 2023-07-12 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prison_app', '0012_prisoner_from_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duty_name', models.CharField(max_length=30)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('jailor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('police', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prison_app.policereg')),
                ('prison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prison_app.prisoner')),
            ],
        ),
    ]
