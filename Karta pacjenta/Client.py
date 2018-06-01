import urllib.request
import json
import fhirclient.models.bundle as b
import fhirclient.models.patient as p
import fhirclient.models.observation as o
import fhirclient.models.medicationstatement as ms
class Client:

    def getPatientById(self,id):
        url ="http://hapi.fhir.org/baseDstu3/Patient/"+str(id)
        contents = urllib.request.urlopen(url).read()
        js = json.loads(contents.decode("utf-8"))
        return p.Patient(js)
    def getObservationById(self,id):
        url ="http://hapi.fhir.org/baseDstu3/Observation/"+str(id)
        contents = urllib.request.urlopen(url).read()
        js = json.loads(contents.decode("utf-8"))
        return o.Observation(js)
    def getMedicationStatement(self,id):
        url ="http://hapi.fhir.org/baseDstu3/MedicationStatement/"+str(id)
        contents = urllib.request.urlopen(url).read()
        js = json.loads(contents.decode("utf-8"))
        return ms.MedicationStatement(js)
    def getAllPatients(self,count=7,offset=3,family=""):
        contents = urllib.request.urlopen("http://hapi.fhir.org/baseDstu3/Patient?family=" + str(family) + "&_getpagesoffset=" + str(offset) + "&_count=" + str(count) + "&_pretty=true").read()
        js = json.loads(contents.decode("utf-8"))
        bundle = b.Bundle(js)
        patients = []
        if(bundle.entry is None):
            return []
        for entry in bundle.entry:
            patients.append(entry.resource)
        return patients
    def getItemsForPatient(self,id,what="MedicationStatement"):
        url ="http://hapi.fhir.org/baseDstu3/"+what+"?patient="+str(id)+"&_pretty=true"
        contents = urllib.request.urlopen(url).read()
        js = json.loads(contents.decode("utf-8"))
        bundle = b.Bundle(js)
        items =[ ]
        if(bundle.entry is None):
            return []
        for entry in bundle.entry:
            items.append(entry.resource)
        return items
