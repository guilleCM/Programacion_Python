#IMPORTAR LIBRERIA XML y asignarle nombre#
import xml.etree.cElementTree as ET
#importar el archivo XML y guardarlo en variables globales
tree = ET.parse('playListVLC_xspf.xml')
root = tree.getroot()

menu = {}
nombrePlato = "Nombre plato: "
precioPlato = "Precio: "
for child in root:
	nombreYprecio = {}
	nombreYprecio[child.find('name').text]=child.find("price").text
	menu.update(nombreYprecio)
	print (nombrePlato + child.find('name').text + ", " + precioPlato + child.find("price").text)

##CASOS TEST##
if __name__ == "__main__":
####POSTCONDICION####
	if len(menu) == 5:
		print ("TEST OK!!!")
	