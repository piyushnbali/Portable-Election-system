from flask import Flask, render_template, url_for, flash, redirect, request

from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'

app.config['SECRET_KEY']='3248934728947dh34'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db=SQLAlchemy(app)


class Voter(db.Model):
    voter_id=db.Column('voter_id', db.Integer, primary_key=True)



    name=db.Column(db.Integer)
    password=db.Column(db.String(60))
    ballot_paper_index=db.Column(db.String)
    city=db.Column(db.String(60), default="Pune")



def __init__(self, name, password, ballot_paper_index, city):
    self.name=name

    self.password=password

    self.ballot_paper_index=ballot_paper_index

    self.city=city

@app.route('/')



def show_all():


    return render_template('eicshow_all.html', Voter=Voter.query.all())








@app.route('/eicnew', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':



        if not request.form['name'] or not request.form['passwd'] or not request.form['bid']:

            flash('Please enter all the fields', 'error')



        else:


            voter=Voter(name=request.form['name'], password=request.form['passwd'],
                        ballot_paper_index=request.form['bid'])

            db.session.add(voter)

            db.session.commit()

            flash('Record was successfully added')

            return redirect(url_for('show_all'))

            return redirect('/')

    return render_template('eicnew.html')


if __name__ == "__main__":
    db.create_all()

    app.run(debug=True,host="localhost",port=4000)
