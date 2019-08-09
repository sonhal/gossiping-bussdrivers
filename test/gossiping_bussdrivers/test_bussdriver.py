import unittest
from gossiping_bussdrivers.busdriver import Busdriver


class BussdriverTest(unittest.TestCase):

    def test_init(self):
        route = [2, 3, 4]
        Busdriver(route, object())

    def test_next_stop(self):
        route = [2, 3, 4]
        bussdriver = Busdriver(route, object())
        self.assertEqual(2, bussdriver.next_stop())
        self.assertEqual(3, bussdriver.next_stop())
        self.assertEqual(4, bussdriver.next_stop())
        self.assertEqual(2, bussdriver.next_stop())

    def test_gossip(self):
        route = [2, 3, 4]
        bussdriver = Busdriver(route, object())
        bussdriver2 = Busdriver(route, object())
        self.assertNotEqual(bussdriver2._gossip, bussdriver._gossip)
        bussdriver.gossip(bussdriver2)
        self.assertEqual(bussdriver2._gossip, bussdriver._gossip)

    def test_has_gossip(self):
        route = [2, 3, 4]
        gossip = object()
        gossip2 = object()
        bussdriver = Busdriver(route, gossip)
        self.assertFalse(bussdriver.has_gossip(gossip2))
        bussdriver2 = Busdriver(route, gossip2)
        bussdriver.gossip(bussdriver2)
        self.assertTrue(bussdriver.has_gossip(gossip2))

    def test_is_at_same_stop(self):
        route = [2, 3, 4]
        gossip = object()
        gossip2 = object()
        bussdriver = Busdriver(route, gossip)
        bussdriver2 = Busdriver(route, gossip2)
        self.assertTrue(bussdriver.is_at_same_stop(bussdriver2))
        bussdriver2.next_stop()
        self.assertFalse(bussdriver.is_at_same_stop(bussdriver2))
        bussdriver.next_stop()
        self.assertTrue(bussdriver.is_at_same_stop(bussdriver2))
