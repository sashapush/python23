"""
Flight leg:
GLA -> LHR -> CAN  - this is a flight, with starting point to the end, like

2 segments (GLA -> LHR, LHR -> CAN)
"""
from typing import List



class Segment:
    def __init__(self, departure, destination):
        self.departure = departure #f.e GLA
        self.destination = destination #f.e LHR

class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    @property
    def departure_point(self) -> str: #we return string
        return self.segments[0].departure

    def __repr__(self):
        """

        :return: string in the format GLA -> LHR -> CAN
        """
        #stops = [self.segments[0].departure,self.segments[0].destination]
        #for seg in self.segments[1:]: #1 onwards
        #    stops.append(seg.destination)
#or to simplify STOPS further
        stops = [self.segments[0].departure]  +[seg.destination for seg in self.segments]
        return ' -> '.join(stops) #joins each of the elements of STOPS with the provided string ' -> '
    @departure_point.setter #allows to update the property
    def departure_point(self, val):
        #self.segments[0].departure = val; another way is to create segment
        dest = self.segments[0].destination
        self.segments[0] = Segment(departure=val,destination=dest)


flight = Flight([Segment("GLA","LHR"),Segment("LHR", "AUS")])
print(flight.departure_point)
print(flight)
#but to update departure point we'd need to:
#flight.segments[0].departure = "EDI"
#but easier to make sure that below works
flight.departure_point = "EDI"
flight.departure_point = "EDI"
print(flight.departure_point)
print(flight)