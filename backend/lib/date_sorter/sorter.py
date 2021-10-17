from typing import List
from datetime import datetime as Datetime


class DateSorter:

    def __init__(self, array: List[Datetime]):
        self._dates = array

    def sort_dates(self):
        dates = self._dates.copy()
        return sorted(dates)
