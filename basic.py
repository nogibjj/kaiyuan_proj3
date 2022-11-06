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


#demo
def demo():
    conn = sqlite3.connect('vegetables2.db')
    c = conn.cursor()

    r1 = get_veg_by_season("winter", c)
    #print("query1: show winter vegetables:")
    #printline(r1)

    r2 = get_veg_lower_than_price(20, c)
    #print("query2: show vegetables which price < 20:")
    #printline(r2)

    r3 = get_veg_higher_than_price(20, c)
    #print("query3: show vegetables which price > 20:")
    #printline(r3)

    r4 = get_cheapest_x_veg_with_x(3, c)
    #print("query4: show cheapest x vegetables")
    #printline(r4)

    r5 = get_veg_by_name("onion", c)
    #print("query5: show vegetable by name")
    #printline(r5)

    conn.close()

demo()