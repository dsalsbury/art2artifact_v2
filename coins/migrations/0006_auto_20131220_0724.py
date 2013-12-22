# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('coins', '0005_auto_20131220_0711')]

    operations = [
        migrations.AlterField(
            field = models.DateTimeField(auto_now_add=True),
            name = 'pub_date',
            model_name = 'coin',
        ),
    ]
