from bike.providers import get_bike_data_stations, create_bike_extra, create_bike_stations


def data_injection_from_api():
    data = get_bike_data_stations()
    count = 0
    for i in range(len(data)):
        extra = create_bike_extra(data[i]['extra'])
        if not extra:
            continue
        count = count + 1
        data[i].pop('extra')
        station = create_bike_stations(extra,data[i])

    return count
