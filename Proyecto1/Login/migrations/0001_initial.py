# Generated by Django 3.0.3 on 2020-02-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mocar1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('ap_pat', models.CharField(max_length=254)),
                ('ap_mat', models.CharField(max_length=254)),
                ('edad', models.IntegerField(max_length=254)),
            ],
        ),
    ]