# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('coins', '0002_auto_20131218_1639')]

    operations = [
        migrations.AddField(
            field = models.DecimalField(default=0, max_digits=9, decimal_places=6),
            name = 'find_long',
            model_name = 'coin',
        ),
        migrations.AddField(
            field = models.DecimalField(default=0, max_digits=9, decimal_places=6),
            name = 'find_lat',
            model_name = 'coin',
        ),
    ]
