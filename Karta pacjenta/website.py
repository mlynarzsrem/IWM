from flask import Flask, session, redirect, render_template_string,render_template,request,Markup
from Client import Client
from View import View

app = Flask(__name__)
app.secret_key = 'super secret key'
client = Client()
view = View()

@app.route('/')
def start_page():
    patients = client.getAllPatients(count=30)
    searchbar,list,schanger ,cSelector= view.getAllPatientsView(patients,30,1)
    return render_template('index.html',searchbar=Markup(searchbar),list=Markup(list),changer=Markup(schanger),cSelector=Markup(cSelector))


@app.route('/patients/')
def getAllPatients():
    name = request.args.get("name")
    count = request.args.get("count")
    offset = request.args.get("offset")
    patients = client.getAllPatients(count=count,family=name,offset=offset)
    searchbar, list,schanger ,cSelector= view.getAllPatientsView(patients, count=count, offset=offset)
    return render_template('index.html', searchbar=Markup(searchbar), list=Markup(list),changer=Markup(schanger),cSelector=Markup(cSelector))

@app.route('/patient/<id>')
def getPatientData(id):
    return ''
if __name__ == '__main__':
    app.run()
