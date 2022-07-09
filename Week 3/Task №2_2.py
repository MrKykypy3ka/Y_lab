from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple, Any


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]
    show_dates = list()

    def schedule(self) -> List[datetime]:
        for interval in self.dates:
            date = interval[0]
            while date <= interval[1]:
                self.show_dates.append(date)
                date += timedelta(days=1)
        return self.show_dates


def main():
    m = Movie('sw', [
      (datetime(2020, 1, 1), datetime(2020, 1, 7)),
      (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])

    for d in m.schedule():
        print(d)


if __name__ == "__main__":
    main()