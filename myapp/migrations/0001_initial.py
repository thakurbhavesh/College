# Generated by Django 3.0.6 on 2020-12-30 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=100)),
                ('mobile', models.ImageField(max_length=10, upload_to='')),
            ],
        ),
    ]
