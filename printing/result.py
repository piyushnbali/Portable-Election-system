from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy

nominee_city=["PuneNominee", "NashikNominee", "AurangabadNominee", "AkolaNominee", "BuldanaNominee"]
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///PuneNominee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)




class Nominee(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    candidate=db.Column(db.String(200), nullable=False)
    votes=db.Column(db.Integer, nullable=False, default=0)

Voters=Nominee.query.all()
def do(q):
    global Voters
    for i in nominee_city:
        if (i == q):
            app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{i}.db'
            app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
            Voters=Nominee.query.all()
            return Voters
    else:
        return Voters


def __init__(self, candidate, votes):
    self.candidate=candidate
    self.votes=votes


@app.route('/', methods=['GET', 'POST'])
def result():
    global q
    if request.method == 'POST':
        q = request.form['name']
        if q=="":
            return redirect(url_for('result'))
        return redirect(url_for('resultpage'))
    return render_template('result.html')


@app.route('/resultpage')
def resultpage():
    global q
    return render_template('resultpage.html', Voter=do(q))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True,host='0.0.0.0', port=11000)
