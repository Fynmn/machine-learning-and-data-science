from flask import Flask, request
import pandas as pd
from app.clean_data import *
from app.load_model import *

app = Flask(__name__)


@app.route('/predict', methods=['GET'])
def predict():
    # Vital Signs
    blood_pressure = request.args.get("blood_pressure")
    pulse = request.args.get("pulse")
    resp = request.args.get("resp")
    spo2 = request.args.get("spo2")
    cbg = request.args.get("cbg")
    temp = request.args.get("temp")

    print("BLOOD PRESSURE BE: ", blood_pressure)
    print("PULSE BE: ", pulse)
    print("RESP BE: ", resp)
    print("SPO2 BE: ", spo2)
    print("CBG BE: ", spo2)
    print("TEMP BE: ", temp)

    # GCS
    eye_opening = request.args.get("eye_opening")
    gcs_verbal = request.args.get("verbal")
    gcs_motor = request.args.get("motor")

    print("Eye opening: ", eye_opening)
    print("Verbal: ", gcs_verbal)
    print("Motor: ", gcs_motor)

    # Physical Assessment
    headneck_pain = request.args.get("headneck_pain", type=int)
    headneck_blunt = request.args.get("headneck_blunt", type=int)
    headneck_deformity = request.args.get("headneck_deformity", type=int)
    headneck_abrasion = request.args.get("headneck_abrasion", type=int)
    headneck_laceration = request.args.get("headneck_laceration", type=int)
    headneck_avulsion = request.args.get("headneck_avulsion", type=int)
    headneck_gunshot = request.args.get("headneck_gunshot", type=int)
    headneck_stab = request.args.get("headneck_stab", type=int)
    headneck_swelling = request.args.get("headneck_swelling", type=int)
    headneck_burns = request.args.get("headneck_burns", type=int)
    headneck_others = request.args.get("headneck_others", type=int)
    facejaw_pain = request.args.get("facejaw_pain", type=int)
    facejaw_blunt = request.args.get("facejaw_blunt", type=int)
    facejaw_deformity = request.args.get("facejaw_deformity", type=int)
    facejaw_abrasion = request.args.get("facejaw_abrasion", type=int)
    facejaw_laceration = request.args.get("facejaw_laceration", type=int)
    facejaw_avulsion = request.args.get("facejaw_avulsion", type=int)
    facejaw_gunshot = request.args.get("facejaw_gunshot", type=int)
    facejaw_stab = request.args.get("facejaw_stab", type=int)
    facejaw_swelling = request.args.get("facejaw_swelling", type=int)
    facejaw_burns = request.args.get("facejaw_burns", type=int)
    facejaw_others = request.args.get("facejaw_others", type=int)
    chestaxillashoulder_pain = request.args.get(
        "chestaxillashoulder_pain", type=int)
    chestaxillashoulder_blunt = request.args.get(
        "chestaxillashoulder_blunt", type=int)
    chestaxillashoulder_deformity = request.args.get(
        "chestaxillashoulder_deformity", type=int)
    chestaxillashoulder_abrasion = request.args.get(
        "chestaxillashoulder_abrasion", type=int)
    chestaxillashoulder_laceration = request.args.get(
        "chestaxillashoulder_laceration", type=int)
    chestaxillashoulder_avulsion = request.args.get(
        "chestaxillashoulder_avulsion", type=int)
    chestaxillashoulder_gunshot = request.args.get(
        "chestaxillashoulder_gunshot", type=int)
    chestaxillashoulder_stab = request.args.get(
        "chestaxillashoulder_stab", type=int)
    chestaxillashoulder_burns = request.args.get(
        "chestaxillashoulder_burns", type=int)
    chestaxillashoulder_others = request.args.get(
        "chestaxillashoulder_others", type=int)
    pelviship_pain = request.args.get("pelviship_pain", type=int)
    pelviship_blunt = request.args.get("pelviship_blunt", type=int)
    pelviship_deformity = request.args.get("pelviship_deformity", type=int)
    pelviship_abrasion = request.args.get("pelviship_abrasion", type=int)
    pelviship_laceration = request.args.get("pelviship_laceration", type=int)
    pelviship_avulsion = request.args.get("pelviship_avulsion", type=int)
    pelviship_gunshot = request.args.get("pelviship_gunshot", type=int)
    pelviship_stab = request.args.get("pelviship_stab", type=int)
    pelviship_swelling = request.args.get("pelviship_swelling", type=int)
    pelviship_burns = request.args.get("pelviship_burns", type=int)
    pelviship_others = request.args.get("pelviship_others", type=int)
    leftarm_pain = request.args.get("leftarm_pain", type=int)
    leftarm_blunt = request.args.get("leftarm_blunt", type=int)
    leftarm_deformity = request.args.get("leftarm_deformity", type=int)
    leftarm_abrasion = request.args.get("leftarm_abrasion", type=int)
    leftarm_laceration = request.args.get("leftarm_laceration", type=int)
    leftarm_avulsion = request.args.get("leftarm_avulsion", type=int)
    leftarm_gunshot = request.args.get("leftarm_gunshot", type=int)
    leftarm_stab = request.args.get("leftarm_stab", type=int)
    leftarm_swelling = request.args.get("leftarm_swelling", type=int)
    leftarm_burns = request.args.get("leftarm_burns", type=int)
    leftarm_others = request.args.get("leftarm_others", type=int)
    rightarm_pain = request.args.get("rightarm_pain", type=int)
    rightarm_blunt = request.args.get("rightarm_blunt", type=int)
    rightarm_deformity = request.args.get("rightarm_deformity", type=int)
    rightarm_abrasion = request.args.get("rightarm_abrasion", type=int)
    rightarm_laceration = request.args.get("rightarm_laceration", type=int)
    rightarm_avulsion = request.args.get("rightarm_avulsion", type=int)
    rightarm_gunshot = request.args.get("rightarm_gunshot", type=int)
    rightarm_stab = request.args.get("rightarm_stab", type=int)
    rightarm_swelling = request.args.get("rightarm_swelling", type=int)
    rightarm_burns = request.args.get("rightarm_burns", type=int)
    rightarm_others = request.args.get("rightarm_others", type=int)
    leftleg_pain = request.args.get("leftleg_pain", type=int)
    leftleg_blunt = request.args.get("leftleg_blunt", type=int)
    leftleg_deformity = request.args.get("leftleg_deformity", type=int)
    leftleg_abrasion = request.args.get("leftleg_abrasion", type=int)
    leftleg_laceration = request.args.get("leftleg_laceration", type=int)
    leftleg_avulsion = request.args.get("leftleg_avulsion", type=int)
    leftleg_gunshot = request.args.get("leftleg_gunshot", type=int)
    leftleg_stab = request.args.get("leftleg_stab", type=int)
    leftleg_swelling = request.args.get("leftleg_swelling", type=int)
    leftleg_burns = request.args.get("leftleg_burns", type=int)
    leftleg_others = request.args.get("leftleg_others", type=int)
    rightleg_pain = request.args.get("rightleg_pain", type=int)
    rightleg_blunt = request.args.get("rightleg_blunt", type=int)
    rightleg_deformity = request.args.get("rightleg_deformity", type=int)
    rightleg_abrasion = request.args.get("rightleg_abrasion", type=int)
    rightleg_laceration = request.args.get("rightleg_laceration", type=int)
    rightleg_avulsion = request.args.get("rightleg_avulsion", type=int)
    rightleg_gunshot = request.args.get("rightleg_gunshot", type=int)
    rightleg_stab = request.args.get("rightleg_stab", type=int)
    rightleg_swelling = request.args.get("rightleg_swelling", type=int)
    rightleg_burns = request.args.get("rightleg_burns", type=int)
    rightleg_others = request.args.get("rightleg_others", type=int)
    backflank_pain = request.args.get("backflank_pain", type=int)
    backflank_blunt = request.args.get("backflank_blunt", type=int)
    backflank_deformity = request.args.get("backflank_deformity", type=int)
    backflank_abrasion = request.args.get("backflank_abrasion", type=int)
    backflank_laceration = request.args.get("backflank_laceration", type=int)
    backflank_avulsion = request.args.get("backflank_avulsion", type=int)
    backflank_gunshot = request.args.get("backflank_gunshot", type=int)
    backflank_stab = request.args.get("backflank_stab", type=int)
    backflank_swelling = request.args.get("backflank_swelling", type=int)
    backflank_burns = request.args.get("backflank_burns", type=int)
    backflank_others = request.args.get("backflank_others", type=int)
    kneehandfoot_pain = request.args.get("kneehandfoot_pain", type=int)
    kneehandfoot_blunt = request.args.get("kneehandfoot_blunt", type=int)
    kneehandfoot_deformity = request.args.get(
        "kneehandfoot_deformity", type=int)
    kneehandfoot_abrasion = request.args.get("kneehandfoot_abrasion", type=int)
    kneehandfoot_laceration = request.args.get(
        "kneehandfoot_laceration", type=int)
    kneehandfoot_avulsion = request.args.get("kneehandfoot_avulsion", type=int)
    kneehandfoot_gunshot = request.args.get("kneehandfoot_gunshot", type=int)
    kneehandfoot_stab = request.args.get("kneehandfoot_stab", type=int)
    kneehandfoot_swelling = request.args.get("kneehandfoot_swelling", type=int)
    kneehandfoot_burns = request.args.get("kneehandfoot_burns", type=int)
    kneehandfoot_others = request.args.get("kneehandfoot_others", type=int)
    leftarm_u = request.args.get("leftarm_u", type=int)
    leftarm_l = request.args.get("leftarm_l", type=int)
    leftarm_j = request.args.get("leftarm_j", type=int)
    rightarm_u = request.args.get("rightarm_u", type=int)
    rightarm_l = request.args.get("rightarm_l", type=int)
    rightarm_j = request.args.get("rightarm_j", type=int)
    leftleg_u = request.args.get("leftleg_u", type=int)
    leftleg_l = request.args.get("leftleg_l", type=int)
    leftleg_j = request.args.get("leftleg_j", type=int)
    rightleg_u = request.args.get("rightleg_u", type=int)
    rightleg_l = request.args.get("rightleg_l", type=int)
    rightleg_j = request.args.get("rightleg_j", type=int)

    features_columns = ["blood_pressure",
                        "pulse_rate",
                        "respiratory_rate",
                        "spo2",
                        "cbg",
                        "temperature",
                        "eye_opening",
                        "verbal",
                        "motor",
                        "pa_headneck_pain",
                        "pa_headneck_blunt",
                        "pa_headneck_deformity",
                        "pa_headneck_abrasion",
                        "pa_headneck_laceration",
                        "pa_headneck_avulsion",
                        "pa_headneck_gunshot",
                        "pa_headneck_stab",
                        "pa_headneck_swelling",
                        "pa_headneck_burns",
                        "pa_headneck_others",
                        "pa_facejaw_pain",
                        "pa_facejaw_blunt",
                        "pa_facejaw_deformity",
                        "pa_facejaw_abrasion",
                        "pa_facejaw_laceration",
                        "pa_facejaw_avulsion",
                        "pa_facejaw_gunshot",
                        "pa_facejaw_stab",
                        "pa_facejaw_swelling",
                        "pa_facejaw_burns",
                        "pa_facejaw_others",
                        "pa_chestaxillashoulder_pain",
                        "pa_chestaxillashoulder_blunt",
                        "pa_chestaxillashoulder_deformity",
                        "pa_chestaxillashoulder_abrasion",
                        "pa_chestaxillashoulder_laceration",
                        "pa_chestaxillashoulder_avulsion",
                        "pa_chestaxillashoulder_gunshot",
                        "pa_chestaxillashoulder_stab",
                        "pa_chestaxillashoulder_burns",
                        "pa_chestaxillashoulder_others",
                        "pa_pelviship_pain",
                        "pa_pelviship_blunt",
                        "pa_pelviship_deformity",
                        "pa_pelviship_abrasion",
                        "pa_pelviship_laceration",
                        "pa_pelviship_avulsion",
                        "pa_pelviship_gunshot",
                        "pa_pelviship_stab",
                        "pa_pelviship_swelling",
                        "pa_pelviship_burns",
                        "pa_pelviship_others",
                        "pa_leftarm_pain",
                        "pa_leftarm_blunt",
                        "pa_leftarm_deformity",
                        "pa_leftarm_abrasion",
                        "pa_leftarm_laceration",
                        "pa_leftarm_avulsion",
                        "pa_leftarm_gunshot",
                        "pa_leftarm_stab",
                        "pa_leftarm_swelling",
                        "pa_leftarm_burns",
                        "pa_leftarm_others",
                        "pa_rightarm_pain",
                        "pa_rightarm_blunt",
                        "pa_rightarm_deformity",
                        "pa_rightarm_abrasion",
                        "pa_rightarm_laceration",
                        "pa_rightarm_avulsion",
                        "pa_rightarm_gunshot",
                        "pa_rightarm_stab",
                        "pa_rightarm_swelling",
                        "pa_rightarm_burns",
                        "pa_rightarm_others",
                        "pa_leftleg_pain",
                        "pa_leftleg_blunt",
                        "pa_leftleg_deformity",
                        "pa_leftleg_abrasion",
                        "pa_leftleg_laceration",
                        "pa_leftleg_avulsion",
                        "pa_leftleg_gunshot",
                        "pa_leftleg_stab",
                        "pa_leftleg_swelling",
                        "pa_leftleg_burns",
                        "pa_leftleg_others",
                        "pa_rightleg_pain",
                        "pa_rightleg_blunt",
                        "pa_rightleg_deformity",
                        "pa_rightleg_abrasion",
                        "pa_rightleg_laceration",
                        "pa_rightleg_avulsion",
                        "pa_rightleg_gunshot",
                        "pa_rightleg_stab",
                        "pa_rightleg_swelling",
                        "pa_rightleg_burns",
                        "pa_rightleg_others",
                        "pa_backflank_pain",
                        "pa_backflank_blunt",
                        "pa_backflank_deformity",
                        "pa_backflank_abrasion",
                        "pa_backflank_laceration",
                        "pa_backflank_avulsion",
                        "pa_backflank_gunshot",
                        "pa_backflank_stab",
                        "pa_backflank_swelling",
                        "pa_backflank_burns",
                        "pa_backflank_others",
                        "pa_kneehandfoot_pain",
                        "pa_kneehandfoot_blunt",
                        "pa_kneehandfoot_deformity",
                        "pa_kneehandfoot_abrasion",
                        "pa_kneehandfoot_laceration",
                        "pa_kneehandfoot_avulsion",
                        "pa_kneehandfoot_gunshot",
                        "pa_kneehandfoot_stab",
                        "pa_kneehandfoot_swelling",
                        "pa_kneehandfoot_burns",
                        "pa_kneehandfoot_others",
                        "pa_leftarm_u",
                        "pa_leftarm_l",
                        "pa_leftarm_j",
                        "pa_rightarm_u",
                        "pa_rightarm_l",
                        "pa_rightarm_j",
                        "pa_leftleg_u",
                        "pa_leftleg_l",
                        "pa_leftleg_j",
                        "pa_rightleg_u",
                        "pa_rightleg_l",
                        "pa_rightleg_j"]

    features_values = [[blood_pressure,
                        pulse,
                        resp,
                        spo2,
                        cbg,
                        temp,
                        eye_opening,
                        gcs_verbal,
                        gcs_motor,
                        headneck_pain,
                        headneck_blunt,
                        headneck_deformity,
                        headneck_abrasion,
                        headneck_laceration,
                        headneck_avulsion,
                        headneck_gunshot,
                        headneck_stab,
                        headneck_swelling,
                        headneck_burns,
                        headneck_others,
                        facejaw_pain,
                        facejaw_blunt,
                        facejaw_deformity,
                        facejaw_abrasion,
                        facejaw_laceration,
                        facejaw_avulsion,
                        facejaw_gunshot,
                        facejaw_stab,
                        facejaw_swelling,
                        facejaw_burns,
                        facejaw_others,
                        chestaxillashoulder_pain,
                        chestaxillashoulder_blunt,
                        chestaxillashoulder_deformity,
                        chestaxillashoulder_abrasion,
                        chestaxillashoulder_laceration,
                        chestaxillashoulder_avulsion,
                        chestaxillashoulder_gunshot,
                        chestaxillashoulder_stab,
                        chestaxillashoulder_burns,
                        chestaxillashoulder_others,
                        pelviship_pain,
                        pelviship_blunt,
                        pelviship_deformity,
                        pelviship_abrasion,
                        pelviship_laceration,
                        pelviship_avulsion,
                        pelviship_gunshot,
                        pelviship_stab,
                        pelviship_swelling,
                        pelviship_burns,
                        pelviship_others,
                        leftarm_pain,
                        leftarm_blunt,
                        leftarm_deformity,
                        leftarm_abrasion,
                        leftarm_laceration,
                        leftarm_avulsion,
                        leftarm_gunshot,
                        leftarm_stab,
                        leftarm_swelling,
                        leftarm_burns,
                        leftarm_others,
                        rightarm_pain,
                        rightarm_blunt,
                        rightarm_deformity,
                        rightarm_abrasion,
                        rightarm_laceration,
                        rightarm_avulsion,
                        rightarm_gunshot,
                        rightarm_stab,
                        rightarm_swelling,
                        rightarm_burns,
                        rightarm_others,
                        leftleg_pain,
                        leftleg_blunt,
                        leftleg_deformity,
                        leftleg_abrasion,
                        leftleg_laceration,
                        leftleg_avulsion,
                        leftleg_gunshot,
                        leftleg_stab,
                        leftleg_swelling,
                        leftleg_burns,
                        leftleg_others,
                        rightleg_pain,
                        rightleg_blunt,
                        rightleg_deformity,
                        rightleg_abrasion,
                        rightleg_laceration,
                        rightleg_avulsion,
                        rightleg_gunshot,
                        rightleg_stab,
                        rightleg_swelling,
                        rightleg_burns,
                        rightleg_others,
                        backflank_pain,
                        backflank_blunt,
                        backflank_deformity,
                        backflank_abrasion,
                        backflank_laceration,
                        backflank_avulsion,
                        backflank_gunshot,
                        backflank_stab,
                        backflank_swelling,
                        backflank_burns,
                        backflank_others,
                        kneehandfoot_pain,
                        kneehandfoot_blunt,
                        kneehandfoot_deformity,
                        kneehandfoot_abrasion,
                        kneehandfoot_laceration,
                        kneehandfoot_avulsion,
                        kneehandfoot_gunshot,
                        kneehandfoot_stab,
                        kneehandfoot_swelling,
                        kneehandfoot_burns,
                        kneehandfoot_others,
                        leftarm_u,
                        leftarm_l,
                        leftarm_j,
                        rightarm_u,
                        rightarm_l,
                        rightarm_j,
                        leftleg_u,
                        leftleg_l,
                        leftleg_j,
                        rightleg_u,
                        rightleg_l,
                        rightleg_j]]

    df = pd.DataFrame(features_values, columns=features_columns)
    cleaned_features = clean_features(df)
    predicted_labels = predict_labels(cleaned_features.values)

    # print("PREDICTED: ", predicted_labels)

    return {'predicted': predicted_labels}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50100, debug=True)
