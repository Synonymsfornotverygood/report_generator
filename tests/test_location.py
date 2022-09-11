import report_generator.location_formatter.location as l


def test_location():
    location = l.Location()
    assert type(location) == l.Location


def test_location_get_location_obj():
    location = l.Location()
    ld = location.get_location_obj()

    assert ld == {
        "region": "NoRegion",
        "country": "NoCountry",
        "country_code": "",
        "continent": "NoContinent",
        "latitude": None,
        "longitude": None,
        "country_full_name": "",
    }


def test_location_str():
    location = l.Location()
    assert str(location) == "Nocontinent_Nocountry_Noregion_None_None_"
