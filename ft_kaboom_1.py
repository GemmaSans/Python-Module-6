#!/usr/bin/env python3


if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    import alchemy.grimoire.dark_spellbook as dark_spellbook
    spell = dark_spellbook.dark_spell_record("Fantasy",
                                             "Earth, wind and fire")
