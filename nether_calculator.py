"""Minecraft Nether Portal Calculator.

A simple tool to convert coordinates between the Overworld and the Nether.
"""


def overworld_to_nether(overworld_x: float, overworld_z: float) -> tuple[int, int]:
    """Converts coordinates from Overworld to Nether."""
    nether_x = round(overworld_x / 8)
    nether_z = round(overworld_z / 8)
    return nether_x, nether_z


def nether_to_overworld(nether_x: float, nether_z: float) -> tuple[int, int]:
    """Converts coordinates from Nether to Overworld."""
    overworld_x = round(nether_x * 8)
    overworld_z = round(nether_z * 8)
    return overworld_x, overworld_z


def main():
    print("====================================")
    print("   MINECRAFT NETHER PORTAL TOOL     ")
    print("====================================\n")

    print("Choose conversion type:")
    print("1. Overworld to Nether")
    print("2. Nether to Overworld")

    choice = input("\nEnter 1 or 2: ").strip()

    if choice not in ["1", "2"]:
        print("Invalid choice! Please restart the program.")
        return

    try:
        coord_x = float(input("Enter X coordinate: "))
        coord_z = float(input("Enter Z coordinate: "))
        coord_y = input("Enter Y height (optional, press Enter to skip): ").strip()

        y_str = f", Y={coord_y}" if coord_y else ""

        if choice == "1":
            nx, nz = overworld_to_nether(coord_x, coord_z)
            print(f"\n[RESULT] Place portal in the NETHER at: X={nx}{y_str}, Z={nz}")
        else:
            ox, oz = nether_to_overworld(coord_x, coord_z)
            print(f"\n[RESULT] Place portal in the OVERWORLD at: X={ox}{y_str}, Z={oz}")

    except ValueError:
        print("\nError: Please enter only valid numbers for coordinates!")


if __name__ == "__main__":
    main()
