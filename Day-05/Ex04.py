travel_log = [
 {"country":"France", "cities_visited":["Paris","Lille", "Dijon"], "total_visits": 12},
 {"country":"Germany", "cities_visited":["Berlin","Hamburg", "Stuttgart"], "total_visits": 5},
]

def add_new_country(country, visited, cities):
 new_country = {}
 new_country['country'] = country
 new_country['cities_visited'] = cities 
 new_country['total_visits'] = visited
 travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)

