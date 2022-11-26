from random import SystemRandom

from modules import events


def generate_random_funnel(user_id: int, session_id: str) -> list:
    funnel = SystemRandom().choice((funnel_a, funnel_b, funnel_c, funnel_d))
    event_list = [
        {
            "core": data_json,
            "user": {
                "user_id": user_id,
                "session_id": session_id
            }
        }
        for data_json in funnel()
    ]

    return event_list

# Funnel List
def funnel_a() -> list:
    # > Home (x)
    return [events.open_home()]

def funnel_b() -> list:
    # > Home > Product (x)
    return [
        events.open_home(),
        events.open_product()
    ]
    
def funnel_c() -> list:
    # > Home > Product > Checkout (X)
    return [
        events.open_home(),
        events.open_product(),
        events.open_checkout()
    ]

def funnel_d() -> list:
    # > Home > Product > Checkout > Payment (X)
    return [
        events.open_home(),
        events.open_product(),
        events.open_checkout(),
        events.open_payment()
    ]
