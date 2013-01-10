# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table('events_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_happens', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_opens', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_closes', self.gf('django.db.models.fields.DateTimeField')()),
            ('max_participants', self.gf('django.db.models.fields.IntegerField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('info', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('events', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table('events_event')


    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'date_closes': ('django.db.models.fields.DateTimeField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_happens': ('django.db.models.fields.DateTimeField', [], {}),
            'date_opens': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'max_participants': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['events']