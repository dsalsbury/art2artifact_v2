# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('coins', '0001_initial')]

    operations = [
        migrations.AddField(
            field = models.DecimalField(default=0, max_digits=9, decimal_places=6),
            name = 'mint_long',
            model_name = 'coin',
        ),
        migrations.AddField(
            field = models.CharField(max_length=500, null=True),
            name = 'description',
            model_name = 'corpus',
        ),
        migrations.AddField(
            field = models.CharField(max_length=2, null=True, choices=(('RR', 'Roman Republican',), ('RI', 'Roman Imperial',), ('GA', 'Greek Archaic',), ('GC', 'Greek Classical',), ('GH', 'Greek Hellenistic',),)),
            name = 'era',
            model_name = 'coin',
        ),
        migrations.AddField(
            field = models.DecimalField(default=0, max_digits=9, decimal_places=6),
            name = 'mint_lat',
            model_name = 'coin',
        ),
        migrations.AlterField(
            field = models.CharField(max_length=50, null=True),
            name = 'denomination',
            model_name = 'coin',
        ),
        migrations.AlterField(
            field = models.CharField(max_length=500, null=True),
            name = 'reverse_legend',
            model_name = 'coin',
        ),
        migrations.AlterField(
            field = models.URLField(),
            name = 'url',
            model_name = 'image',
        ),
        migrations.AlterField(
            field = models.IntegerField(default=0, null=True),
            name = 'date_end',
            model_name = 'coin',
        ),
        migrations.AlterField(
            field = models.CharField(max_length=200, null=True),
            name = 'minting_authority',
            model_name = 'coin',
        ),
        migrations.AlterField(
            field = models.IntegerField(default=0, null=True),
            name = 'date_start',
            model_name = 'coin',
        ),
        migrations.AlterField(
            field = models.CharField(max_length=100, null=True),
            name = 'affiliation',
            model_name = 'user',
        ),
        migrations.AlterField(
            field = models.EmailField(max_length=75),
            name = 'email',
            model_name = 'user',
        ),
        migrations.AlterField(
            field = models.CharField(max_length=500, null=True),
            name = 'obverse_lengend',
            model_name = 'coin',
        ),
    ]
