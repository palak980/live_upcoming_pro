# Generated by Django 3.2 on 2023-04-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('like', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_video', models.FileField(blank=True, null=True, upload_to='docs/')),
                ('upload_photo', models.ImageField(blank=True, null=True, upload_to='docs/photo/')),
                ('upload_story', models.CharField(blank=True, max_length=10000000, null=True)),
            ],
        ),
    ]