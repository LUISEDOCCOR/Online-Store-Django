# Generated by Django 4.2.7 on 2023-12-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveBigIntegerField()),
                ('available', models.BooleanField(default=False)),
                ('text', models.TextField()),
                ('img', models.ImageField(default='null', upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
