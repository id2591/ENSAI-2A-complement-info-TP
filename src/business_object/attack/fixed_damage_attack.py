from business_object.attack.abstract_attack import AbstractAttack
from business_object.statistic import Statistic

class FixedDamageAttack(AbstractAttack):
    """
    A Fixed damage Attack
    """
    def __init__(
        self, 
        power: int = 0, 
        name: str | None=None, 
        description: str | None=None
    ):
        super().__init__(
            power=power, name=name, description=description
        )
        
    def def compute_damage(self, APkm, APkm) -> int:
        """
        Compute a damage related to the pokemon type.

        Returns :
            float : the multiplier
        """
        return power
