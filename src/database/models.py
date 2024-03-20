import peewee as pw

db = pw.SqliteDatabase("src/database/sqlitedb.db")


class Help(pw.Model):
    id_ = pw.IntegerField(column_name="id", primary_key=True)
    command = pw.TextField(null=False)
    description = pw.TextField(default="No description")

    class Meta:
        database = db
