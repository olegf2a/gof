from .handler import Handler
from .request import Request


class Chain:
    def __init__(self, handlers: list[Handler]) -> None:
        self._handlers = handlers

    def add_handler(self, handler: Handler) -> None:
        self._handlers.append(handler)

    def call_service(self, request: Request) -> str:
        for handler in self._handlers:
            response = handler.handle(request)
            if response is not None:
                return response
        raise ValueError(
            f"No handler found for emergency type: '{request.emergency_type}'"
        )
