#!usr/bin/env python3

import alchemy


if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    out = alchemy.create_air()
    print(f"Testing create_air: {out}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    out = alchemy.create_earth()
    print(f"Testing the hidden create_earth: {out}")
