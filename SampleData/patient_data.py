
class Patient:
    def __init__(self,name : str,pincode : int,phoneNumber : str,is_corona : bool):
        self.name = name
        self.pincode = pincode
        self.phoneNumber = phoneNumber
        self.is_corona = is_corona
    
    def getName(self):
        return self.name
    def getPincode(self):
        return self.pincode
    def getPhoneNumber(self):
        return self.phoneNumber
    def getls_corona(self):
        return self.is_corona

class CoronaPatient:
    def __init__(self):
        self.patients = []

    def addPatent(self,newPatient):
        self.patients.append(newPatient)
        return self.patients

    def getLessCases(self):
        dictionary = {}
        for data in self.patients:
            if data['is_corona'] == True:
                dictionary[data['pincode']] = dictionary.get(data['pincode'],0) + 1
        default_values = dictionary.values()
        value = min(list(default_values))
        pincode = []
        for key in dictionary:
            if value == dictionary[key]:
                pincode.append(key)
        return pincode
    
        

obj = Patient(name="thanseef",pincode=676504,phoneNumber="6282741696",is_corona=False)

# print(obj.getPincode())


obj2 = CoronaPatient()

new_patient_inserted =obj2.addPatent(newPatient={"name":"thanseef",
                           "pincode":676504,
                           "phoneNumber" : "6282741696",
                           "is_corona": False})

# print(f"new_patient_inserted : {new_patient_inserted}")

new_patient_inserted_two =obj2.addPatent(newPatient={"name":"San",
                           "pincode":676509,
                           "phoneNumber" : "6282741694",
                           "is_corona": True})

new_patient_inserted_t2 =obj2.addPatent(newPatient={"name":"Manu",
                           "pincode":676509,
                           "phoneNumber" : "6282741693",
                           "is_corona": True})
new_patient_inserted_tw3 =obj2.addPatent(newPatient={"name":"Shafeer",
                           "pincode":676501,
                           "phoneNumber" : "6282741692",
                           "is_corona": True})
new_patient_inserted_tw6 =obj2.addPatent(newPatient={"name":"dds",
                           "pincode":676500,
                           "phoneNumber" : "6282741692",
                           "is_corona": True})

new_patient_inserted_three =obj2.addPatent(newPatient={"name":"Sam",
                           "pincode":676504,
                           "phoneNumber" : "6282741698",
                           "is_corona": True})

new_patient_inserted_four =obj2.addPatent(newPatient={"name":"Jhon",
                           "pincode":676504,
                           "phoneNumber" : "6282741691",
                           "is_corona": True})
new_patient_inserted_four =obj2.addPatent(newPatient={"name":"noonu",
                           "pincode":676504,
                           "phoneNumber" : "6282741691",
                           "is_corona": True})

# print(f"full Patients Data : {new_patient_inserted_four}")

print(obj2.getLessCases())


