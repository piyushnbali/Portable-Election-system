from flask import Flask, render_template, url_for, request, redirect

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'

db=SQLAlchemy(app)

data={1:'PuneNominee',2:'AkolaNominee',3:'AurangabadNominee',4:'BuldanaNominee',5:'NashikNominee'}

voterid = 0
bid=-1
class Voter(db.Model):
    voter_id = db.Column('voter_id',db.Integer,primary_key=True)
    name = db.Column(db.Integer)
    password = db.Column(db.String(60))
    ballot_paper_index = db.Column(db.String)
    city=db.Column(db.String(60), default="Pune")
    def __repr__(self):

        return "<name %r>" %self.name
class Nominee(db.Model):
    
    id=db.Column(db.Integer, primary_key=True)

    candidate=db.Column(db.String(200), nullable=False)

    votes=db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):

        return "<candidate %r>" %self.candidate

@app.route("/votenow", methods=['POST','GET'])
def votenow():
    global voterid
    if voterid == 0:
        print(voterid)
        return render_template('votenow.html', voterid = voterid)
    else:
        print(voterid)
        voterid = 0
        return redirect('/index')
        

@app.route('/index')
def voting():
    global bid
    if bid!=-1:
        i=data[bid]
        app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///{}.db".format(i)
        app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
        #Nominee().bind_key(bid)
        k=Nominee.query.all()
        return render_template('index.html', tasks=k)
    else:
        return redirect('/votenow')
    #persons=Nominee.query.all()
    

@app.route("/thank/<int:id>", methods = ['POST','GET'])
def thank(id):
    task = Nominee.query.get_or_404(id)
    task.votes=task.votes + 1
    db.session.commit()
    return render_template('votenow.html', voterid = voterid)

@app.route("/proceed",methods=['POST','GET'])
def proceed():
    global voterid
    global bid
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
    if request.method=="POST":

        voterid = request.form.get('voterid')
        task=Voter.query.all()
        flag=0
        for t in task:
            if t.name==voterid:
                flag=1
                bid=int(t.ballot_paper_index)

        if flag==0:
            bid=-1
            return redirect('/proceed')

    

    return render_template('proceed.html')
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=7000)
#host="192.168.43.94"
