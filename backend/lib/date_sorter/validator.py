from typing import List, Optional, Tuple
from datetime import datetime as Datetime
from lib.date_sorter.exceptions import WrongInputDate


class DateValidator:

    VALID_FORMATS_EXAMPLES = [
        ("%d %b %Y", "11 Aug 2020"),
        ("%d %b", "29 Jan"),
        ("%d/%m/%Y", "01/01/1990")
    ]
    datetimes: List[Datetime]

    def __init__(self, array: List[str]):
        self._str_dates = array
        self.datetimes = []
        self._fill_datetimes_or_raise()

    def _fill_datetimes_or_raise(self):
        for date in self._str_dates:
            dttime = self._maybe_apply_format_to_date(date)
            self.datetimes.append(dttime)
    
    def _maybe_apply_format_to_date(self, date: str):
        for dt_format, _ in self.VALID_FORMATS_EXAMPLES:
            dttime = self._parse_date(date, dt_format)
            if not dttime:
                continue
            return dttime
        raise WrongInputDate((
            f"Invalid date format for `{date}`. "
            "Valid Formats are: " +
            str([example for _, example in self.VALID_FORMATS_EXAMPLES])
        ))
    
    def _parse_date(self, date: str, dt_format: str) -> Optional[Datetime]:
        date, dt_format = self._get_date_and_format_with_year(date, dt_format)
        try:
            dttime = Datetime.strptime(date, dt_format)
        except ValueError:
            return None
        return dttime

    def _get_date_and_format_with_year(self, date: str, dt_format: str) -> Tuple[str, str]:
        YEAR_FORMAT = '%Y'
        if YEAR_FORMAT not in dt_format:
            dt_format += YEAR_FORMAT
            date += str(Datetime.today().year)
        return date, dt_format
