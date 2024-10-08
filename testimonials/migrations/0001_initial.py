# Generated by Django 3.2.25 on 2024-08-18 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=254)),
                ('customer_age', models.IntegerField(blank=True, null=True)),
                ('customer_county', models.CharField(blank=True, max_length=80, null=True)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('headline', models.CharField(max_length=254)),
                ('body', models.TextField()),
            ],
        ),
    ]
