import yaml
import sys
import xml.etree.ElementTree as ET

if len(sys.argv) < 3:
    sys.exit(1)

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

def dict_to_xml(tag, d):
    elem = ET.Element(tag)
    if isinstance(d, dict):
        for k, v in d.items():
            child = dict_to_xml(k, v)
            elem.append(child)
    elif isinstance(d, list):
        for item in d:
            child = dict_to_xml('item', item)
            elem.append(child)
    else:
        elem.text = str(d)
    return elem

root = dict_to_xml('root', data)
tree = ET.ElementTree(root)
ET.indent(tree, space="    ")
tree.write(sys.argv[2], encoding='utf-8', xml_declaration=True)
