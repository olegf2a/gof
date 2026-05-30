from .. import Handler, Request


class Medical(Handler):
    def handle(self, request: Request) -> str | None:
        if request.emergency_type != "medical":
            return None
        return (
            f"Medical DEPARTMENT dispatched to {request.location}. "
            f"Reason: {request.description}"
        )
