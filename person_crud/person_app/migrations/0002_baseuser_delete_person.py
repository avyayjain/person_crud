# Generated by Django 4.0.1 on 2023-10-02 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
