# Generated by Django 3.1.5 on 2021-04-05 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210321_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=250)),
                ('Phone', models.CharField(max_length=30)),
                ('Message', models.TextField()),
            ],
        ),
    ]