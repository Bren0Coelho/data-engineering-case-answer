"""
Author: Breno Spinelli Coelho
This code was developed to accomplish part 2 of Lablift data engineering case tasks

"""

from flask import Flask, jsonify
import joblib as jb
from part1 import patient_info

app = Flask(__name__)


@app.route('/blood', methods=['GET'])
def first_route():
    return 'Please, type the patient ID as a sequence for the url above', 200


@app.route('/blood/<int:id_patient>', methods=['GET'])
def output(id_patient):
    observation = patient_info(id_patient)
    if not bool(observation):
        return 'Sorry, I could not find this patient', 404

    observation['patient_id'] = id_patient

    # Predicting
    model = jb.load('blood_donation_model.joblib')
    x1 = observation['months_since_last_donation']
    x2 = observation['number_of_donations']
    x3 = observation['total_volume_donated_cc']
    x4 = observation['months_since_first_donation']
    prediction = model.predict([[x1, x2, x3, x4]])
    observation['prediction'] = int(prediction[0])

    return jsonify(observation), 200


if __name__ == '__main__':
    app.run(debug=True)
