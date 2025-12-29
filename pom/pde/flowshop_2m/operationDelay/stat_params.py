from dataclasses import dataclass
from typing import Tuple


@dataclass
class StatParams:
    mean: float
    std: float

    @property
    def stats(self) -> Tuple[float, float]:
        return self.mean, self.std
