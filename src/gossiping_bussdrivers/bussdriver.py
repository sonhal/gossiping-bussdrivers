import typing


class Bussdriver:

    def __init__(self, route: typing.Sequence, gossip):
        self._route = route
        self._index = 0
        self._gossip = {gossip, }

    def next_stop(self):
        next_stop = self._route[self._index]
        self._index += 1
        if self._index > len(self._route) - 1:
            self._index = 0
        return next_stop

    def gossip(self, bussdriver: "Bussdriver"):
        self._gossip.update(bussdriver._gossip)
        bussdriver._gossip.update(self._gossip)

    def has_gossip(self, *gossip):
        gossip = set(gossip)
        return gossip.issubset(self._gossip)

    def is_at_same_stop(self, bussdriver2: "Bussdriver"):
        return self._route[self._index] == bussdriver2._route[bussdriver2._index]
