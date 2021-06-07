# Generated by Django 3.2.2 on 2021-05-10 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=250)),
                ('text', models.TextField(max_length=1000)),
            ],
        ),
        migrations.AlterModelOptions(
            name='myself',
            options={'verbose_name': 'Myself', 'verbose_name_plural': 'Myself'},
        ),
    ]