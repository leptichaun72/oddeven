import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, \
	render_template

project_dir = os.path.dirname(os.path.abspath(__file__))
db_file = "sqlite:///{}".format(os.path.join(project_dir, "foo.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_file
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
db = SQLAlchemy(app)

class OddEven(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	typename = db.Column(db.Text)

	def __repr__(self):
		return "<ODDEVEN nametype is %r>" % self.typename

class Counting(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	odd_even_id = db.Column(db.Integer,db.ForeignKey("odd_even.id"),nullable=False)
	textform = db.Column(db.String(25))

	def __repr__(self):
		return "<COUNTING number is %r>" % self.textform

@app.route('/')
def index():
    return 'hello'

@app.route('/loop')
def loopy():
	all_odds = Counting.query.filter_by(odd_even_id=1).all()
	return render_template('index.jade',numbahs=all_odds)

app.run(debug=True)

