import Spread
import json
def main():

    with open('Parameters.JSON') as file:
        params = json.load(file)
    Sim = Spread.Spread(50,1,params)
    Sim.run()
main()

