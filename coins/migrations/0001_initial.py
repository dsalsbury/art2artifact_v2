# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'coins_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('privileges', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('affiliation', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'coins', ['User'])

        # Adding model 'Location'
        db.create_table(u'coins_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=9, decimal_places=6)),
            ('lon', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=9, decimal_places=6)),
        ))
        db.send_create_signal(u'coins', ['Location'])

        # Adding model 'Coin'
        db.create_table(u'coins_coin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_start', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('date_end', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('denomination', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('minting_authority', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('obverse_lengend', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('reverse_legend', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('bibliography', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('era', self.gf('django.db.models.fields.CharField')(max_length=2, null=True)),
            ('mint_location', self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='mint', to=orm['coins.Location'])),
            ('find_location', self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='find', to=orm['coins.Location'])),
        ))
        db.send_create_signal(u'coins', ['Coin'])

        # Adding model 'Tag'
        db.create_table(u'coins_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'coins', ['Tag'])

        # Adding model 'coin_has_tag'
        db.create_table(u'coins_coin_has_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(default='tester', to=orm['coins.Tag'])),
            ('coin', self.gf('django.db.models.fields.related.ForeignKey')(default='tester', to=orm['coins.Coin'])),
        ))
        db.send_create_signal(u'coins', ['coin_has_tag'])

        # Adding model 'Corpus'
        db.create_table(u'coins_corpus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(default='tester', to=orm['coins.User'])),
        ))
        db.send_create_signal(u'coins', ['Corpus'])

        # Adding model 'coin_in_corpus'
        db.create_table(u'coins_coin_in_corpus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('corpus', self.gf('django.db.models.fields.related.ForeignKey')(default='tester', to=orm['coins.Corpus'])),
            ('coin', self.gf('django.db.models.fields.related.ForeignKey')(default='tester', to=orm['coins.Coin'])),
        ))
        db.send_create_signal(u'coins', ['coin_in_corpus'])

        # Adding model 'Image'
        db.create_table(u'coins_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('coin', self.gf('django.db.models.fields.related.ForeignKey')(default='tester', to=orm['coins.Coin'])),
        ))
        db.send_create_signal(u'coins', ['Image'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'coins_user')

        # Deleting model 'Location'
        db.delete_table(u'coins_location')

        # Deleting model 'Coin'
        db.delete_table(u'coins_coin')

        # Deleting model 'Tag'
        db.delete_table(u'coins_tag')

        # Deleting model 'coin_has_tag'
        db.delete_table(u'coins_coin_has_tag')

        # Deleting model 'Corpus'
        db.delete_table(u'coins_corpus')

        # Deleting model 'coin_in_corpus'
        db.delete_table(u'coins_coin_in_corpus')

        # Deleting model 'Image'
        db.delete_table(u'coins_image')


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
            'coin': ('django.db.models.fields.related.ForeignKey', [], {'default': "'tester'", 'to': u"orm['coins.Coin']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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