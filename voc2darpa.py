import glob
import sys
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom
import numpy as np


def create_txt_file_darpa(xml_path):
    txt_label = (xml_path).replace('.xml','.txt')
    new_f = open(txt_label, "w+")

    voc_annotation_file = ET.parse(xml_path)
    root = voc_annotation_file.getroot()

    sizes = []
    classes = []
    bbox = []
    for elem in root:
        if elem.tag == "size":
            for size in elem:
                sizes.append(size.text)
        for subelem in elem:
            if subelem.tag == "name":
                if subelem.text == 'survirvor':
                    classes.append(0)
                if subelem.text == 'cell_phone':
                    classes.append(1)
                if subelem.text == 'backpack':
                    classes.append(2)
                if subelem.text == 'drill':
                    classes.append(3)
                if subelem.text == 'fire_extinguisher':
                    classes.append(4)
                if subelem.text == 'vent':
                    classes.append(5)
                if subelem.text == 'helmet':
                    classes.append(6)
                if subelem.text == 'rope':
                    classes.append(7)
                if subelem.text == 'cube':
                    classes.append(8)  # Verify that cube is 8..!
            for subsubelem in subelem:
                if subsubelem.tag in ["xmin", "xmax", "ymin", "ymax"]:
                    bbox.append(subsubelem.text)
    
    for i in range(0,len(classes)):
        x = float((int(bbox[1 + (i*4)]) + int(bbox[0 + (i*4)])) / (2*int(sizes[0]))) # Middle of the bbox
        y = float((int(bbox[3 + (i*4)]) + int(bbox[2 + (i*4)])) / (2*int(sizes[1]))) # Middle of the bbox
        w  = float((int(bbox[1 + (i*4)]) - int(bbox[0 + (i*4)])) / int(sizes[0]))
        h = float((int(bbox[3 + (i*4)]) - int(bbox[2 + (i*4)])) / int(sizes[1]))
        new_f.write(f"{classes[i]} {x} {y} {w} {h} \n")
    

if __name__ == '__main__':

    for root, dirs, files in os.walk("./output_darpa_v2/annotations"):
        for file in files:
            if file.endswith(".xml"):
                create_txt_file_darpa(root+ "/" + file)
                
