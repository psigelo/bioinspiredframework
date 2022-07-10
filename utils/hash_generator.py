from datetime import datetime as dt


def create_hash(prefix_text="") -> int:
    return hash(prefix_text + str(dt.now()))
