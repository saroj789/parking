# Generated by Django 4.0.4 on 2022-05-10 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.DateTimeField(blank=True, null=True)),
                ('exit_time', models.DateTimeField(blank=True, null=True)),
                ('is_avail', models.BooleanField(default=True)),
                ('position', models.CharField(blank=True, max_length=50, null=True)),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slots.parking')),
            ],
        ),
    ]
