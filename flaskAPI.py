from flask import Flask, Response
from flask_restful import Resource, Api, reqparse, abort
import json

#define required arguments for coin PUT statement
coin_put_args = reqparse.RequestParser()
coin_put_args.add_argument("coin", type=int, help="Incorrectly formatted data", required=True, location = "json")


# number of coins in machine held locally as it will zero out at the end of transaction
COINS = 0

class Coin(Resource):
    def put(self):
        coin_put_args.parse_args()
        global COINS
        COINS += 1
        return Response("", status=204, mimetype='application/json', headers={'X-Coins': COINS})

    def delete(self):
        global COINS
        temp_coins = COINS
        Coins = 0
        return Response("", status=204, mimetype='application/json', headers={'X-Coins': temp_coins})


class Inventory(Resource):
    # open vending.json, read contents, return them as an array of integers
    def get(self):
        with open("vending.json", "r") as read_file:
            inventory = json.load(read_file)
        read_file.close()
        inventory_quantity = list(inventory.values())
        return Response(str(inventory_quantity), status=200, mimetype='application/json')

class Specific_inventory(Resource):
    #return quantity of specific item in vending.json
    def get(self, item_id):
        with open("vending.json", "r") as read_file:
            inventory = json.load(read_file)
        read_file.close()
        item_id = str(item_id)
        return Response(str(inventory[item_id]), status=200, mimetype='application/json')

    #return item if available AND coins are >= 2, decrement item in vending.json, reset coins.
    def put(self, item_id):
        with open("vending.json", "r") as read_file:
            inventory = json.load(read_file)
        read_file.close()
        item_id = str(item_id)
        global COINS
        if COINS <= 1:
            abort(Response("", status=403, mimetype='application/json', headers={'X-Coins': COINS}))
        elif inventory[item_id] == 0:
            abort(Response("", status=404, mimetype='application/json', headers={'X-Coins': COINS}))
        else:
            COINS -= 2 #reduce by two coins
            inventory[item_id] -= 1 #decrement item by 1
            with open("vending.json", 'w') as write_file:
                json.dump(inventory, write_file)
            write_file.close()
            coins_to_return = COINS
            COINS = 0
            return Response('{"quantity":1}', status=200, mimetype='application/json', headers={'X-Coins': coins_to_return, 'X-Inventory-Remaining': inventory[item_id]})

#initializing app and establishing database
app = Flask(__name__)
api = Api(app)

#add all routes for api
api.add_resource(Coin, "/")
api.add_resource(Inventory, "/inventory")
api.add_resource(Specific_inventory, "/inventory/<int:item_id>")

#run the thing!
if __name__ == "__main__":
    app.run()