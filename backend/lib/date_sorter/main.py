from lib.date_sorter.validator import DateValidator
from lib.date_sorter.sorter import DateSorter


if __name__ == '__main__':
    dates = ["11 Aug 2020", "29 Jan", "27 Jan", "1 Dec 2022", "28 Jan"]
    print("Input:")
    print("+-" * 50)
    print('\n'.join(dates))

    validator = DateValidator(dates)
    sorter = DateSorter(validator.datetimes)
    sorted_dates = sorter.sort_dates()
    isoformatted = [dt.isoformat() for dt in sorted_dates]

    print("*-" * 50)
    print("Output:")
    print('\n'.join(isoformatted))
