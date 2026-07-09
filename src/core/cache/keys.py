def trip_search_key(source, destination, travel_date):
    return (
        f"trip_search"
        f"{source.strip().lower()}:"
        f"{destination.strip().lower()}"
        f"{travel_date}"
    )