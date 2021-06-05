# Generated by Django 3.0.8 on 2021-06-05 13:47

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
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogtype', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('author', models.ManyToManyField(related_name='custom_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('degree', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='custom_user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]