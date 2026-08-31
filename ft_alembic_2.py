#!usr/bin/env python3

import alchemy.elements


if __name__ == "__main__":
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    out = alchemy.elements.create_earth()
    print(f"Testing create_earth: {out}")
