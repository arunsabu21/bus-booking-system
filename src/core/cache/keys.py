def trip_search_key(source, destination, travel_date):
    return (
        f"trip_search:"
        f"{source.strip().lower()}:"
        f"{destination.strip().lower()}:"
        f"{travel_date}"
    )


def cities_list_key():
    return "cities:list"


def operators_list_key():
    return "operators:list"


def get_routes_list_key():
    return "routes:list"


def get_buses_list_key():
    return "buses:list"


def trip_details_key(trip_id):
    return f"trip:{trip_id}"


def route_stops_key(route_id):
    return f"route:stops:{route_id}"