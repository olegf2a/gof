from .. import Handler, Request


class Police(Handler):
    def handle(self, request: Request) -> str | None:
        if request.emergency_type != "police":
            return None
        return (
            f"Police DEPARTMENT dispatched to {request.location}. "
            f"Reason: {request.description}"
        )
