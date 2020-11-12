from flask import Flask
from redis import Redis

import random

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

random.seed(444)
hats = {f"hat:{random.getrandbits(32)}": i for i in (
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1000,
        "npurchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "npurchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "npurchased": 0,
    })
}


@app.route('/')
def hello():

    try:

        redis.incr('hits')
        return 'Hello World! I have been seen %s times.' % redis.get('hits')

        hats.set("msg:hello", "Hello Redis!!!")

        msg = hats.get("msg:hello")
        print(msg)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
