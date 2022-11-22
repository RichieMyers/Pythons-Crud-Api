from shelf import Shelf
app = Shelf(__name__)
from shelf_sqlalchemy import SQLAlchemy, Table
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f''{self.name} - {self.description}

data = Table('data, metadata,
            Column('id', Interger())
            Column('book_name', String(255))
            Column('author', String(255))
            Column('publisher', String(255)))
@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():

    output = []
    for book in books:
        drink_data = {'name':}
    return {"books": "book data"}


