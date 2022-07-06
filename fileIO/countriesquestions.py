import json
with open("countries.json",encoding="utf-8") as f:
    data=json.load(f)

#print total number of country details
print(len(data))
#print details of india
india_details=[country for country in data if country["name"]=="India"]
print(india_details)
#print languages of ukrane
languages=[country["languages"] for country in data if country["name"]=="India"]
for lan in languages[0]:
    print(lan["name"])
#print currency of china
currency_details=[country["currencies"] for country in data if country["name"].lower().startswith("palestine")]
curr=[details.get("name") for details in currency_details[0]]
print(curr)
# print(currency_details)
currency=[country["currencies"] for country in data if country["name"]=="China"]
currency_name=[c.get("name")for c in currency[0]]
print(currency_name)
#print population of india
population=[country["population"] for country in data if country["name"]=="India"]
print(population)
##print neighboring countries od australia
# neighbor=[country["borders"] for country in data if country["name"]=="India"]
# print(neighbor)


#print neighboring countries od australia using function
def get_country_data(country_name):
    return[country for country in data if country["name"].lower().startswith(country_name)]

aust_data=get_country_data("austria")
print(aust_data[0].get("borders"))

country_data=get_country_data("india")
country_borders=country_data[0].get("borders")
sharing_borders=[country.get("name") for country in data if country["alpha3Code"] in country_borders]
print(sharing_borders)


# country with highest population
population=max(data,key=lambda d:d.get("population"))
print(population.get("name"))


#country with minimum population
population=min(data,key=lambda d:d.get("population"))
print(population.get("name"))