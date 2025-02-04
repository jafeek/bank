# Generated by Django 4.2.8 on 2024-10-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('district', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('pasword', models.CharField(max_length=200)),
                ('pasword1', models.CharField(max_length=160)),
            ],
        ),
    ]
