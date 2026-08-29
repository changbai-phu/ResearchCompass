from dataclasses import dataclass

@dataclass
class Message:      # a single structured chat message payload object
    role: str       # e.g, system or user
    content: str    # actual textual message body content