# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'General'
        db.create_table('content_general', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('content', ['General'])

        # Adding model 'Slide'
        db.create_table('content_slide', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('belongs_to', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('content', ['Slide'])


    def backwards(self, orm):
        # Deleting model 'General'
        db.delete_table('content_general')

        # Deleting model 'Slide'
        db.delete_table('content_slide')


    models = {
        'content.general': {
            'Meta': {'object_name': 'General'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'content.slide': {
            'Meta': {'object_name': 'Slide'},
            'belongs_to': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['content']