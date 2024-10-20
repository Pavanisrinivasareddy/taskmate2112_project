# Generated by Django 5.0.6 on 2024-07-02 15:49

from django.db import migrations, models # type: ignore


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=300)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
