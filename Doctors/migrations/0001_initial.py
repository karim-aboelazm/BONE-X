# Generated by Django 3.2.4 on 2021-06-30 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=200)),
                ('description', models.TextField(max_length=400)),
                ('image', models.ImageField(upload_to='doc/')),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
    ]