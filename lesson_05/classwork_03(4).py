my_map = {
    "Winter": [12,1,2],
    "Fruhling": [3, 4, 5],
    "Sommer": [6, 7, 8],
    "Herbst": [9, 10, 11],
}
def month_to_season(month_number):
    for season, months in my_map.items():
        if month_number in months:
            return season



print(month_to_season(2))