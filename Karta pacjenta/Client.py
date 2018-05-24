from fhirclient import client
import fhirclient.models.patient as p
import urllib.request
import json
import fhirclient.models.medicationstatement as medSt
import fhirclient.models.observation as obs
import fhirclient.models.medication as med
import fhirclient.models.bundle as b
class Client:
    def __init__(self):
        self.settings = {
            'app_id': 'my_web_app',
            'api_base': 'http://hapi.fhir.org/baseDstu3'
        }
        self.smart = client.FHIRClient(settings=self.settings)

    def getPatientById(self,id):
        patient =  p.Patient.read(str(id),self.smart)
        return patient
    def getAllPatients(self,count=7,offset=3,family=""):
        contents = urllib.request.urlopen("http://hapi.fhir.org/baseDstu3/Patient?family="+str(family)+"&_getpagesoffset="+str(offset)+"&_count="+str(count)+"&_pretty=true").read()
        js = json.loads(contents)
        bundle = b.Bundle(js)
        patients = []
        if(bundle.entry is None):
            return []
        for entry in bundle.entry:
            patients.append(entry.resource)
        return patients

