# Generated by Django 5.0.4 on 2024-05-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Iphone',
            },
        ),
    ]
