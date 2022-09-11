import report_generator.read_from_db.query_db as qd
from report_generator.excel_extraction.excel_to_sql import create_connection


def test_read_from_db():
    df = qd.read_from_db({})
    assert len(df.index) == 8249


def test_get_query_options():
    qo = qd.get_query_options({})
    assert qo == {}


def test_build_query():
    qs = qd.build_query({})
    assert qs != """"""
    assert "order_taxon_name as 'Order'" in qs


def test_build_where_statements():
    where = qd.build_where_statements("key", "1234")
    assert where == "key = 1234"


def test_query_db():
    conn = create_connection("/home/cush/testproj/data/database/species.db")
    query = qd.build_query({})
    df = qd.query_db(conn, query)
    assert len(df.index) == 8249
