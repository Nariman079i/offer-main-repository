# Generated by Django 4.1.3 on 2022-11-11 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_profile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='img/')),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('industry', models.CharField(max_length=40)),
                ('locate', models.CharField(max_length=40, null=True)),
                ('status', models.CharField(max_length=80)),
                ('role', models.CharField(choices=[('inv', 'Инвестор'), ('bus', 'Предприниматель'), ('com', 'Компания')], max_length=30)),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
