# Generated by Django 5.0.6 on 2024-06-09 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=50, unique=True)),
                ('amount', models.FloatField()),
                ('phone_number', models.CharField(max_length=20)),
                ('account_reference', models.CharField(max_length=50)),
                ('transaction_desc', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
