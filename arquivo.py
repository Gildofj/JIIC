from conexao import MongoConnect
import csv
import json
import pandas as pd
class Arquivo():

    def save(self):

        csvfile = 'C:/Users/junio/PycharmProjects/MotorcycleData.csv'
        data = pd.read_csv(csvfile)
        df = pd.DataFrame(data)
        
        #Limpeza dos dados com o pandas
        df['Condition_Desc'] = df['Condition_Desc'].str.replace("'", "")
        df['Condition_Desc'] = df['Condition_Desc'].str.replace('"', '')
        df['Condition_Desc'] = df['Condition_Desc'].str.replace(',', '')
        df['Condition_Desc'] = df['Condition_Desc'].str.replace('!', '')
        df['Price'] = df['Price'].str.replace('$', '')
        df['Price'] = df['Price'].str.replace(',', '')
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
        df['Mileage'] = df['Mileage'].str.replace(',', '')
        df['Mileage'] = df['Mileage'].str.replace('NA', '')
        df['Mileage'] = df['Mileage'].str.replace('N/A', '')
        df['Mileage'] = df['Mileage'].str.replace('n/a', '')
        df['Mileage'] = pd.to_numeric(df['Mileage'], errors='coerce')
        df['Feedback_Perc'] = df['Feedback_Perc'].str.replace('.', '')
        df['Feedback_Perc'] = df['Feedback_Perc'].str.replace('>', '')
        df['Feedback_Perc'] = pd.to_numeric(df['Feedback_Perc'], errors='coerce')
        df['Watch_Count'] = df['Watch_Count'].str.replace('>', '')

        arrayJSON = {}
        conexao = MongoConnect()
        arrayJSON = df.to_dict("records")
       # arrayJSON = json.dump(df)
        conexao.save(arrayJSON)
