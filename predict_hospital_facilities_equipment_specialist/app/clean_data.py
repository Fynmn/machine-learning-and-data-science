import numpy as np
import pandas as pd

def clean_features(dataframe):
    #blood_pressure
    def convert_bp(bp_string):
        ls_bp = bp_string.replace('"', '').split("/")
        print("bb_list: ", ls_bp)
        if int(float(ls_bp[0])) >= 130 | int(float(ls_bp[1])) >= 80:
            return pd.Series([1, 0, 0])
        elif (int(float(ls_bp[0])) >= 90 & int(float(ls_bp[0])) < 130) & (int(float(ls_bp[1])) >= 60 & int(float(ls_bp[1])) < 80):
            return pd.Series([0, 1, 0])
        elif int(float(ls_bp[0])) < 90 | int(float(ls_bp[1])) < 60:
            return pd.Series([0, 0, 1])
        else:
            return pd.Series([0, 0, 0])

    dataframe[['bp_high','bp_normal','bp_low']]=dataframe['blood_pressure'].apply(convert_bp)

    #pulse
    def convert_pulse(num):
        print("PULSE: ", int(num.replace('"', '')))
        if int(num.replace('"', '')) > 100:
            return pd.Series([1, 0, 0])
        elif int(num.replace('"', '')) <= 100 and int(num.replace('"', '')) >= 60:
            return pd.Series([0, 1, 0])
        elif int(num.replace('"', '')) <= 60:
            return pd.Series([0, 0, 1])
        else:
            return pd.Series([0, 0, 0])

    dataframe[['pulse_high','pulse_normal','pulse_low']]=dataframe['pulse_rate'].apply(convert_pulse)

    #resp
    def convert_respiratory(num):
        if int(num.replace('"', '')) > 20:
            return pd.Series([1, 0, 0])
        elif int(num.replace('"', '')) <= 20 and int(num.replace('"', '')) >= 12:
            return pd.Series([0, 1, 0])
        elif int(num.replace('"', '')) < 12:
            return pd.Series([0, 0, 1])
        else:
            return pd.Series([0, 0, 0])


    dataframe[['respiratory_high','respiratory_normal','respiratory_low']]=dataframe['respiratory_rate'].apply(convert_respiratory)

    #spo2
    def convert_spo2(num):
        if int(num.replace('"', '')) <= 100 and int(num.replace('"', '')) >= 95:
            return pd.Series([1, 0])
        elif int(num.replace('"', '')) < 95:
            return pd.Series([0, 1])
        else:
            return pd.Series([0, 0])
    
    dataframe[['spo2_normal','spo2_low']]=dataframe['spo2'].apply(convert_spo2)

    #cbg
    def convert_cbg(num):
        if int(num.replace('"', '')) > 5.6:
            return pd.Series([1, 0, 0])
        elif int(num.replace('"', '')) <= 5.6 and int(num.replace('"', '')) >= 3.9:
            return pd.Series([0, 1, 0])
        elif int(num.replace('"', '')) < 3.9:
            return pd.Series([0, 0, 1])
        else:
            return pd.Series([0, 0, 0])
    
    dataframe[['cbg_high','cbg_normal','cbg_low']]=dataframe['cbg'].apply(convert_cbg)

    #temp
    def convert_temperature(num):
        if float(num.replace('"', '')) > 37.2:
            return pd.Series([1, 0, 0])
        elif float(num.replace('"', '')) <= 37.2 and float(num.replace('"', '')) >= 35.8:
            return pd.Series([0, 1, 0])
        elif float(num.replace('"', '')) < 35.8:
            return pd.Series([0, 0, 1])
        else:
            return pd.Series([0, 0, 0])
    
    dataframe[['temperature_high','temperature_normal','temperature_low']]=dataframe['temperature'].apply(convert_temperature)

    #eye_opening
    def convert_eye_opening(x):
        if x == "Spontaneous":
            return pd.Series([1, 0, 0, 0])
        elif x == "To Voice":
            return pd.Series([0, 1, 0, 0])
        elif x == "To Pain":
            return pd.Series([0, 0, 1, 0])
        elif x == "No Response":
            return pd.Series([0, 0, 0, 1])
        else:
            return pd.Series([0, 0, 0, 0])

    
    dataframe[['eye_opening_spontaneous','eye_opening_tovoice','eye_opening_topain', 'eye_opening_nores']]=dataframe['eye_opening'].apply(convert_eye_opening)

    #verbal
    def convert_verbal(x):
        if x == "Oriented, coos bubbles":
            return pd.Series([1, 0, 0, 0, 0])
        elif x == "Confused, cry":
            return pd.Series([0, 1, 0, 0, 0])
        elif x == "Inappropriate Words":
            return pd.Series([0, 0, 1, 0, 0])
        elif x == "Incomprehensible Sounds":
            return pd.Series([0, 0, 0, 1, 0])
        elif x == "No Response":
            return pd.Series([0, 0, 0, 0, 1])
        else:
            return pd.Series([0, 0, 0, 0, 0])

    
    dataframe[['verbal_or_coos','verbal_con_cry','verbal_in_wo', 'verbal_in_so', 'verbal_nores']]=dataframe['verbal'].apply(convert_verbal)

    #motor
    def convert_motor(x):
        if x == "Obeys Commands":
            return pd.Series([1, 0, 0, 0, 0, 0])
        elif x == "Localizes Pain":
            return pd.Series([0, 1, 0, 0, 0, 0])
        elif x == "Withdraw":
            return pd.Series([0, 0, 1, 0, 0, 0])
        elif x == "Flexion":
            return pd.Series([0, 0, 0, 1, 0, 0])
        elif x == "Extension":
            return pd.Series([0, 0, 0, 0, 1, 0])
        elif x == "No Response":
            return pd.Series([0, 0, 0, 0, 0, 1])
        else:
            return pd.Series([0, 0, 0, 0, 0, 0])

    
    dataframe[['motor_obey','motor_local','motor_withdraw', 'motor_flex', 'motor_ext', 'motor_nores']]=dataframe['motor'].apply(convert_motor)

    # Drop Columns
    dataframe = dataframe.drop(columns='blood_pressure')
    dataframe = dataframe.drop(columns='pulse_rate')
    dataframe = dataframe.drop(columns='respiratory_rate')
    dataframe = dataframe.drop(columns='spo2')
    dataframe = dataframe.drop(columns='cbg')
    dataframe = dataframe.drop(columns='temperature')
    dataframe = dataframe.drop(columns='eye_opening')
    dataframe = dataframe.drop(columns='verbal')
    dataframe = dataframe.drop(columns='motor')

    df2 = dataframe.iloc[:, :121]
    df1 = dataframe.iloc[:, 121:]
    new_dataframe = pd.concat([df1, df2], axis=1)
    
    return new_dataframe


