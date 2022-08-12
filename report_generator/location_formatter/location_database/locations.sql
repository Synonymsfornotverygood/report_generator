CREATE TABLE IF NOT EXISTS country_codes (
    country_code_id integer NOT NULL AUTOINCREMENT PRIMARY KEY
    continent_name VARCHAR(50) NOT NULL,
    continent_code VARCHAR(4) NOT NULL,
    country_name VARCHAR(50) NOT NULL,
    two_letter_country_code VARCHAR(2),
    three_letter_country_code VARCHAR(3),
    country_number integer NOT NULL
)

CREATE TABLE IF NOT EXISTS geocode (
    geoname_id INT NOT NULL PRIMARY KEY,
    place_name VARCHAR(50),
    ascii_name TEXT,
    alternate_names TEXT,
    latitude REAL,
    longitude REAL,
    feature_class TEXT,
    feature_code TEXT,
    country_code TEXT,
    cc2 TEXT,
    admin1_code TEXT,
    admin2_code TEXT,
    admin3_code TEXT,
    admin4_code TEXT,
    population_info integer,
    elevation integer,
    dem integer,
    timezone TEXT,
    modification TEXT
)
