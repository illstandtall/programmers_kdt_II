# Generated by Django 3.2.3 on 2021-05-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burger',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=30)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]