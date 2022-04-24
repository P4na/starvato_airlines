# Generated by Django 4.0.3 on 2022-04-24 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('starvato_airlines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, max_length=36)),
                ('model', models.CharField(max_length=100)),
                ('seats', models.IntegerField(default=60)),
                ('km_tot', models.IntegerField(default=0)),
                ('pilots_num', models.IntegerField(default=4)),
                ('team_num', models.IntegerField(default=4)),
            ],
        ),
        migrations.CreateModel(
            name='Fly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, max_length=36)),
                ('free_seats', models.IntegerField(default=10000)),
                ('aircraft', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='starvato_airlines.aircraft')),
            ],
        ),
    ]
