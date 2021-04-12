"""
Author: Breno Spinelli Coelho
This code was developed to accomplish part 1 of Lablift data engineering case tasks
"""
import datetime
import pandas as pd


# Function requested
def patient_info(id_number):
    """
    This function builds a dictionary with the following keys:
    - months_since_last_donation
    - number_of_donations
    - total_volume_donated_cc
    - months_since_first_donation
    From blood_donation_hist.csv archive

    :param id_number: string that idenfies the patient
    :return  patient_dic: dictionary with informations of the patient
    """

    # Read csv file
    filename = 'blood_donation_hist.csv'
    patient_dic = {}
    data = pd.read_csv(filename)

    # Current date
    today = datetime.datetime.now()

    # Find patient
    patient_found = data['patient_id'] == id_number
    patient = data[patient_found]

    # If patient not found
    try:
        first_don = datetime.datetime.strptime(patient['donation_date'].values[0], '%Y-%m-%d')
    except IndexError:
        print("Sorry, I could not find this patient")
        return

    # Convert string from csv to datetime. Obs: 'first_donation' comes from try/except
    last_don = datetime.datetime.strptime(patient['donation_date'].values[-1], '%Y-%m-%d')

    # Write in dictionary
    patient_dic['months_since_last_donation'] = (today.year-last_don.year)*12 + today.month - last_don.month
    patient_dic['number_of_donations'] = len(patient['patient_id'])
    patient_dic['total_volume_donated_cc'] = sum(patient['volume_donated_cc'])
    patient_dic['months_since_first_donation'] = (today.year-first_don.year)*12 + today.month - first_don.month

    return patient_dic


id_number = int(input('Please, type a patient ID: '))
print(patient_info(id_number))

