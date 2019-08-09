from gossiping_bussdrivers.busdriver import Busdriver
from pprint import pprint as pp

from gossiping_bussdrivers.gossiping_busdrivers import GossipingBusdrivers


def gossip_sim():
    routes = [[3, 1, 2, 3], [3, 2, 3, 1], [4, 2, 3, 4, 5]]
    gbd = GossipingBusdrivers(routes)
    print("Result: " + str(gbd.simulate(480)))


if __name__ == "__main__":
    gossip_sim()