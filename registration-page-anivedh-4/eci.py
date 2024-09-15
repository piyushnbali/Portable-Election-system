from flask import Flask,render_template,url_for,flash,redirect,request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SECRET_KEY']='3248934728947dh34'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)

class Voter(db.Model):
    voter_id = db.Column('voter_id',db.Integer,primary_key=True)
    name = db.Column(db.String(60))
    password = db.Column(db.String(60))
    city= db.Column(db.String(60),default="Pune")

    def __init__(self, name, password, city):
        self.name=name
        self.password=password
        self.city=city




@app.route('/9970384403',methods=['GET','POST'])
def new():
    if request.method=='POST':
        if not request.form['name'] or not request.form['password']:
            flash('Please enter all the fields', 'error')
        else:
            voter = Voter(name=request.form['name'],password=request.form['password'])
            db.session.add(voter)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('new'))
    return render_template('new.html')

@app.route('/')
def show_all():
    return render_template('show_all.html', Voter=Voter.query.all())
if __name__=="__main__":
    db.create_all()
    app.run(debug=True,host="localhost",port=3000)