# Generated by Django 2.2.6 on 2019-10-30 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_code', models.CharField(max_length=10)),
                ('lecture', models.CharField(max_length=100)),
                ('professor', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=10)),
                ('start_time', models.IntegerField()),
                ('end_time', models.IntegerField()),
                ('day_of_week', models.CharField(max_length=5)),
                ('is_register', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memos', to='item.Item')),
            ],
        ),
    ]
