# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('coins', '0006_auto_20131220_0724')]

    operations = [
        migrations.RemoveField(
            name = 'inserted_by',
            model_name = 'coin',
        ),
    ]
