# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('url', models.CharField(max_length=500),)],
            bases = (models.Model,),
            options = {},
            name = 'Image',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('title', models.CharField(max_length=100),), ('date_created', models.DateTimeField(verbose_name='date created'),)],
            bases = (models.Model,),
            options = {},
            name = 'Corpus',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('title', models.CharField(max_length=200),), ('pub_date', models.DateTimeField(verbose_name='date published'),), ('date_start', models.IntegerField(default=0),), ('date_end', models.IntegerField(default=0),), ('denomination', models.CharField(max_length=50),), ('minting_authority', models.CharField(max_length=200),), ('obverse_lengend', models.CharField(max_length=500),), ('reverse_legend', models.CharField(max_length=500),), ('bibliography', models.CharField(max_length=200),)],
            bases = (models.Model,),
            options = {},
            name = 'Coin',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=100),), ('email', models.CharField(max_length=100),), ('password', models.CharField(max_length=100),), ('privileges', models.IntegerField(default=0),), ('affiliation', models.CharField(max_length=100),)],
            bases = (models.Model,),
            options = {},
            name = 'User',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('title', models.CharField(max_length=100),)],
            bases = (models.Model,),
            options = {},
            name = 'Tag',
        ),
    ]
