# Generated by Django 3.0.3 on 2020-03-19 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('face', '0014_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Missing_Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.DecimalField(decimal_places=2, max_digits=10)),
                ('address', models.CharField(max_length=200)),
                ('Contact_no', models.DecimalField(decimal_places=2, max_digits=15)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('image_name', models.CharField(max_length=200)),
                ('file_type', models.CharField(choices=[('image', 'image')], max_length=256)),
            ],
        ),
    ]
