from gossiping_bussdrivers.busdriver import Busdriver


class GossipingBusdrivers:

    def __init__(self, routes):
        self._gossips = [object() for _ in routes]
        driver_data = list(zip(self._gossips, routes))
        self._bussdrivers = [
            Busdriver(route, gossip)
            for
            gossip, route
            in
            driver_data
        ]

    def is_all_gossip_known(self):
        for driver in self._bussdrivers:
            if not driver.has_gossip(*self._gossips):
                return False
        return True

    def tick(self):
        for driver in self._bussdrivers:
            for driver2 in self._bussdrivers:
                if driver == driver2:
                    continue
                if driver.is_at_same_stop(driver2):
                    driver.gossip(driver2)
        for driver in self._bussdrivers:
            driver.next_stop()

    def ticks(self, num):
        for _ in range(num):
            self.tick()

    def simulate(self, num_ticks):
        count = 1
        for _ in range(num_ticks):
            self.tick()
            if self.is_all_gossip_known():
                return count
            count += 1
        raise AttributeError("Cannot share all gossip within tick range")

