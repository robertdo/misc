try:
    if open('data.csv', 'r'):
        db(db.jobs.id>0).delete()
        db.jobs.import_from_csv_file(open('data.csv', 'r'))
except IOError:
    pass