#****_XML example
#****_Autor: Jakub Koziorowski

# TODO: change code to function

import xml.etree.ElementTree as et

tree = et.ElementTree(file='books.xml')
root = tree.getroot()
#root.tag
x = 0
for child in root:
    #print('tag:', child.tag, '')
    for grandchild in child:
        if grandchild.tag == 'price':
            x += float(grandchild.text)
            #return x
print(x)
