from .. import Handler, Request


class Fire(Handler):
    def handle(self, request: Request) -> str | None:
        if request.emergency_type != "fire":
            return None
        return (
            f"Fire DEPARTMENT dispatched to {request.location}. "
            f"Reason: {request.description}"
        )
