# Generated by Django 3.1.5 on 2021-06-01 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20210601_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=200)),
                ('last', models.CharField(max_length=200)),
                ('gmail', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
