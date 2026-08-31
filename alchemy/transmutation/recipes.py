from .. import potions
import alchemy.elements
import elements


def lead_to_gold() -> str:
    air = alchemy.elements.create_air()
    str_pot = potions.strength_potion()
    fire = elements.create_fire()
    out = (f"Recipe transmuting Lead to Gold: brew '{air}' and "
           f"'{str_pot}' mixed with '{fire}'")
    return out
