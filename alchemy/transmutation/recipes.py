from ..potions import strength_potion
from alchemy.elements import create_air
import elements


def lead_to_gold() -> str:
    air = create_air()
    str_pot = strength_potion()
    fire = elements.create_fire()
    out = (f"Recipe transmuting Lead to Gold: brew '{air}' and "
           f"'{str_pot}' mixed with '{fire}'")
    return out
