# Generated by Django 4.1.3 on 2022-11-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer_start', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='inn',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]