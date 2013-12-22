# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('coins', '0007_remove_coin_inserted_by')]

    operations = [
        migrations.AlterField(
            field = models.ForeignKey(to=u'coins.Location', default=0, to_field=u'id'),
            name = 'mint_location',
            model_name = 'coin',
        ),
        migrations.AlterField(
            field = models.ForeignKey(to=u'coins.Location', default=0, to_field=u'id'),
            name = 'find_location',
            model_name = 'coin',
        ),
    ]
