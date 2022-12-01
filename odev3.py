from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd
#Esref Erdal 02195076034
app = Flask(__name__)
api = Api(app)

class veri(Resource):
    def get(self):
        data = pd.read_csv('veri.csv')
        data = data.to_dict('records')
        return {'data': data}, 200

    def post(self):
        taban = request.args['taban']
        yukseklik = request.args['yukseklik']
        ustkenar = request.args['ustkenar']
        sagkenar = request.args['sagkenar']

        kare=>taban = yukseklik = ustkenar = sagkenar
        data = pd.read_csv('veri.csv')

        new_data = pd.DataFrame({
            'taban': [taban],
            'yukseklik': [yukseklik],
            'ustkenar': [ustkenar],
            'sagkenar': [sagkenar],
        })
        data = data.append(new_data, ignore_index=True)
        data.to_csv('veri.csv', index=False)
        return {'data': new_data.to_dict('records')}, 200

class KareAlan(Resource):
    def get(self):
        data = pd.read_csv('veri.csv')
        data = data.to_dict('records')
        alan = []
        for i in range(0, len(data)):
            alan = (data[i]['taban'] * data[i]['taban']) #verilerden herhangi birinin karesi
            alan.append(alan)
        return {'alan': alan}, 200

class karecevre(Resource):
    def get(self):
        data = pd.read_csv('veri.csv')
        data = data.to_dict('records')
        cevre = []
        for i in range(0, len(data)):
            cevre = (data[i]['taban'] + data[i]['yukseklik'] + data[i]['sagkenar'] + data[i]['ustkenar'])
            cevre.append(cevre)
        return {'cevre': cevre}, 200

api.add_resource(Veri, '/veri')
api.add_resource(karealan, '/kareninAlani')
api.add_resource(karecevre, '/kareninCevresi')
if __name__ == '__main__':
    app.run()