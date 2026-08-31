#!/usr/bin/env python3

import alchemy


if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    str_pot = alchemy.strength_potion()
    print(f"Testing strength_potion: {str_pot}")
    heal_pot = alchemy.heal()
    print(f"Testing heal alias: {heal_pot}")
