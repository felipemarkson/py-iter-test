import random
import time
from functools import reduce

random.seed(0)
MAX_QTY = 10
MAX_PRICE = 500

def __get_item():
    return {
        "product": f"Doesn't matter {random.random()}",
        "qty": random.randint(1, MAX_QTY),
        "price": random.randint(1, MAX_PRICE)
    }

def mens_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start
    return wrapper

def get_items(n_itens):
    return [__get_item() for _ in range(0, n_itens)]

def warm_things(items):
    return sum([item["qty"] + item["price"] for item in items])

@mens_time
def run_for(items):
    total = 0
    for item in items:
        total += item["qty"] * item["price"]
    return total

@mens_time
def run_reduce(items):
    return reduce(lambda acc, item: acc + (item["qty"] * item["price"]), items, 0)

@mens_time
def run_list_comprehension(items):
    return sum([item["qty"] * item["price"] for item in items])