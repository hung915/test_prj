# test_prj
# hehe
`$env:FLASK_APP = "app.py"`  (Windows power shell)

`set FLASK_APP=app.py` (Windows CMD)

`export FLASK_APP=app.py` (Linux/Mac)

`flask db init`

`flask db migrate -m "..."`

`flask db upgrade` (perform update table)

db.relationship (expects a class name)

db.ForeignKey (expects table name)

backref (back reference name | what ever name)

Address.query.filter(and_(Address.person_id==1, Address.email=='def'))