import sqlite3


#get vegetabel given specific season
def get_veg_by_season(season, c):
    c.execute("SELECT * FROM vegetables WHERE Season = :season", {'season': season})
    return c.fetchall()

def get_veg_lower_than_price(price, c):
    c.execute("SELECT * FROM vegetables WHERE Price_per_kg < :price", {'price': price})
    return c.fetchall()

def get_veg_higher_than_price(price, c):
    c.execute("SELECT * FROM vegetables WHERE Price_per_kg > :price", {'price': price})
    return c.fetchall()

def get_cheapest_x_veg_with_x(limit, c):
    c.execute("SELECT * FROM vegetables ORDER BY Price_per_kg LIMIT :limit", {'limit':limit})
    return c.fetchall()

def get_veg_by_name(name, c):
    c.execute("SELECT * FROM vegetables WHERE Vegetable = :name", {'name':name})
    return c.fetchall()

#helper function
def printline(results):
    for element in results:
        print(element)


