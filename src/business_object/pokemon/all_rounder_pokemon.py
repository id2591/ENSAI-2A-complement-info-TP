from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.statistic import Statistic

class AllRounderPokemon(AbstractPokemon):
    """
    An All Rounder Pokemon
    """
    def __init__(
        self,
        stat_max: Statistic | None = None,
        stat_current: Statistic | None = None,
        level: int = 0,
        name: str | None = None
    ):
        super().__init__(
            stat_max=None, stat_current=stat_current, level=level, name=name, type_pk="All rounder"
        )

    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the pokemon type.

        Returns :
            float : the multiplier
        """
        return 1 + (self.sp_atk_current + self.sp_def_current) / 200
