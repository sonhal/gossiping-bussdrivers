from unittest import TestCase

from gossiping_bussdrivers.bussdriver import Bussdriver
from gossiping_bussdrivers.gossiping_busdrivers import GossipingBusdrivers


class TestGossipingBusdrivers(TestCase):

    def setUp(self) -> None:
        self.routes = [[3, 1, 2, 3], [3, 2, 3, 1], [4, 2, 3, 4, 5]]


    def test_init(self):
        GossipingBusdrivers(self.routes)

    def test_is_all_gossip_known(self):
        self.assertFalse(GossipingBusdrivers(self.routes).is_all_gossip_known())

    def test_tick(self):
        self.routes = [[1, 2], [2], [1, 2, 3]]
        gbd = GossipingBusdrivers(self.routes)
        gbd.tick()
        gbd.tick()
        self.assertTrue(gbd.is_all_gossip_known())

    def test_ticks(self):
        self.routes = [[1, 2], [2], [1, 2, 3]]
        gbd = GossipingBusdrivers(self.routes)
        gbd.ticks(2)
        self.assertTrue(gbd.is_all_gossip_known())
        self.routes = [[1, 2], [2, 1], [1, 2]]
        gbd = GossipingBusdrivers(self.routes)
        gbd.ticks(20)
        self.assertFalse(gbd.is_all_gossip_known())

    def test_simulate(self):
        self.routes = [[1, 2], [2], [1, 2, 3]]
        gbd = GossipingBusdrivers(self.routes)
        self.assertEqual(1, gbd.simulate(2))

        self.routes = [[1, 2], [2, 1], [1, 2]]
        gbd = GossipingBusdrivers(self.routes)
        self.assertRaises(AttributeError, lambda: gbd.simulate(2))


