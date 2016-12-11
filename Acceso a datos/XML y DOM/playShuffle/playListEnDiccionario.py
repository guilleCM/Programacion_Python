#IMPORTAR LIBRERIA XML y asignarle nombre#
import xml.etree.cElementTree as ET
#importar el archivo XML y guardarlo en variables globales
tree = ET.parse('playListVLC_xspf.xml')
root = tree.getroot()
#diccionario que contiene el espacio de nombres
xmlns = {"xmlns": "http://xspf.org/ns/0/",
         "xmlns:vlc": "http://www.videolan.org/vlc/playlist/ns/0/"}

trackList=root.find('xmlns:trackList', xmlns)

libreriaPlayList={}
for track in trackList:
	detallesCancion={
	track.find('xmlns:title', xmlns).text: {
		"location":track.find('xmlns:location', xmlns).text,
		"creator":track.find('xmlns:creator', xmlns).text,
		"album":track.find('xmlns:album', xmlns).text,
		"trackNum":track.find('xmlns:trackNum', xmlns).text,
		}
	}

	libreriaPlayList.update(detallesCancion)

print (libreriaPlayList)