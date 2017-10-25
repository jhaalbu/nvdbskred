import nvdbapi
from flask import Flask, request, render_template
from wtforms import Form, IntegerField, StringField, validators
import requests

app = Flask(__name__)

@app.route('/')
def graph(chartID = 'chart_ID', chart_type = 'pie', chart_height = 500):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'Label1', "data": [['foo',2],['bar',4],['monty',5]]}]
	title = {"text": 'My Title'}
	xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
	yAxis = {"title": {"text": 'yAxis Label'}}
	return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

# print(data)
#skred = nvdbapi.nvdbFagdata(445)
#skred.addfilter_geo( { 'vegreferanse' : 'Fv241', 'fylke' : 14})
#skred.addfilter_egenskap('2326=4198')


#print(skred.statistikk())
#ettskred = skred.nesteNvdbFagObjekt()
#print(ettskred.egenskapverdi(2326))
#print(ettskred.egenskapverdi(2324))
#print(ettskred.egenskap(2326))
"""
i = 0
for i in range(0, 1):
    i = i + 1
    ettskred = skred.nesteNvdbFagObjekt()
    print(ettskred.egenskapverdi(2326))
    print(ettskred.egenskapverdi(2324))
    print(ettskred.egenskapverdi(7905))
    print(ettskred.wkt())
    print(ettskred.egenskapverdi(2326))
"""

if __name__ == "__main__":
	app.run()