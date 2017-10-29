import urllib2
import xml.dom.minidom
import datetime
from xml.dom.minidom import Node
from xml.dom.minidom import parseString

#-----------------
#Functions
#-----------------
def getXgeoWeb(date,parameter,lat,lon):
	print('---Getting data from xgeo---')
	print('Input: Date: ' + str(date) + ' Parameter: ' + str(parameter) + ' Position: ' + str(lat) + '/' + str(lon))
	#Setting url
	url = 'http://h-web01.nve.no/chartserver/ShowData.aspx?req=getchart&ver=1.0&vfmt=xml&time=' + date + 'T0000;' + date + 'T1200&chs=10x10&lang=no&chlf=none&chsl=0;+0&chhl=2|0|2&timeo=-06:00&app=3d&chd=ds=hgts,da=29,id=' + str(lon) + ';' + str(lat) + ';' + parameter + ',cht=line,mth=inst&nocache=0.18694874164774933'
	#Download file:
	xmldata = urllib2.urlopen(url)
	#Parsing xml
	dom = xml.dom.minidom.parseString(xmldata.read())
	serie=dom.getElementsByTagName('Serie')
	for node in serie:
		data=node.getElementsByTagName('Legend')
		for a in data:
			legend = a.firstChild.data
		data=node.getElementsByTagName('DateTime')
		for a in data:
			date = a.firstChild.data
		data=node.getElementsByTagName('Value')
		for a in data:
			value = a.firstChild.data
	date = datetime.datetime.strptime(date, '%d/%m/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S') 	#Changing date format if needed
	print('Output: Date: ' + date + ' Value: ' + value)
	return (date,value)

#-----------------
#Settings and workflow
#-----------------
lat = 6812749
lon = 33413
date = '20170912'
parameter = 'rr' #nedbør?

print(getXgeoWeb(date,parameter,lat,lon))
