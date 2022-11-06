import sqlite3
import basic

#demo
def demo():
    conn = sqlite3.connect('vegetables2.db')
    c = conn.cursor()

    r1 = basic.get_veg_by_season("winter", c)
    print("query1: show winter vegetables:")
    basic.printline(r1)
    print()

    r2 = basic.get_veg_lower_than_price(20, c)
    print("query2: show vegetables which price < 20:")
    basic.printline(r2)
    print()

    r3 = basic.get_veg_higher_than_price(20, c)
    print("query3: show vegetables which price > 20:")
    basic.printline(r3)
    print()

    r4 = basic.get_cheapest_x_veg_with_x(3, c)
    print("query4: show cheapest x vegetables")
    basic.printline(r4)
    print()

    r5 = basic.get_veg_by_name("onion", c)
    print("query5: show vegetable by name")
    basic.printline(r5)
    print()

    conn.close()



demo()