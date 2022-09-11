import report_generator.excel_extraction.excel_to_sql as es
import report_generator.location_formatter.location_updater as lu

data_frame = es.create_data_frame("/home/cush/GABiP DATABASE_V5_06.July.2022-1.xlsx")
locations_data = lu.load_locations_data()


def test_update_location():
    df = lu.update_location(data_frame)
    assert "FormattedGeographicRegion" in list(df.columns)


def test_update_location_entries():
    df = lu.update_location_entries(data_frame, locations_data)
    assert "FormattedGeographicRegion" in list(df.columns)


def test_location_entry():
    pass


def test_load_location_json():
    pass


def test_load_locations_data():
    pass


def test_update_locations_unknowns():
    pass


def test_update_locations_data():
    pass


def test_search_for_unknowns():
    pass


def test_save_locations_data():
    pass
