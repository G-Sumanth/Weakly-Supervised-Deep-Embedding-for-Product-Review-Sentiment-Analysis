
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('weight', models.IntegerField()),
                ('color', models.CharField(choices=[('Red', 'Red'), ('Blue', 'Blue'), ('White', 'White'), ('Black', 'Black'), ('Golden', 'Golden'), ('Brown', 'Brown'), ('Others', 'Others')], max_length=200)),
                ('price', models.CharField(max_length=200)),
               
                ('images', models.FileField(upload_to='')),
            ],
        ),
    ]
