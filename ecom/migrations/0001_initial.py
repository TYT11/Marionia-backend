# Generated by Django 4.1.7 on 2023-03-24 09:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('SLL', 'Shells'), ('WPN', 'Weapons'), ('MSHRM', 'Mushrooms'), ('MYBX', 'Mystery Boxes')], default='SLL', max_length=10)),
                ('img', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
