import typer
import basic
import sqlite3

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")

@app.command()
def get_veg_by_name(name: str):
    #connect
    conn = sqlite3.connect('vegetables2.db')
    c = conn.cursor()

    r = basic.get_veg_by_name(name, c)
    basic.printline(r)

    #disconnect
    conn.close()


if __name__ == "__main__":
    app()