from fractions import Fraction
import math
#Triggy.1.1

def normal_triggy():

    angle_deg = float(input("\nEnter the known angle in degrees: "))
    if angle_deg <= 0 or angle_deg >= 90:
        print("Error: Angle must be between 0° and 90° for a right triangle.")
        return

    angle_rad = math.radians(angle_deg)

    print("\nWhich side do you already know?")
    print("1. Opposite")
    print("2. Adjacent")
    print("3. Hypotenuse")
    known_side = input("Pick 1, 2, or 3: ").strip()

    if known_side == "1":
        opp = float(input("Enter Opposite length: "))
        if opp <= 0:
            print("Error: Side length must be greater than 0.")
            return
        hyp = opp / math.sin(angle_rad)
        adj = opp / math.tan(angle_rad)
    elif known_side == "2":
        adj = float(input("Enter Adjacent length: "))
        if adj <= 0:
            print("Error: Side length must be greater than 0.")
            return
        hyp = adj / math.cos(angle_rad)
        opp = adj * math.tan(angle_rad)
    elif known_side == "3":
        hyp = float(input("Enter Hypotenuse length: "))
        if hyp <= 0:
            print("Error: Side length must be greater than 0.")
            return
        opp = hyp * math.sin(angle_rad)
        adj = hyp * math.cos(angle_rad)
    else:
        print("Invalid choice! Pick 1, 2, or 3.")
        return

    print(f"\n--- All Three Sides (for {angle_deg}°) ---")
    print(f"Opposite:   {round(opp, 4)}")
    print(f"Adjacent:   {round(adj, 4)}")
    print(f"Hypotenuse: {round(hyp, 4)}")

def reverse_triggy():

    sides = {
        "a": float(input("\nEnter length of side a: ")),
        "b": float(input("Enter length of side b: ")),
        "c": float(input("Enter length of side c: "))
    }

    if any(length <= 0 for length in sides.values()):
        print("\nError: All side lengths must be greater than 0.")
        return

    touching = input("Which two sides touch angle x? (e.g. 'ac' or 'bc'): ").lower().replace(" ", "")

    hyp_name = max(sides, key=sides.get)
    hyp = sides[hyp_name]

    all_names = {"a", "b", "c"}
    touching_set = set(touching)

    if len(touching_set) != 2 or not touching_set.issubset(all_names):
        print("\nError: Please enter two valid side letters like 'ac' or 'bc'.")
        return
    elif hyp_name not in touching_set:
        print("\nError: Angle x is the 90° right angle! Pick one of the two smaller corners.")
        return

    opp_name = (all_names - touching_set).pop()
    adj_name = (touching_set - {hyp_name}).pop()

    opp = sides[opp_name]
    adj = sides[adj_name]

    if not math.isclose(opp**2 + adj**2, hyp**2, rel_tol=1e-2):
        print("\nError: Those side lengths do not form a valid right triangle (a² + b² ≠ c²).")
        return

    print(f"\nAuto-detected -> Opposite: {opp_name} ({opp}), Adjacent: {adj_name} ({adj}), Hypotenuse: {hyp_name} ({hyp})")

    sin_f = Fraction(str(opp)) / Fraction(str(hyp))
    cos_f = Fraction(str(adj)) / Fraction(str(hyp))
    tan_f = Fraction(str(opp)) / Fraction(str(adj))
    angle_x = round(math.degrees(math.asin(opp / hyp)), 2)

    print(f"\nsin(x) = {sin_f}  ({round(opp / hyp, 4)})")
    print(f"cos(x) = {cos_f}  ({round(adj / hyp, 4)})")
    print(f"tan(x) = {tan_f}  ({round(opp / adj, 4)})")
    print(f"Angle x = {angle_x}°")

def main():
    while True:
        print("\n         Welcome To Triggy 1.1         ")
        print("---------------------------------------")
        print("1. normal_trig (finding sides)")
        print("2. reverse_trig (finding angles & ratios)")
        print("e. Exit")
        mode = input("\nType 1, 2, or e to pick: ").strip().lower()

        if mode == "e":
            print("Exiting Triggy 1.1. Goodbye!")
            break

        try:
            if mode == "1":
                normal_triggy()
            elif mode == "2":
                reverse_triggy()
            else:
                print("\nInvalid mode! Type 1, 2, or e.")
        except ValueError:
            print("\nOops! Make sure you enter valid numbers for angles and side lengths.")


if __name__ == "__main__":
    main()