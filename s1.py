import nvdbapi
from flask import Flask, request, render_template
from wtforms import Form, IntegerField, StringField, validators
import requests

app = Flask(__name__)

from wtforms import Form, IntegerField, StringField, validators

class InputForm(Form):
    veg = StringField(label='Veg (f.eks fv60)', validators=[validators.InputRequired()])
    fylke = IntegerField(label='Fylke (f.eks 14)', validators=[validators.InputRequired()])

def hentSkred(veg, fylke):
    skredtypenr = [4198, 4199, 5351, 4200, 4201, 4202, 4203, 13103]
    skredtype = {4198 : 'Stein', 4199: 'Jord/løsmasse', 5351: 'Is/stein', 4200: 'Snø', 4201: 'Is', 4202: 'Flomskred (vann+stein+jord)', 4203: 'Sørpeskred (vann+snø+stein)', 13103: 'Utglidning av veg'}
    liste = []
    skred = nvdbapi.nvdbFagdata(445)
    skred.addfilter_geo( { 'vegreferanse' : veg, 'fylke' : fylke})
    sNum = 0
    data = []
    for i in skredtypenr:
        skred.addfilter_egenskap('2326=' + str(skredtypenr[sNum]))
        stat = skred.statistikk()
        data.append([skredtype[i], stat['antall']])
        sNum = sNum + 1
    return data



@app.route('/', methods=['GET', 'POST'])
def index(chart1ID = 'chart1_ID', chart1_type = 'pie', chart1_height = 500,  chart2ID = 'chart2_ID', chart2_type = 'bar', chart2_height = 500):
	form = InputForm(request.form)
	if request.method == 'POST' and form.validate():
		data = hentSkred(form.veg.data, form.fylke.data)
	else:
		data = None

	chart1 = {"renderTo": chart1ID, "type": chart1_type, "height": chart1_height,}
	series1 = [{"name": 'Antall skred', "data": data}]
	title1 = {"text": 'Skred per vegstrekning'}
	xAxis1 = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
	yAxis1 = {"title": {"text": 'yAxis Label'}}

	chart2 = {"renderTo": chart2ID, "type": chart2_type, "height": chart2_height,}
	series2 = [{"name": 'Antall skred', "data": data}]
	title2 = {"text": 'Skred per vegstrekning'}
	xAxis2 = {"categories": ['Stein', 'Jord/løsmasse', 'Is/stein', 'Snø', 'Is', 'Flomskred (vann+stein+jord)', 'Sørpeskred (vann+snø+stein)', 'Utglidning av veg' ]}
	yAxis2 = {"title": {"text": 'Antall skred'}}

	return render_template('graf.html', form=form, chart1ID=chart1ID, chart1=chart1, series1=series1, title1=title1, xAxis1=xAxis1, yAxis1=yAxis1, chart2ID=chart2ID, chart2=chart2, series2=series2, title2=title2, xAxis2=xAxis2, yAxis2=yAxis2)


if __name__ == "__main__":
	app.run()