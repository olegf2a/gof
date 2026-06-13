from .pizza_oven import PizzaOven


def demo() -> None:
    print("=== State Pattern — Pizza Oven ===\n")

    oven = PizzaOven()
    print(f"Initial state: {oven.state_name}")

    print("\n--- Heat up ---")
    oven.heat_up()
    print(f"State: {oven.state_name}")

    print("\n--- Bake a Margherita ---")
    oven.bake("Margherita")

    print("\n--- Bake a Pepperoni ---")
    oven.bake("Pepperoni")

    print("\n--- Overheat ---")
    oven.heat_up()
    print(f"State: {oven.state_name}")

    print("\n--- Try to bake while overheated ---")
    try:
        oven.bake("Quattro Formaggi")
    except RuntimeError as e:
        print(f"  RuntimeError: {e}")

    print("\n--- Cool down to Ready ---")
    oven.cool_down()
    print(f"State: {oven.state_name}")

    print("\n--- Bake after cooling ---")
    oven.bake("Diavola")

    print("\n--- Cool down to Cold ---")
    oven.cool_down()
    print(f"State: {oven.state_name}")

    print("\n--- Try to bake while cold ---")
    try:
        oven.bake("Marinara")
    except RuntimeError as e:
        print(f"  RuntimeError: {e}")

    print("\n--- Try to cool down when already cold ---")
    try:
        oven.cool_down()
    except RuntimeError as e:
        print(f"  RuntimeError: {e}")

    print("\n--- Try to overheat when already overheated ---")
    oven.heat_up()
    oven.heat_up()
    try:
        oven.heat_up()
    except RuntimeError as e:
        print(f"  RuntimeError: {e}")


if __name__ == "__main__":
    demo()
