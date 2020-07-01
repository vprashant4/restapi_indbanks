# Generated by Django 2.2.4 on 2019-08-22 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('name', models.CharField(blank=True, max_length=49, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'banks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('ifsc', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('branch', models.CharField(blank=True, max_length=74, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('district', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=26, null=True)),
            ],
            options={
                'db_table': 'branches',
                'managed': False,
            },
        ),
    ]
