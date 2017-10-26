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
        print(i)
        print(skredtype[i])
        skred.addfilter_egenskap('2326=' + str(skredtypenr[sNum]))
        stat = skred.statistikk()
        data.append([skredtype[i], stat['antall']])
        sNum = sNum + 1
    return data

@app.route('/', methods=['GET', 'POST'])
def index(chartID = 'chart_ID', chart_type = 'pie', chart_height = 500):
	form = InputForm(request.form)
	if request.method == 'POST' and form.validate():
		data = hentSkred(form.veg.data, form.fylke.data)
	else:
		data = None

	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'Antall skred', "data": data}] #legg til data variabel istaden for liste i liste
	title = {"text": 'Antall skred fordelt på type'}
	xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
	yAxis = {"title": {"text": 'yAxis Label'}}

	return render_template('graf.html', form=form, chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)


if __name__ == "__main__":
	app.run()