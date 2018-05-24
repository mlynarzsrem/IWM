class View:
    def getAllPatientsView(self,patients,count,offset,name=None):
        patientsList=''
        for p in patients:
            patientsList +=self.getSinglePatientRow(p)
        return self.getSearchBar(count,offset),patientsList,self.getSiteChanger(count,offset,name),self.getCountSelector(offset,name)


    def getSinglePatientRow(self,patient):
        link = '/patient/'+str(patient.id)
        id='<td>'+str(patient.id)+'</td>'
        if(patient.birthDate is None):
            birthDate = '<td>Nieznana</td>'
        else:
            birthDate='<td>'+str(patient.birthDate.date)+'</td>'
        gender ='<td>'+str(patient.gender)+'</td>'
        if(patient.name is  None):
            name="<td>Nieznane</td>"
        else:
            name ='<td>'+str(patient.name[0].family)+'</td>'
        if(patient.active is True):
            isActive='Tak'
        else:
            isActive = 'Nie'
        active ='<td>'+isActive+'</td>'
        button = '<td><a href="'+str(link)+'"><button>View data</button></a></td>'
        return '<tr>'+name+id+birthDate+gender+active+button+'</tr>'

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