from conexao import MongoConnect
import csv
import json
import pandas as pd
import sys, getopt, pprint
class Arquivo():

    def save(self):

        csvfile = 'C:/Users/junio/PycharmProjects/MotorcycleData.xlsx'
        # header = ['Condition', 'Condition_Desc', 'Price', 'Location', 'Model_Year', 'Mileage', 'Exterior_Color', 'Make',
        #           'Warranty', 'Model', 'Sub_Model', 'Type', 'Vehicle_Title', 'OBO', 'Feedback_Perc', 'Watch_Count',
        #          'N_Reviews', 'Seller_Status', 'Vehicle_Tile', 'Auction', 'Buy_Now', 'Bid_Count']
        
        arrayJSON = {}
        conexao = MongoConnect()
        data = pd.read_excel(csvfile)
        dataframe = pd.DataFrame(data)
        arrayJSON = dataframe.to_dict("records")
       # arrayJSON = json.dump(df)
        conexao.save(arrayJSON)
