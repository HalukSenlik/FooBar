cities_string = """Beijing	39.9	116.4
Cairo	30.0	31.2
Chicago	41.9	-87.6
Denver	39.7	-105.0
Karachi	24.9	67.0
Lagos	6.5	3.4
Lima	-12.0	-77.0
London	51.5	0.1
Los Angeles	34.1	-118.2
Manila	14.6	121.0
Mexico City	19.4	-99.1
Miami	25.7	-80.2
Moscow	55.7	37.6
Mumbai	19.1	72.8
New York	40.7	-74.0
San Francisco	37.8	-122.4
Sao Paulo	-23.6	-46.6
Sydney	-33.9	151.2
Tehran	35.7	51.3
Toronto	43.7	-79.4"""


def get_cities_dict():
    cities = cities_string.split("\n")
    cities_dict = {}
    for city_row in cities:
        city_split = city_row.split("	")
        city = city_split[0]
        latitude = city_split[1]
        longitude = city_split[-1]
        cities_dict[city] = {
            'latitude': latitude,
            'longitude': longitude
        }
    return cities_dict
