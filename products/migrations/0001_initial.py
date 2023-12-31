# Generated by Django 4.2.7 on 2023-12-26 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveBigIntegerField()),
                ('available', models.BooleanField(default=False)),
                ('text', models.TextField()),
            ],
        ),
    ]
