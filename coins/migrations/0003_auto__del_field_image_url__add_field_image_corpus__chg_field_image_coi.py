# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Image.url'
        db.delete_column(u'coins_image', 'url')

        # Adding field 'Image.corpus'
        db.add_column(u'coins_image', 'corpus',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coins.Corpus'], null=True),
                      keep_default=False)


        # Changing field 'Image.coin'
        db.alter_column(u'coins_image', 'coin_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coins.Coin'], null=True))

    def backwards(self, orm):
        # Adding field 'Image.url'
        db.add_column(u'coins_image', 'url',
                      self.gf('django.db.models.fields.URLField')(default=datetime.datetime(2013, 12, 24, 0, 0), max_length=200),
                      keep_default=False)

        # Deleting field 'Image.corpus'
        db.delete_column(u'coins_image', 'corpus_id')


        # Changing field 'Image.coin'
        db.alter_column(u'coins_image', 'coin_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coins.Coin']))

    models = {
        u'coins.coin': {
            'Meta': {'object_name': 'Coin'},
            'bibliography': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_end': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'date_start': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'denomination': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'era': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'find_location': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'find'", 'to': u"orm['coins.Location']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mint_location': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'mint'", 'to': u"orm['coins.Location']"}),
            'minting_authority': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'obverse_lengend': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'reverse_legend': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'coins.coin_has_tag': {
            'Meta': {'object_name': 'coin_has_tag'},
            'coin': ('django.db.models.fields.related.ForeignKey', [], {'default': "'tester'", 'to': u"orm['coins.Coin']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'default': "'tester'", 'to': u"orm['coins.Tag']"})
        },
        u'coins.coin_in_corpus': {
            'Meta': {'object_name': 'coin_in_corpus'},
            'coin': ('django.db.models.fields.related.ForeignKey', [], {'default': "'tester'", 'to': u"orm['coins.Coin']"}),
            'corpus': ('django.db.models.fields.related.ForeignKey', [], {'default': "'tester'", 'to': u"orm['coins.Corpus']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'coins.corpus': {
            'Meta': {'object_name': 'Corpus'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'default': "'tester'", 'to': u"orm['coins.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'coins.image': {
            'Meta': {'object_name': 'Image'},
            'coin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coins.Coin']", 'null': 'True'}),
            'corpus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coins.Corpus']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'static/coins/images/default_coin_image.jpeg'", 'max_length': '100'})
        },
        u'coins.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '6'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '6'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'coins.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'coins.user': {
            'Meta': {'object_name': 'User'},
            'affiliation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'privileges': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['coins']