import xml.etree.ElementTree as ET
import os

# not working if count of files more than 1000?
# all_files = os.listdir('../технологии_ИИ_в_детской_стоматологии/all_xml/')

FILENAME_0 = '0_ (%s).xml'
FILENAME_1 = '%s.xml'

for i in range(50):
    try:
        with open('../технологии_ИИ_в_детской_стоматологии/all_xml/' + FILENAME_0 % str(i + 1), 'r', encoding='ISO-8859-1') as xml_file:
            xml_tree = ET.parse(xml_file)

            xml_root = xml_tree.getroot()
            path_element = xml_root.find('path')
            path_text = path_element.text
            path_text = 'teeth' + path_text.split('teeth')[1]
            path_element.text = path_text

            xml_tree.write('../технологии_ИИ_в_детской_стоматологии/all_xml/' + FILENAME_0 % str(i + 1))
    except:
        print(FILENAME_0 % str(i + 1) + ' not exist')

for i in range(1246):
    try:
        with open('../технологии_ИИ_в_детской_стоматологии/all_xml/' + FILENAME_1 % str(i), 'r', encoding='ISO-8859-1') as xml_file:
            xml_tree = ET.parse(xml_file)

            xml_root = xml_tree.getroot()
            path_element = xml_root.find('path')
            path_text = path_element.text
            path_text = 'teeth' + path_text.split('teeth')[1]
            path_element.text = path_text

            xml_tree.write('../технологии_ИИ_в_детской_стоматологии/all_xml/' + FILENAME_1 % str(i))
    except:
        print(FILENAME_1 % str(i) + ' not exist')
