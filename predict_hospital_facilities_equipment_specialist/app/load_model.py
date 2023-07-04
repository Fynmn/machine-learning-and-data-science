import joblib
import pandas as pd

def predict_labels(df_values):

    # converting the feature values into a dataframe
    df = pd.DataFrame(df_values)

    # loading the exported model
    m_jlib = joblib.load('./app/model_jlib')

    # check prediction
    pred = m_jlib.predict(df)

    labels = ['burn_unit', 'operating_room_complex', 'emergency_room_complex', 'coronary_care_unit', 'cardiology', 'surgery', 'pulmonology', 'neurology', 'critical_unit', 'thoraco_cardiovascular_surgery', 'open_heart_surgery', 'endocrinology', 'allergology', 'toxicology', 'delivery_room', 
    'nursery_room', 'post_anesthesia_care_unit', 'animal_bite_center', 'defribilators', 'patient_monitor', 'anesthesia_machines', 'strilizers', 'ekg_ecg_machines', 'surgical_tables', 'blanket_and_fluid_warmers', 'electrosurgical_units', 'x_ray', 'mri', 'ct_scan', 'ultrasound', 'hematology_analyzer', 'biochemistry_analyzer', 'ventilator', 'infusion_pump', 'opthalmologist', 'obstetrician', 'cardiologist', 'endocrinologist', 'gastroenterologist', 'nephrologist', 'urologist', 'pulmonologist', 'otolaryngologist', 'neurologist', 'psychiatrist', 'oncologist', 'radiologist', 'rheumatologist', 'general_surgeon', 'orthopedic_surgeon', 'cardiac_surgeons', 'anesthesiologist']
    label_dict = dict()

    for num, i in enumerate(labels):
        label_dict[num] = i

    label_tbl = list()

    for label in pred.toarray():
        temp = list()
        for i in range(len(label)):
            if(label[i] == 1): temp.append(labels[i])
        label_tbl.append(temp)

    return label_tbl