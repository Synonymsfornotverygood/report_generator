import pandas
import pytest

from report_generator.excel_extraction import clean_data


def test_create_data_frame_none():
    df = clean_data.create_data_frame("nonexsistpath")
    assert df is None


def test_create_data_frame():
    df = clean_data.create_data_frame(
        "/home/cush/GABiP DATABASE_V5_06.July.2022-1.xlsx"
    )
    assert type(df) == pandas.DataFrame


def test_clean_data():
    data_frame = clean_data.create_data_frame(
        "/home/cush/GABiP DATABASE_V5_06.July.2022-1.xlsx"
    )
    clean_df = clean_data.clean_data(data_frame)
    assert len(data_frame.index) == 8251
    assert len(clean_df.index) == 8249


def test_remove_duplicates():
    pass
    # data_frame =  clean_data.create_data_frame("/home/cush/GABiP DATABASE_V5_06.July.2022-1.xlsx")
    # removed_dups = clean_data.remove_duplicates(data_frame)
    # assert len(removed_dups.index) == 8249


def test_main():
    with pytest.raises(AttributeError) as e:
        clean_data.main("nonexsistfile", "nonexistfile")
