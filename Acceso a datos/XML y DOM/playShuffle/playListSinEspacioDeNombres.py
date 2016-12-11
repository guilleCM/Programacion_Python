
#IMPORTAR LIBRERIA XML y asignarle nombre#
import xml.etree.cElementTree as ET
#importar el archivo XML y guardarlo en variables globales
tree = ET.parse('prueba.xml')
root = tree.getroot()

tracklist = root.find('trackList')

libreriaPlayList={}
for track in tracklist:
	detallesCancion={
		track.find('title').text:
		{
		"location":track.find('location').text,
		"creator":track.find('creator').text,
		"album":track.find('album').text,
		"trackNum":track.find('trackNum').text,
		}
	}
	libreriaPlayList.update(detallesCancion)


print ("##### CANCIONES EN LA LIBRERIA #####")
print (libreriaPlayList.keys())
