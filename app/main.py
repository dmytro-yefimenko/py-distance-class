from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float) -> Any:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            return TypeError("Wrong type for addition")

    def __iadd__(self, other: int | float) -> Any:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Wrong type for inplace addition")
        return self

    def __mul__(self, other: int | float) -> Any:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("Wrong type for multiplication")

    def __truediv__(self, other: int | float) -> Any:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError("Unsupported type for division")

    def __lt__(self, other: int | float) -> Any:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km < other_km

    def __gt__(self, other: int | float) -> Any:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km > other_km

    def __eq__(self, other: int | float) -> Any:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km == other_km

    def __le__(self, other: int | float) -> Any:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km <= other_km

    def __ge__(self, other: int | float) -> Any:
        other_km = other.km if isinstance(other, Distance) else other
        return self.km >= other_km
