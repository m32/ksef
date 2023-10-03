import xml.etree.ElementTree as ET 
from lxml import etree


class KSeF_xml:
    def __init__(self, path):
        self.tree: ET.ElementTree = etree.parse(path)
        self.root: ET.Element = self.tree.getroot( )
        self.nsmap: dict = self._set_namespaces()
        
    def _set_namespaces(self) -> dict:
        namespaces = self.root.nsmap
        for namespace, value in self.root.nsmap.items():
            if not namespace:
                del namespaces[namespace]
                namespaces[''] = value
        return namespaces
    
    def get_child_by_tag(self, tag:str, namespace:str=None, in_element:ET.Element=None) -> ET.Element:
        if in_element is None:
            in_element = self.root
        
        if namespace:
            element = in_element.find(f'{namespace}:{tag}', namespaces=self.nsmap)
        else:
            element = in_element.find(tag, namespaces=self.nsmap)
        
        if element is None:
            for child in in_element:
                element = self.get_child_by_tag(tag, namespace, in_element=child)
                if element is not None:
                    break
        
        if element is not None: 
            return element
        raise Exception(f'Cannot find element {tag} with namespace {namespace}')
    
    def to_string(self):
        return ET.tostring(self.root).decode('UTF-8')
    
    def to_bytes(self):
        return ET.tostring(self.root)