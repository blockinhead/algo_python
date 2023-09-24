class Floor:
    def __init__(self, floor_number, queue):
        self.floor_number = floor_number
        self.goes_up = []
        self.goes_down = []
        for p in queue:
            if p > floor_number:
                self.goes_up.append(p)
            else:
                self.goes_down.append(p)

    def empty(self):
        if self.goes_up or self.goes_down:
            return False

        return True

    def __repr__(self):
        return '<up: %s; down: %s>' % (self.goes_up, self.goes_down)


class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = queues
        self.capacity = capacity
        self.direction = 'up'
        self.floors = [Floor(i, q) for i, q in enumerate(self.queues)]
        self.passengers = []
        self.current_floor = 0

    def _all_done(self) -> bool:
        for f  in self.floors:
            if not f.empty():
                return False

        return True

    def _lift_goes(self):
        stops = []
        floors = range(0, len(self.floors)) if self.direction == 'up' else range(len(self.floors) - 1, -1, -1)

        for f in floors:
            slo = self._stop_to_let_off(f)
            sli = self._stop_to_let_in(f)

            if slo or sli and f != self.current_floor:
                self.current_floor = f
                stops.append(f)

        self.direction = 'up' if self.direction == 'down' else 'down'

        return stops

    def _stop_to_let_off(self, floor):
        stopped = False
        while True:
            try:
                self.passengers.remove(floor)
                stopped = True
            except ValueError:
                break

        return stopped

    def _stop_to_let_in(self, floor):
        stopped = False
        if self.direction == 'up' and self.floors[floor].goes_up:
            stopped = True
            while len(self.passengers) < self.capacity and self.floors[floor].goes_up:
                self.passengers.append(self.floors[floor].goes_up.pop(0))
        if self.direction == 'down' and self.floors[floor].goes_down:
            stopped = True
            while len(self.passengers) < self.capacity and self.floors[floor].goes_down:
                self.passengers.append(self.floors[floor].goes_down.pop(0))

        return stopped

    def theLift(self):
        stops = [0]

        while not self._all_done():
            stops += self._lift_goes()

        if stops[-1] != 0:
            stops.append(0)

        return stops


if __name__ == '__main__':
    tests = [[((), (), (5, 5, 5), (), (), (), ()), [0, 2, 5, 0]],
             [((), (), (1, 1), (), (), (), ()), [0, 2, 1, 0]],
             [((), (3,), (4,), (), (5,), (), ()), [0, 1, 2, 3, 4, 5, 0]],
             [((), (0,), (), (), (2,), (3,), ()), [0, 5, 4, 3, 2, 1, 0]]]

    for t, r in tests:
        rr = Dinglemouse(t, 5).theLift()
        print(rr, r)
        # print(rr == r)
