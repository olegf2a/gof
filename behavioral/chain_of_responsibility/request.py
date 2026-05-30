from dataclasses import dataclass


@dataclass
class Request:
    emergency_type: str
    location: str
    description: str
