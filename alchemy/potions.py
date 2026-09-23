from elements import create_fire, create_water
from .elements import create_air, create_earth


def healing_potion() -> str:
    earth = create_earth()
    air = create_air()
    out = f"Healing potion brewed with '{earth}' and '{air}'"
    return out


def strength_potion() -> str:
    fire = create_fire()
    water = create_water()
    out = f"Strength potion brewed with '{fire}' and '{water}'"
    return out
