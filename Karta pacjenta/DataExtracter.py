

class MyPatient:
    def __init__(self,patient):
        self.link = '/patient/'+str(patient.id)
        self.id ='<td>'+str(patient.id) +'</td>'
        #Get birthday
        if(patient.birthDate is None):
            self.birthDate = '<td>Nieznana</td>'
        else:
            self.birthDate='<td>'+str(patient.birthDate.date)+'</td>'
        self.gender ='<td>'+str(patient.gender)+'</td>'
        #Get patient name
        if(patient.name is  None):
            self.name="<td>Nieznane</td>"
        else:
            self.name ='<td>'+str(patient.name[0].family)+'</td>'
        #Check if is active
        if(patient.active is True):
            isActive='Tak'
        else:
            isActive = 'Nie'
        self.active ='<td>'+isActive+'</td>'
        #Telecom
        if(patient.telecom is None):
            self.telecom = '<td>Nieznana</td>'
        else:
            self.telecom='<td>'+str(patient.telecom)+'</td>'
        #Adress
        if(patient.address is None):
            self.address = '<td>Nieznana</td>'
        else:
            self.address='<td>'+str(patient.address)+'</td>'
        #deceased
        if(patient.deceasedBoolean is True):
            isdeceased='Tak'
        else:
            isdeceased = 'Nie'
        self.deceased = '<td>'+isdeceased+'</td>'
        #Telecom
        #Martial status
        if(patient.maritalStatus is None):
            self.maritalStatus = '<td>Nieznana</td>'
        else:
            self.maritalStatus='<td>'+str(patient.maritalStatus)+'</td>'

class MyObservation:
    def __init__(self,obs):
        self.type ="<td>Observation</td>"
        self.id ='<td>'+str(obs.id)+'</td>'
        self.date =obs.effectiveDateTime.date;
        self.dateRow = '<td>'+str(self.date)+'</td>'
        self.value = '<td>'+str(obs.valueQuantity.value)+'</td>'
        self.unit = '<td>'+str(obs.valueQuantity.unit)+'</td>'
        self.obsType = obs.code.text
        self.code = '<td>'+str(obs.code.text)+'</td>'
        self.category = '<td>' + str(obs.category) + '</td>'
        self.link = '/observation/' + str(obs.id)
        self.status = '<td>'+str(obs.status)+'</td>'

class MyMedicationStatement:
    def __init__(self,med):
        self.id = '<td>' + str(med.id) + '</td>'
        self.type = "<td>MedicationStatement</td>"
        self.status = med.status
        self.link = '/medstate/' + str(med.id)
        self.status = '<td>'+med.status+'</td>'
        self.taken = '<td>'+med.taken+'</td>'
        if (med.medicationCodeableConcept is not None):
            self.code = '<td>' + med.medicationCodeableConcept.text + '</td>'
        else:
            self.code = '<td>No data</td>'
        if(med.dosage[0] is not None):
            self.dosage = '<td>'+med.dosage[0].text+'</td>'
            self.value = '<td>'+str(med.dosage[0].doseQuantity.value)+'</td>'
            self.unit = '<td>' + str(med.dosage[0].doseQuantity.unit) + '</td>'
        else:
            self.dosage = '<td>No data</td>'
            self.code = '<td>No data</td>'
            self.value =  '<td>No data</td>'
            self.unit =  '<td>No data</td>'
