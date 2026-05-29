from .chain import Chain
from .handlers import Fire, Medical, Police
from .request import Request


def demo() -> None:
    print("=== Chain of Responsibility — Emergency Dispatcher ===\n")

    chain = Chain([Fire(), Police(), Medical()])

    requests = [
        Request("fire", "Main St", "Building on fire"),
        Request("police", "Broadway", "Robbery in progress"),
        Request("medical", "Park Ave", "Heart attack"),
    ]

    print("--- Dispatching emergencies ---")
    for req in requests:
        result = chain.call_service(req)
        print(f"  [{req.emergency_type.upper()}] {result}")

    print("\n--- Unknown type raises ValueError ---")
    try:
        chain.call_service(Request("unknown", "Somewhere", "Mystery incident"))
    except ValueError as e:
        print(f"  Error: {e}")

    print("\n--- Dynamic chain extension ---")
    small_chain = Chain([Fire()])
    print(f"  Chain has only Fire handler")
    try:
        small_chain.call_service(Request("police", "Broadway", "Robbery"))
    except ValueError as e:
        print(f"  Police request failed: {e}")
    small_chain.add_handler(Police())
    result = small_chain.call_service(Request("police", "Broadway", "Robbery"))
    print(f"  After add_handler(Police()): {result}")


if __name__ == "__main__":
    demo()
