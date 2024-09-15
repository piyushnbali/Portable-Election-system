from flask import Flask,render_template,url_for,flash,redirect,request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SECRET_KEY']='3248934728947dh34'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)

class Voter(db.Model):
    voter_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Integer)
    password = db.Column(db.String(60))
    city=db.Column(db.String(60), default="Pune")

    def __repr__(self):
        return "Voter({},{},{})".format(self.name,self.password,self.city)

@app.route('/dropdown')
def dropdown():
    return render_template('ade.html')

@app.route('/',methods=['GET','POST'])
def new():
    if request.method=='POST':
        if not request.form['name'] or not request.form['passwd']:
            flash('Please enter all the fields', 'error')
        else:
            n=request.form['name']
            p=request.form['passwd']
            voter = Voter(name=n,password=p)
            list1=Voter.query.all()
            f=0
            for l in list1:
                if l.name==n and l.password==p:
                    f=1
                    break
            if f:
                return redirect(url_for('dropdown'))
            else:
                flash("Wrong password")
    return render_template('new.html')
if __name__=="__main__":
    db.create_all()
    app.run(debug=True)