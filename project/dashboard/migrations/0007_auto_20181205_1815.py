# Generated by Django 2.1.4 on 2018-12-05 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20181205_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountdetails',
            old_name='b_acc',
            new_name='Bank_Account',
        ),
        migrations.RenameField(
            model_name='accountdetails',
            old_name='b_tra',
            new_name='Bank_Balance',
        ),
        migrations.RemoveField(
            model_name='user',
            name='acc_bal',
        ),
    ]