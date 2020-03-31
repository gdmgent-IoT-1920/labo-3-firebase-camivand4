from sense_hat import SenseHat
import threading
import firebase_admin
from firebase_admin import credentials, firestore
import time

#const
COLLECTION = 'raspberry'
DOCUMENT = 'collectie'

# firebase
cred = credentials.Certificate("../assets/config/firebase_admin.json")
firebase_admin.initialize_app(cred)

# connect to firestore
db = firestore.client()

# sensehat 
sense = SenseHat()
sense.set_imu_config(False, False, False)
sense.clear()

def get_set_value():
    # get value
    temperatuur = round(sense.get_temperature())
    druk = round(sense.get_pressure())
    vochtigheid = round(sense.get_humidity())

    t = temperatuur
    d = druk 
    v = vochtigheid 

    # SET VALUES IN FIREBASE
    pi_ref.update(
        {'enviroment': 
            {
                'temperatuur' : temperatuur,
                'druk' : druk,
                'vochtigheid' : vochtigheid
            }
        },
        )

    sense.show_message("temperature")
    sense.show_message(str(t), text_colour=[255, 100, 100])
    sense.show_message(str(t), text_colour=[255, 100, 100])
    sense.show_message("druk")
    sense.show_message(str(d), text_colour=[255, 100, 100])
    sense.show_message("vochtigheid")
    sense.show_message(str(v), text_colour=[255, 100, 100])
    print("tempature=", t, "pressure=", d, "humidity=", v)
    return [temperatuur, druk, vochtigheid]

# connect firestore
db = firestore.client()
pi_ref = db.collection(COLLECTION).document(DOCUMENT)

# app
while True:
    get_set_value()
    time.sleep(5)