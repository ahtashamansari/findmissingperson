# Generated by Django 3.0.3 on 2020-02-26 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.DecimalField(decimal_places=2, max_digits=10)),
                ('address', models.CharField(max_length=200)),
                ('contact_no', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='missing_faces/Known')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
