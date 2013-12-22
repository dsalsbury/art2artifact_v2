# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('coins', '0003_auto_20131218_1641')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('tag', models.ForeignKey(to=u'coins.Tag', default='tester', to_field=u'id'),), ('coin', models.ForeignKey(to=u'coins.Coin', default='tester', to_field=u'id'),)],
            bases = (models.Model,),
            options = {},
            name = 'coin_has_tag',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('corpus', models.ForeignKey(to=u'coins.Corpus', default='tester', to_field=u'id'),), ('coin', models.ForeignKey(to=u'coins.Coin', default='tester', to_field=u'id'),)],
            bases = (models.Model,),
            options = {},
            name = 'coin_in_corpus',
        ),
        migrations.AddField(
            field = models.ForeignKey(to=u'coins.User', default='tester', to_field=u'id'),
            name = 'inserted_by',
            model_name = 'coin',
        ),
        migrations.AddField(
            field = models.ForeignKey(to=u'coins.Coin', default='tester', to_field=u'id'),
            name = 'coin',
            model_name = 'image',
        ),
        migrations.AddField(
            field = models.ForeignKey(to=u'coins.User', default='tester', to_field=u'id'),
            name = 'created_by',
            model_name = 'corpus',
        ),
    ]
