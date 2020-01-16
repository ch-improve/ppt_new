# Generated by Django 2.2.6 on 2020-01-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ppt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(verbose_name='pptid')),
                ('png', models.CharField(max_length=200, verbose_name='url')),
            ],
            options={
                'db_table': 'ppt',
            },
        ),
    ]