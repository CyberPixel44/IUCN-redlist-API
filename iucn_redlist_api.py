#!/usr/bin/env python
 
import urllib
import json
import sys

if sys.version_info[0] == 3:
    from urllib.request import urlopen

locu_api = '?token=<INSERT_YOUR_TOKEN_id_HERE>'
line = "-----------------------------------------------"
def country_search(query):
    api_key = locu_api
    url = 'http://apiv3.iucnredlist.org/api/v3/country/getspecies/'
    country = query.replace(' ', ' ')
    final_url = url + country + api_key
    json_obj = urllib.urlopen(final_url)
    data = json.load(json_obj)
    for item in data['result']:
        print (item['category'], item['scientific_name'])

def category_search(query):
    api_key = locu_api
    url = 'http://apiv3.iucnredlist.org/api/v3/species/category/'
    category = query.replace(' ', ' ')
    final_url = url + category + api_key
    json_obj = urllib.urlopen(final_url)
    data = json.load(json_obj)
    for item in data['result']:
        print (item['scientific_name'])

def species_search(query):
    api_key = locu_api
    url = 'http://apiv3.iucnredlist.org/api/v3/species/'
    species = query.replace(' ', ' ')
    final_url = url + species + api_key
    with urlopen(final_url) as url:
        json_obj = url.read()
    data = json.load(json_obj)
    for item in data['result']:
        print ("Scientific Name : ", item['scientific_name'], "\n", "Kingdom : ", item['kingdom'], "\n" ,"Phylum : ", item['phylum'], "\n", "Class : ", item['class'],"\n","Order : ", item['order'], "\n", "Family : ", item['family'], "\n", "Genus : ", item['genus'], "\n", "Common Name : ", item['main_common_name'], "\n", "Category : ", item['category'])

print ("Options : Country, Category, Species")
option = input("Type The Option : ")
if option == "country" :
    country_input = raw_input("Type country code : ")
    print (line)
    country_search(country_input)
    print (line)

if option == "category" :
    category_input = input("Type category code : ")
    print (line)
    category_search(category_input)
    print (line)

if option == "species" :
    species_input = input("Type species scientific name : ")
    print (line)
    species_search(species_input)
    print (line)
