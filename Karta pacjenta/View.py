from DataExtracter import MyPatient,MyObservation,MyMedicationStatement
class View:
    def getAllPatientsView(self,patients,count,offset,name=None):
        patientsList=''
        for p in patients:
            patientsList +=self.getSinglePatientRow(p)
        return self.getSearchBar(count,offset),patientsList,self.getSiteChanger(count,offset,name),self.getCountSelector(offset,name)


    def getSinglePatientRow(self,patient,patientView=False):
        mp = MyPatient(patient)
        if(patientView ==False):
            button = '<td><a href="'+str(mp.link)+'"><button>View data</button></a></td>'
            return '<tr>'+mp.name+mp.id+mp.birthDate+mp.gender+mp.active+button+'</tr>'
        else:
            return '<tr>'+mp.id+mp.active+mp.name+mp.telecom+mp.gender+mp.birthDate+mp.deceased+mp.address,mp.maritalStatus+'</tr>'

    def getSearchBar(self,count,offset):
        form ='<form action="/patients"> <input type="text" name="name">\
        <input style="display: None;" value ='+str(count)+' type="text" name="count">'\
        '<input style="display: None;"value ='+str(0)+' type="text" name="offset">'\
        '<input type="submit"></form>'
        return form

    def getSiteChanger(self,count,offset,name):
        count = int(count)
        offset = int(offset)
        toSearch=''
        if(name is not None):
            toSearch=name
        linkPrev =''
        if(offset -count>=0):
            linkPrev='<a href="/patients/?name='+str(toSearch)+'&count='+str(count)+'&offset='+str(offset - count)+'">Poprzedni</a>   '
        linkNext = '<a href="/patients/?name='+str(toSearch)+'&count='+str(count)+'&offset='+str(offset +count)+'">Następny</a>'
        return '<div>'+linkPrev+linkNext+'</div>'

    def getCountSelector(self,offset,name):
        toSearch=''
        if(name is not None):
            toSearch=name
        link ='/patients'
        form ='<form action = "'+link+'" id = "countSelector" > \
            <input style="display: None;" value ="'+str(toSearch)+'" type="text" name="name"> \
            <input style="display: None;" value =' + str(offset) + ' type="text" name="offset"> \
            <input type = "submit" ></form>'
        return form


    def getTimeline(self,items):
        timeline=''
        for it in items:
            itType = it.type
            link = it.link
            date =it.dateRow
            button = '<td><a href="' + str(link) + '"><button>View data</button></a></td>'
            timeline+="<tr>"+date+itType+button+"</tr>\n"
        return timeline
    def getPatientView(self,patient,obs):
        patientInfo = self.getSinglePatientRow(patient,True)
        myObs = [MyObservation(o) for o in obs]
        button = '<td><a href="/medstate/' + str(patient.id) + '"><button>View data</button></a></td>'
        return patientInfo,self.getTimeline(myObs),button

    def getObservationView(self,observation):
        obs = MyObservation(observation)
        return '<tr>'+obs.id+obs.status+obs.dateRow+obs.category+obs.value+obs.unit+obs.code+'</tr>'

    def getMedicationView(self,meds):
        myMeds = [MyMedicationStatement(m) for m in meds]
        table=''
        for myMed in myMeds:
            table+="<tr>"+myMed.id+myMed.status+myMed.code+myMed.dosage+myMed.value+myMed.unit+myMed.taken+"</tr>\n"
        return table