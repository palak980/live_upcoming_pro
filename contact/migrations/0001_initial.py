# Generated by Django 3.2 on 2023-08-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mymsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=20000, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=13, null=True)),
                ('msg', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
