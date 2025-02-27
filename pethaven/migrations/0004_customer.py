# Generated by Django 5.1.4 on 2024-12-15 05:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pethaven', '0003_alter_product_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('district', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Chittagong', 'Chittagong'), ('Sylhet', 'Sylhet'), ('Rangpur', 'Rangpur'), ('Rajshahi', 'Rajshahi'), ('Mymensingh', 'Mymensingh'), ('Khulna', 'Khulna'), ('Barisal', 'Barisal')], max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
