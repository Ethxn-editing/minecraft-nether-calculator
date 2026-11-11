"""Minecraft Nether Portal Calculator.

Un semplice tool per convertire le coordinate tra Overworld e Nether.
"""


def overworld_to_nether(x: float, z: float) -> tuple[int, int]:
    """Converte le coordinate dall'Overworld al Nether."""
    return round(x / 8), round(z / 8)


def nether_to_overworld(x: float, z: float) -> tuple[int, int]:
    """Converte le coordinate dal Nether all'Overworld."""
    return round(x * 8), round(z * 8)


def main():
    print("====================================")
    print("   MINECRAFT NETHER PORTAL TOOL     ")
    print("====================================\n")

    print("Scegli il tipo di conversione:")
    print("1. Da Overworld a Nether")
    print("2. Da Nether a Overworld")

    scelta = input("\nInserisci 1 o 2: ").strip()

    if scelta not in ["1", "2"]:
        print("Scelta non valida! Riavvia il programma.")
        return

    try:
        coord_x = float(input("Inserisci la coordinata X: "))
        coord_z = float(input("Inserisci la coordinata Z: "))
        coord_y = input(
            "Inserisci l'altezza Y (opzionale, premi Invio per saltare): "
        )

        y_str = f", Y={coord_y}" if coord_y.strip() else ""

        if scelta == "1":
            nx, nz = overworld_to_nether(coord_x, coord_z)
            print(
                f"\n[RISULTATO] Posiziona il portale nel NETHER a: X={nx}{y_str}, Z={nz}"
            )
        else:
            ox, oz = nether_to_overworld(coord_x, coord_z)
            print(
                f"\n[RISULTATO] Posiziona il portale nell'OVERWORLD a: X={ox}{y_str}, Z={oz}"
            )

    except ValueError:
        print("\nErrore: inserisci solo numeri validi per le coordinate!")


if __name__ == "__main__":
    main()