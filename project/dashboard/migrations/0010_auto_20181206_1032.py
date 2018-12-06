# Generated by Django 2.1.4 on 2018-12-06 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20181205_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountdetails',
            name='transac',
            field=models.ForeignKey(default=1500, on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.Transac'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='transac',
            name='trans',
        ),
        migrations.AddField(
            model_name='transac',
            name='trans',
            field=models.ManyToManyField(through='dashboard.AccountDetails', to='dashboard.User'),
        ),
    ]