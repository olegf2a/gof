from .army import Army
from .factory import FlyweightFactory
from .unit import Unit


def demo() -> None:
    print("=== Flyweight demo — Game Units ===\n")

    factory = FlyweightFactory()

    army = Army()
    army.add(Unit(x=0, y=0, flyweight=factory.get("tank")))
    army.add(Unit(x=5, y=0, flyweight=factory.get("infantry")))
    army.add(Unit(x=10, y=0, flyweight=factory.get("infantry")))
    army.add(Unit(x=15, y=0, flyweight=factory.get("tank")))

    tank_fw = factory.get("tank")
    inf_fw = factory.get("infantry")
    print(f"Flyweight objects in memory: 2")
    print(
        f"  factory.get('tank') is factory.get('tank') → {tank_fw is factory.get('tank')}"
    )
    print(
        f"  factory.get('infantry') is factory.get('infantry') → {inf_fw is factory.get('infantry')}"
    )

    print("\n--- Before move ---")
    army.render_all()

    print("\n--- move_all(10, 5) ---")
    army.move_all(10, 5)
    army.render_all()


if __name__ == "__main__":
    demo()
