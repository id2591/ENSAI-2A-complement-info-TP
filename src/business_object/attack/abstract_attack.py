import copy

from business_object.statistic import Statistic
from abc import ABC, abstractmethod

class AbstractAttack:

    # -------------------------------------------------------------------------
    # Constructor
    # -------------------------------------------------------------------------

    def __init__(self, power:0, name=None, description=None):
        # -----------------------------
        # Attributes
        # -----------------------------
        self._power: int = power
        self._name: str = name
        self._description: str = description

    # -------------------------------------------------------------------------
    # Methods
    # -------------------------------------------------------------------------

    @abstractmethod
    def compute_damage(self, APkm, APkm) -> int:
        pass
