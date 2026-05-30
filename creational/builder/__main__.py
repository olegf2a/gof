"""Demo script for Builder pattern - Custom Pizza Builder"""

from .pizza_builder import PizzaBuilder
from .pizza_with_builder import Pizza


def demo_inner_builder() -> None:
    """Demonstrate the inner-class Builder variant"""
    print("🍕 === Inner-class Builder Demo (Pizza.Builder) === 🍕\n")

    margherita = (
        Pizza.builder()
        .with_size("medium")
        .with_crust("thin")
        .with_topping("mozzarella")
        .with_topping("tomato sauce")
        .with_topping("basil")
        .build()
    )
    print(f"  {margherita}")
    print(f"  Price: ${margherita.get_price():.2f}\n")

    pepperoni = (
        Pizza.builder()
        .with_size("large")
        .with_crust("regular")
        .with_topping("mozzarella")
        .with_topping("pepperoni")
        .build()
    )
    print(f"  {pepperoni}")
    print(f"  Price: ${pepperoni.get_price():.2f}\n")


def main() -> None:
    """Demonstrate the Builder pattern with custom pizza creation"""
    print("🍕 === Custom Pizza Builder Demo === 🍕\n")

    # Create builder
    builder = PizzaBuilder()

    print("1. Building a Hawaiian Pizza:")
    print("-" * 40)

    # Build Hawaiian pizza (with pineapple and bacon)
    hawaiian_pizza = (
        builder.set_size("large")
        .set_crust("thin")
        .add_cheese("mozzarella")
        .add_bacon()
        .add_pineapple()
        .build()
    )

    print(f"🍕 {hawaiian_pizza}")
    print(f"💰 Price: ${hawaiian_pizza.get_price():.2f}\n")

    print("2. Building a Seafood Deluxe Pizza:")
    print("-" * 40)

    # Build seafood pizza
    seafood_pizza = (
        builder.set_size("medium")
        .set_crust("regular")
        .add_cheese("parmesan")
        .add_seafood("shrimp")
        .add_seafood("mussels")
        .add_mushrooms("shiitake mushrooms")
        .add_vegetables("bell peppers")
        .build()
    )

    print(f"🍕 {seafood_pizza}")
    print(f"💰 Price: ${seafood_pizza.get_price():.2f}\n")

    print("3. Building a Vegetarian Pizza:")
    print("-" * 40)

    # Build vegetarian pizza
    veggie_pizza = (
        builder.set_size("small")
        .set_crust("thick")
        .add_cheese("goat cheese")
        .add_mushrooms("portobello mushrooms")
        .add_vegetables("tomatoes")
        .add_vegetables("red onions")
        .add_vegetables("spinach")
        .build()
    )

    print(f"🍕 {veggie_pizza}")
    print(f"💰 Price: ${veggie_pizza.get_price():.2f}\n")

    print("4. Building a Meat Lovers Pizza:")
    print("-" * 40)

    # Build meat lovers pizza
    meat_pizza = (
        builder.set_size("large")
        .set_crust("regular")
        .add_cheese("cheddar")
        .add_bacon()
        .add_pepperoni()
        .add_custom_topping("sausage")
        .add_custom_topping("ham")
        .build()
    )

    print(f"🍕 {meat_pizza}")
    print(f"💰 Price: ${meat_pizza.get_price():.2f}\n")

    print("5. Inner-class Builder variant:")
    print("-" * 40)
    demo_inner_builder()

    print("6. Interactive Pizza Builder:")
    print("-" * 40)

    # Interactive demo
    interactive_demo()


def interactive_demo() -> None:
    """Interactive demo where user can build their own pizza"""
    builder = PizzaBuilder()

    print("Let's build your custom pizza!")

    # Get size
    while True:
        size = input("\nChoose size (small/medium/large): ").strip().lower()
        if size in ["small", "medium", "large"]:
            builder.set_size(size)
            break
        print("Invalid size. Please choose: small, medium, or large")

    # Get crust
    while True:
        crust = input("Choose crust (thin/regular/thick): ").strip().lower()
        if crust in ["thin", "regular", "thick"]:
            builder.set_crust(crust)
            break
        print("Invalid crust. Please choose: thin, regular, or thick")

    print("\nNow let's add toppings! (type 'done' when finished)")
    print("Available toppings:")
    print("- cheese (specify type, e.g., 'cheese mozzarella')")
    print("- bacon")
    print("- pineapple")
    print("- mushrooms (specify type, e.g., 'mushrooms button')")
    print("- seafood (specify type, e.g., 'seafood shrimp')")
    print("- pepperoni")
    print("- vegetables (specify type, e.g., 'vegetables tomatoes')")
    print("- custom (specify topping, e.g., 'custom olives')")

    while True:
        topping_input = input("\nAdd topping (or 'done' to finish): ").strip().lower()

        if topping_input == "done":
            break
        elif topping_input == "bacon":
            builder.add_bacon()
        elif topping_input == "pineapple":
            builder.add_pineapple()
        elif topping_input == "pepperoni":
            builder.add_pepperoni()
        elif topping_input.startswith("cheese"):
            parts = topping_input.split(maxsplit=1)
            cheese_type = parts[1] if len(parts) > 1 else "mozzarella"
            builder.add_cheese(cheese_type)
        elif topping_input.startswith("mushrooms"):
            parts = topping_input.split(maxsplit=1)
            mushroom_type = parts[1] if len(parts) > 1 else "button mushrooms"
            builder.add_mushrooms(mushroom_type)
        elif topping_input.startswith("seafood"):
            parts = topping_input.split(maxsplit=1)
            seafood_type = parts[1] if len(parts) > 1 else "shrimp"
            builder.add_seafood(seafood_type)
        elif topping_input.startswith("vegetables"):
            parts = topping_input.split(maxsplit=1)
            if len(parts) > 1:
                builder.add_vegetables(parts[1])
            else:
                print("Please specify vegetable type (e.g., 'vegetables tomatoes')")
                continue
        elif topping_input.startswith("custom"):
            parts = topping_input.split(maxsplit=1)
            if len(parts) > 1:
                builder.add_custom_topping(parts[1])
            else:
                print("Please specify custom topping (e.g., 'custom olives')")
                continue
        else:
            print(f"Unknown topping: {topping_input}. Try again or type 'done'.")
            continue

        # Show current pizza
        print(f"Current pizza: {builder.get_current_pizza_info()}")

    # Build the final pizza
    final_pizza = builder.build()

    print("\n🎉 Your custom pizza is ready! 🎉")
    print(f"🍕 {final_pizza}")
    print(f"💰 Total price: ${final_pizza.get_price():.2f}")


if __name__ == "__main__":
    main()
