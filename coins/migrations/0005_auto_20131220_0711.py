# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('coins', '0004_auto_20131220_0659')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=200),), ('lat', models.DecimalField(default=0, max_digits=9, decimal_places=6),), ('lon', models.DecimalField(default=0, max_digits=9, decimal_places=6),)],
            bases = (models.Model,),
            options = {},
            name = 'Location',
        ),
        migrations.AddField(
            field = models.ForeignKey(to=u'coins.Location', default='tester', to_field=u'id'),
            name = 'mint_location',
            model_name = 'coin',
        ),
        migrations.AddField(
            field = models.ForeignKey(to=u'coins.Location', default='tester', to_field=u'id'),
            name = 'find_location',
            model_name = 'coin',
        ),
        migrations.RemoveField(
            name = 'mint_long',
            model_name = 'coin',
        ),
        migrations.RemoveField(
            name = 'find_long',
            model_name = 'coin',
        ),
        migrations.RemoveField(
            name = 'find_lat',
            model_name = 'coin',
        ),
        migrations.RemoveField(
            name = 'mint_lat',
            model_name = 'coin',
        ),
    ]
