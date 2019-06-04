from pymongo import MongoClient

#pip install pymongo

class MongoConnect():

    def save(self, json):
        try:
            cliente = MongoClient('localhost', 27017)
            banco = cliente.aula_aberta
            JIIC = banco.JIIC
            arq_mongo = JIIC.insert_many(json)
        except Exception as e:
            print("problema ao salvar registro")
            print(json)
            print(e)