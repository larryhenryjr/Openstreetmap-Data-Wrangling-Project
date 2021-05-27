#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 23:58:58 2021

@author: larry

Task:
"""
# Importing modules
import csv
import codecs
import pprint
import re
import xml.etree.cElementTree as ET
from collections import defaultdict
import cerberus
import schema

osmfile = "sample_irving_texas.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected = ["Avenue", "Boulevard", "Bridge", "Center", "Circle", "Court", "Drive", "East", "Expressway", "Freeway", "Highway", "Lane", "Loop", 
            "National", "North", "Northeast", "Northwest", "Parkway", "Place", "Plaza", "Road", "Route", "South", "Southeast", "Southwest", "Square", 
            "Street", "Terrace", "Trail", "Turnpike", "Way", "West"]

#mapping
mapping = { "Ave":"Avenue",
            "Ave.":"Avenue",
			"Blvd": "Boulevard",
			"Blvd.": "Boulevard",			
			"Cir": "Circle",
			"Cir.": "Circle",
			"Cres": "Crescent",
			"Cres.": "Crescent",
			"Ct": "Court",
			"Ct.": "Court",
			"Ctr": "Center",
			"Ctr.": "Center",
			"Dr": "Drive",
			"Dr.": "Drive",
			"E": "East",
			"E.": "East",
			"Expwy": "Expressway",
			"Expwy.": "Expressway",
			"Fwy": "Freeway",
			"Fwy.": "Freeway",
			"Hill": "Hill",
			"Hill.": "Hill",
			"Hwy": "Highway",
			"Hwy.": "Highway",
            "Ln": "Lane",
            "Ln.": "Lane",
            "Pkwy":"Parkway",
			"Rd": "Road",
			"Rd.": "Road",
            "Raod": "Road",      
			"Rte": "Route",
			"Rte.": "Route",
			"S": "South",
			"S.": "South",
			"Se": "Southeast",
			"Se.": "Southeast",
			"Sq": "Square",
			"Sq.": "Square",	
        	"St": "Street",
            "St.": "Street",
			"Tr": "Trail",
			"Tr.": "Trail",
			"W": "West",
			"W.": "West",
			"Way": "Way",
			"Way.": "Way"			
            }

# ================================================== #
#         Auditing and Cleaning Functions            #
# ================================================== #

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


# This function is used for cleaning the street names
def update_name(name, mapping):
    """Function is used for cleaning the street names"""
    
    unwanted = ['(',')','/', '[', ']', '.', ',']  # List of unwanted characters
    cname = ''                  # Create an empty string 
    
    # for loop to remove unwanted characters
    for i in range(len(name)):
        if name[i] not in unwanted:
            cname = cname + name[i]
    
    # Slicing to remove '-'
    if cname[0]=='-':
        print("2. Slicing to remove '-'")
        cname = cname[1:]
    if cname[-1]=='-' or cname[-1]==',':
        cname = cname[:-1]
    
    # To remove postal codes from street name
    if '-' in cname:
        ch = cname.split('-')
        if len(ch[1])>=4:
            cname = ch[0]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    
    # Capitalize the first letter of each street name and convert other letters to lower case
    low_name = cname.lower()
    if ' ' in low_name:
        cname = ''
        t = low_name.split(' ')
        for i in t:
            cname = cname + ' ' + i.capitalize()
    else:
        cname = low_name.capitalize()
           
    # Mapping 
    k = mapping.keys()
    key_list = list(k)
    for abrev in key_list:
        if abrev in cname.split():
            cname = cname.replace(abrev,mapping[abrev])

    return cname

  
# ================================================== #
#         Preparing for Database - SQL               #
# ================================================== #

#OSM_PATH = "sample_IrvingTX-W-LasColinas.osm"

NODES_PATH = "nodes.csv"
NODE_TAGS_PATH = "nodes_tags.csv"
WAYS_PATH = "ways.csv"
WAY_NODES_PATH = "ways_nodes.csv"
WAY_TAGS_PATH = "ways_tags.csv"

LOWER_COLON = re.compile(r'^([a-z]|_)+:([a-z]|_)+')
PROBLEMCHARS = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

SCHEMA = schema.schema

# Make sure the fields order in the csvs matches the column order in the sql table schema
NODE_FIELDS = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_FIELDS = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAY_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_NODES_FIELDS = ['id', 'node_id', 'position']


def shape_element(element, node_attr_fields=NODE_FIELDS, way_attr_fields=WAY_FIELDS, problem_chars=PROBLEMCHARS, default_tag_type='regular'):
    """Clean and shape node or way XML element to Python dict 'shape_element()' function edits a single element (parent and children) one at a time. Called by the 'process_map()' function"""
      
    node_attribs = {}
    way_attribs = {}
    way_nodes = []
    tags = []  # Handle secondary tags the same way for both node and way elements

    if element.tag == 'node':
        for i in node_attr_fields:
            node_attribs[i]=element.attrib[i]
                
        for next_tag in element.iter('tag'):
            node_tag = {}
            
            if PROBLEMCHARS.match(next_tag.attrib['k']):
                continue
            
            elif LOWER_COLON.match(next_tag.attrib['k']):
                node_tag["id"] = element.attrib['id']                
                node_tag["type"] = next_tag.attrib['k'].split(":", 1) [0]
                node_tag["key"] = next_tag.attrib['k'].split(":", 1) [1]
                                
                # use cleaning function:
                if next_tag.attrib["k"] == 'addr:street':
                    node_tag["value"] = update_name(next_tag.attrib['v'], mapping)

                # otherwise:
                else:
                    node_tag["value"] = next_tag.attrib['v']  
                tags.append(node_tag)
            
            else:
                tag_elements = {}
                tag_elements['id'] = element.attrib['id']
                tag_elements['value'] = next_tag.attrib['v']
                if ':' in next_tag.attrib['k']:
                    k_value = next_tag.attrib['k'].split(':',1)
                    tag_elements['type'] = k_value[0]
                    tag_elements['key'] = k_value[1]
                else:
                    tag_elements['type'] = default_tag_type
                    tag_elements['key'] = next_tag.attrib['k']
                tags.append(tag_elements)
                
        return({'node': node_attribs, 'node_tags': tags})
    
    elif element.tag == 'way':
        
        for i in WAY_FIELDS:
            way_attribs[i]=element.attrib[i]
        
        for next_tag in element.iter('tag'):
            way_tag = {}

            if PROBLEMCHARS.match(next_tag.attrib['k']):
                continue
                
            elif LOWER_COLON.match(next_tag.attrib['k']):
                way_tag["type"] = next_tag.attrib['k'].split(":", 1) [0]
                way_tag["key"] = next_tag.attrib['k'].split(":", 1) [1]
                way_tag["id"] = element.attrib['id']
                
                # use cleaning function:
                if next_tag.attrib["k"] == 'addr:street':
                    way_tag["value"] = update_name(next_tag.attrib['v'], mapping)
                
                # otherwise:
                else:
                    way_tag["value"] = next_tag.attrib['v']
                tags.append(way_tag)
                
            else:
                tag_elements = {}
                tag_elements['id'] = element.attrib['id']
                tag_elements['value'] = next_tag.attrib['v']
                if ':' in next_tag.attrib['k']:
                    k_value = next_tag.attrib['k'].split(':',1)
                    tag_elements['type'] = k_value[0]
                    tag_elements['key'] = k_value[1]
                else:
                    tag_elements['type'] = 'regular'
                    tag_elements['key'] = next_tag.attrib['k']
                tags.append(tag_elements)
        
        pos = 0
        for node in element.iter('nd'):
            waynd_dt = {}
            waynd_dt['id'] = element.attrib['id']
            waynd_dt['node_id'] = node.attrib['ref']
            waynd_dt['position'] = pos
            pos += 1
            way_nodes.append(waynd_dt)

        return({'way': way_attribs, 'way_nodes': way_nodes, 'way_tags': tags})


# ================================================== #
#               Helper Functions                     #
# ================================================== #

def get_element(osm_file, tags=('node', 'way', 'relation')):
    """Yield element if it is the right type of tag"""

    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()


def validate_element(element, validator, schema=SCHEMA):
    """Raise ValidationError if element does not match schema"""
    if validator.validate(element, schema) is not True:
        field, errors = next(validator.errors.iteritems())
        message_string = "\nElement of type '{0}' has the following errors:\n{1}"
        error_string = pprint.pformat(errors)
        
        raise Exception(message_string.format(field, error_string))


class UnicodeDictWriter(csv.DictWriter, object):
    """Extend csv.DictWriter to handle Unicode input"""

    def writerow(self, row):
        super(UnicodeDictWriter, self).writerow({
            k: v for k, v in row.items()
        })

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


# ================================================== #
#               Main Function                        #
# ================================================== #
def process_map(file_in, validate):
    """Iteratively process each XML element and write to csv(s)"""

    with codecs.open(NODES_PATH, 'w', "utf-8") as nodes_file, \
         codecs.open(NODE_TAGS_PATH, 'w', "utf-8") as nodes_tags_file, \
         codecs.open(WAYS_PATH, 'w', "utf-8") as ways_file, \
         codecs.open(WAY_NODES_PATH, 'w', "utf-8") as way_nodes_file, \
         codecs.open(WAY_TAGS_PATH, 'w', "utf-8") as way_tags_file:

        nodes_writer = UnicodeDictWriter(nodes_file, NODE_FIELDS)
        node_tags_writer = UnicodeDictWriter(nodes_tags_file, NODE_TAGS_FIELDS)
        ways_writer = UnicodeDictWriter(ways_file, WAY_FIELDS)
        way_nodes_writer = UnicodeDictWriter(way_nodes_file, WAY_NODES_FIELDS)
        way_tags_writer = UnicodeDictWriter(way_tags_file, WAY_TAGS_FIELDS)

        nodes_writer.writeheader()
        node_tags_writer.writeheader()
        ways_writer.writeheader()
        way_nodes_writer.writeheader()
        way_tags_writer.writeheader()

        validator = cerberus.Validator()

        for element in get_element(file_in, tags=('node', 'way')):
            el = shape_element(element)
            if el:
                if validate is True:
                    validate_element(el, validator)

                if element.tag == 'node':
                    nodes_writer.writerow(el['node'])
                    node_tags_writer.writerows(el['node_tags'])
                elif element.tag == 'way':
                    ways_writer.writerow(el['way'])
                    way_nodes_writer.writerows(el['way_nodes'])
                    way_tags_writer.writerows(el['way_tags'])


if __name__ == '__main__':
    process_map(osmfile, validate=True)
