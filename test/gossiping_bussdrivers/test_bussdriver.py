import unittest
from gossiping_bussdrivers.bussdriver import Bussdriver


class BussdriverTest(unittest.TestCase):

    def test_init(self):
        route = [2, 3, 4]
        Bussdriver(route, object())

    def test_next_stop(self):
        route = [2, 3, 4]
        bussdriver = Bussdriver(route, object())
        self.assertEqual(2, bussdriver.next_stop())
        self.assertEqual(3, bussdriver.next_stop())
        self.assertEqual(4, bussdriver.next_stop())
        self.assertEqual(2, bussdriver.next_stop())

    def test_gossip(self):
        route = [2, 3, 4]
        bussdriver = Bussdriver(route, object())
        bussdriver2 = Bussdriver(route, object())
        self.assertNotEqual(bussdriver2._gossip, bussdriver._gossip)
        bussdriver.gossip(bussdriver2)
        self.assertEqual(bussdriver2._gossip, bussdriver._gossip)

    def test_has_gossip(self):
        route = [2, 3, 4]
        gossip = object()
        gossip2 = object()
        bussdriver = Bussdriver(route, gossip)
        self.assertFalse(bussdriver.has_gossip(gossip2))
        bussdriver2 = Bussdriver(route, gossip2)
        bussdriver.gossip(bussdriver2)
        self.assertTrue(bussdriver.has_gossip(gossip2))

    def test_is_at_same_stop(self):
        route = [2, 3, 4]
        gossip = object()
        gossip2 = object()
        bussdriver = Bussdriver(route, gossip)
        bussdriver2 = Bussdriver(route, gossip2)
        self.assertTrue(bussdriver.is_at_same_stop(bussdriver2))
        bussdriver2.next_stop()
        self.assertFalse(bussdriver.is_at_same_stop(bussdriver2))
        bussdriver.next_stop()
        self.assertTrue(bussdriver.is_at_same_stop(bussdriver2))
