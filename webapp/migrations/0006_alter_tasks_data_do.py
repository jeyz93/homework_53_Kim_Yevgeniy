# Generated by Django 4.1.1 on 2022-09-19 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_tasks_data_do_alter_tasks_set_st'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='data_do',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата выполненияя'),
        ),
    ]