"""Read From DB."""


def read_from_db(params: dict):
    conn = create_connection()
    query = build_query(params)
    results = query_db(conn, query)
    return results


def create_connection():
    pass


def build_query(params):

    sql = f"""
    SELECT {", ".join(params['columns'])} FROM species
    JOIN
    JOIN
    JOIN
    JOIN
    JOIN
    WHERE

    """


def query_db(conn, query):
    pass
