# kaiyuan_proj3
This is project 3 for ids706. This project generates a script that queries database sqlite3 with vegetable market data from
[dataset source](https://www.kaggle.com/datasets/sudipsamanta35/vegetable-market)

The 5 queries in basic.py are :
1. get the x cheapest vegetable with given x
2. get vegetable with given name
3. get vegetable with given season
4. get vegetable which price is higher than given price
5. get vegetable which price is lower than given price

demo.py uses the functions in basic.py to answer these questions.

Extra:
Using typer in main.py, we can also use command line tool to do the query. This is a more customized choice that user can decide with what argument he/she want to do the query.

## 5 Query with fixed argument
```
make install
demo.py
```

## Command line tool with customized argument

```
make install
python3 main.py --help
python3 main.py get-cheapest-x-veg-with-x [OPTIONS] LIMIT
python3 main.py get-veg-by-name [OPTIONS] NAME
python3 main.py get-veg-by-season [OPTIONS] SEASON 
python3 main.py get-veg-higher-than-price [OPTIONS] PRICE
python3 main.py get-veg-lower-than-price [OPTIONS] PRICE
```
