# -*- coding: utf-8 -*-
### required - do no delete
from google.appengine.ext import blobstore
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp.util import run_wsgi_app
import uuid
import logging

def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    all_cats = db(db.jobs.category>0).select()
    unique_cats = []
    for cat in all_cats:
        if cat.category not in unique_cats:
            unique_cats.append(cat.category)
    return dict(cats=unique_cats)
def cat():
    all_cats = db(db.jobs.category>0).select()
    unique_cats = []
    for cat in all_cats:
        if cat.category not in unique_cats:
            unique_cats.append(cat.category)
    return dict(cats=unique_cats)

def catlist():
    jobs_in_cat = db(db.jobs.category==request.args[0]).select()
    return dict(jobs_in_cat=jobs_in_cat, category = request.args[0])

def info():
    job = db.jobs[request.args(0)]
    
    form=SQLFORM(db.submissions, fields=['name', 'email', 'resume'])
    form.vars.job = request.args(0)
    if form.process().accepted:
        response.flash = 'Your info has been sent!'
    download = URL('download')
    records = SQLTABLE(db().select(db.submissions.ALL), upload=download, headers='fieldname:capitalize')
    #if not job: raise HTTP(404)
    return dict(job=job, form=form, records=records)

def submissions():
    download = URL('download')
    records = SQLTABLE(db().select(db.submissions.ALL), upload=download, headers='fieldname:capitalize')
    return dict(records=records) 

def submissions2():
    records = db().select(db.submissions.ALL)
    return dict(records=records) 

def error():
    return dict()

def upload():
    pass

def importcsv():
    try:
        if open('data.csv', 'r'):
            db(db.jobs.id>0).delete()
            db.jobs.import_from_csv_file(open('data.csv', 'r'))
            return 'Success'
    except IOError:
        return 'I/O Error'

