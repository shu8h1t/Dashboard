# Generated by Django 2.1.4 on 2018-12-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20181205_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='acc_bal',
            field=models.CharField(default=1000000, max_length=200),
            preserve_default=False,
        ),
    ]
