import elements
import alchemy.elements


def healing_potion() -> str:
    earth = alchemy.elements.create_earth()
    air = alchemy.elements.create_air()
    out = f"Healing potion brewed with '{earth}' and '{air}'"
    return out


def strength_potion() -> str:
    fire = elements.create_fire()
    water = elements.create_water()
    out = f"Strength potion brewed with '{fire}' and '{water}'"
    return out
