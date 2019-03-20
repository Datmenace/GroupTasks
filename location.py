import datetime


class TravelPoint:

    def __init__(self, place_name, departure_time, arrival_time):
        self.place_name = place_name.title()
        if departure_time is None:
            self.departure_time = None
        else:
            try:
                self.departure_time = datetime.datetime.strptime(
                    departure_time, '%Y/%m/%d %H:%M')
            except ValueError:
                raise ValueError("The departure_time must have the "
                                 "format YYYY/MM/DD HH:MM")
        if arrival_time is None:
            self.arrival_time = None
        else:
            try:
                self.arrival_time = datetime.datetime.strptime(
                    arrival_time, '%Y/%m/%d %H:%M')
            except ValueError:
                raise ValueError("The arrival_time must have the format "
                                 "YYYY/MM/DD HH:MM")
        if self.departure_time is None and self.arrival_time is None:
            raise ValueError("At least one of arrival "
                             "or departure time must be set")

