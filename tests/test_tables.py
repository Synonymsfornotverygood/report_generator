import report_generator.excel_extraction.tables as t


def test_get_tables_sql():
    sql = t.get_tables_sql()
    assert len(sql) == 19
