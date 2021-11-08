from mysite import db


class Poem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(128), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text(256))

    def __repr__(self):
        return f'{self.author} "{self.title}"'
