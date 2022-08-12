"""Functions to structure data from dataset to fit into sql tables schema."""

# stand lib imports

# pip package imports
import pandas

# other imports


def structure_data(data_frame: object) -> object:
    """Structures data_frame.

    Args:
        data_frame(object): Pandas DataFrame object
    Returns:
        tables_object(object): Object containing structured Pandas DataFrames
    """
    order = structure_order(data_frame)
    family = structure_family(data_frame, order)
    genus = structure_genus(data_frame, family)
    pop_trend = structure_pop_trend(data_frame)
    iucn = structure_iucn(data_frame)
    parity_mode = structure_parity_mode(data_frame)
    micro_habitat = structure_micro_habitat(data_frame)
    activity = structure_activity(data_frame)
    nesting_site = structure_nesting_site(data_frame)
    species = structure_species(data_frame, genus, parity_mode, iucn, pop_trend)
    nesting_site_species = structure_nesting_site_species(
        data_frame, species, nesting_site
    )
    activity_species = structure_activity_species(data_frame, species, activity)
    micro_habitat_species = structure_micro_habitat_species(
        data_frame, species, micro_habitat
    )
    spec_df, continent, country, geo_location = structure_geo_location(
        data_frame, species
    )
    geo_location_species = structure_geo_location_species(spec_df, geo_location)

    tables_object = {
        "order_taxon": order,
        "family": family,
        "genus": genus,
        "pop_trend": pop_trend,
        "iucn": iucn,
        "parity_mode": parity_mode,
        "micro_habitat": micro_habitat,
        "activity": activity,
        "nesting_site": nesting_site,
        "species": species,
        "nesting_site_species": nesting_site_species,
        "activity_species": activity_species,
        "micro_habitat_species": micro_habitat_species,
        "continent": continent,
        "country": country,
        "geo_location": geo_location,
        "geo_location_species": geo_location_species,
    }

    return tables_object


def structure_order(data_frame: object) -> object:
    """Structures data for Order table.

    Args:
        data_frame(object): Pandas DataFrame object
    Returns:
        order_data_frame(object):Pandas DataFrame object with order data
    """
    print("Order")
    order = data_frame["Order"].dropna().unique()
    df = pandas.DataFrame(order, columns=["order_taxon_name"])
    return df


def structure_family(data_frame: object, order: object) -> object:
    """Structures data for Family table.

    Args:
        data_frame(object): Pandas DataFrame object
    Returns:
        family_data_frame(object):Pandas DataFrame object with Family data
    """
    print("Family")

    fam = data_frame[["Order", "Family"]]
    fam["Ind"] = fam["Order"].map(
        lambda x: str(order.index[order["order_taxon_name"] == x].tolist()[0] + 1)
    )

    fam["OrderFam"] = fam["Family"] + "+" + fam["Ind"]
    uni = [x.split("+") for x in fam["OrderFam"].dropna().unique()]

    a = []
    b = []

    for x in uni:
        a.append(x[0])
        b.append(x[1])

    df = pandas.DataFrame({"family_name": a, "order_id": b})

    return df


def structure_genus(data_frame: object, family: object) -> object:
    """Structures data for Genus table.

    Args:
        data_frame(object): Pandas DataFrame object
        family(object): Pandas DataFrame object
    Returns:
        genus_data_frame(object):Pandas DataFrame object with Genus data
    """
    print("Genus")

    genus = data_frame[["Family", "Genus"]]
    genus["Ind"] = genus["Family"].map(
        lambda x: str(family.index[family["family_name"] == x].tolist()[0] + 1)
    )

    genus["GenFam"] = genus["Genus"] + "+" + genus["Ind"]
    uni = [x.split("+") for x in genus["GenFam"].dropna().unique()]

    a = []
    b = []

    for x in uni:
        a.append(x[0])
        b.append(x[1])

    df = pandas.DataFrame({"genus_name": a, "family_id": b})

    return df


def structure_pop_trend(data_frame: object) -> object:
    """Structures data for pop_trend table.

    Args:
        data_frame(object): Pandas DataFrame object
    Returns:
        pop_trend_frame(object):Pandas DataFrame object with pop_trend data
    """
    print("PopTrend")

    pop_trend = data_frame["PopTrend"].dropna().unique()
    df = pandas.DataFrame(pop_trend, columns=["pop_trend_status"])
    return df


def structure_iucn(data_frame: object) -> object:
    """Structures data for IUCN table.

    Args:
        data_frame(object): Pandas DataFrame object
    Returns:
        IUCN_frame(object):Pandas DataFrame object with IUCN data
    """
    print("IUCN")

    iucn = data_frame["IUCN"].dropna().unique()
    df = pandas.DataFrame(iucn, columns=["iucn_status"])
    return df


def structure_parity_mode(data_frame: object) -> object:
    """Structures data for Parity table.

    Args:
        data_frame(object): Pandas DataFrame object
    Returns:
        IUCN_frame(object):Pandas DataFrame object with Parity data
    """
    print("Parity")

    parity_mode = data_frame["ParityMode"].dropna().unique()
    df = pandas.DataFrame(parity_mode, columns=["parity_mode_desc"])
    return df


def structure_continent(data_frame: object) -> object:
    """Structures data for Continent table.

    Args:
        data_frame(object): Pandas DataFrame object
    Returns:
        Continent_frame(object):Pandas DataFrame object with Continent data
    """


def structure_country(data_frame: object, continent: object) -> object:
    """Structures data for Country table.

    Args:
        data_frame(object): Pandas DataFrame object
        continent(object): Pandas DataFrame object

    Returns:
        Country_frame(object):Pandas DataFrame object with Country data
    """


def structure_geo_location(data_frame: object, species: object) -> object:
    """Structures data for geo_location table.

    Args:
        data_frame(object): Pandas DataFrame object
        species(object): Pandas DataFrame object

    Returns:
        geo_location_frame(object):Pandas DataFrame object with geo_location data
    """
    print("Geo Location")

    # geo dataframe
    geolocation = data_frame[["Species", "FormattedGeographicRegion"]]
    geolocation["SpecInd"] = geolocation["Species"].map(
        lambda x: str(species.index[species["species_name_latin"] == x].tolist()[0] + 1)
    )

    print("Split Lines")
    # process lines
    results = []
    for row in geolocation.iterrows():
        vals = []
        for value in row:
            if isinstance(value, int):
                vals.append(value)
            else:
                vals = [*vals, *value.values]

        species = vals[1]
        locations_strs = vals[2].split("/")
        species_ind = vals[3]

        for location_str in locations_strs:
            parts = location_str.split("_")
            results.append([species_ind, *parts])

    species = []
    continent = []
    country = []
    region = []
    latitude = []
    longitude = []
    country_code = []

    print("Lines to new dataframe")
    for x in results:
        species.append(x[0])
        continent.append(x[1])
        country.append(x[2])
        region.append(x[3])
        latitude.append(x[4])
        longitude.append(x[5])
        country_code.append(x[6])

    # new base dataframe
    df = pandas.DataFrame(
        {
            "species_index": species,
            "continent": continent,
            "country": country,
            "region": region,
            "latitude": latitude,
            "longitude": longitude,
            "country_code": country_code,
        }
    )

    print("create continent")
    # continent dataframe
    continent_sp = df["continent"].dropna().unique()
    continent_df = pandas.DataFrame(continent_sp, columns=["continent_name"])

    print("creart country")
    # country
    country_sp = df[["continent", "country"]]
    country_sp["Ind"] = country_sp["continent"].map(
        lambda x: str(
            continent_df.index[continent_df["continent_name"] == x].tolist()[0] + 1
        )
    )
    country_sp["contcount"] = country_sp["country"] + "+" + country_sp["Ind"]
    uni = [x.split("+") for x in country_sp["contcount"].dropna().unique()]

    a = []
    b = []

    for x in uni:
        a.append(x[0])
        b.append(x[1])

    country_df = pandas.DataFrame({"country_name": a, "continent_id": b})

    # geo_location
    print("create geolocation")
    geo_sp = df[["region", "country", "latitude", "longitude"]]
    geo_sp["Ind"] = geo_sp["country"].map(
        lambda x: str(country_df.index[country_df["country_name"] == x].tolist()[0] + 1)
    )
    geo_sp["countreglatlon"] = "+".join(
        [geo_sp["region"], geo_sp["latitude"], geo_sp["longitude"], geo_sp["Ind"]]
    )
    uni = [x.split("+") for x in geo_sp["countreglatlon"].dropna().unique()]

    a = []
    b = []
    c = []
    d = []

    for x in uni:
        a.append(x[0])
        b.append(x[1] if str(x[1]) != "None" else None)
        c.append(x[2] if str(x[2]) != "None" else None)
        d.append(x[3])

    geolocation_df = pandas.DataFrame(
        {"region_name": a, "latitude": b, "longitude": c, "country_id": d}
    )

    return [df, continent_df, country_df, geolocation_df]


def structure_geo_location_species(data_frame: object, geo_location: object) -> object:
    """Structures data for geo_location table.

    Args:
        data_frame(object): Pandas DataFrame object
        species(object): Pandas DataFrame object

    Returns:
        geo_location_frame(object):Pandas DataFrame object with geo_location data
    """
    loc_spec = data_frame[["species_index", "region"]]
    loc_spec["geo_id"] = loc_spec["region"].map(
        lambda x: str(
            geo_location.index[geo_location["region_name"] == x].tolist()[0] + 1
        )
    )
    loc_spec["geo_spec"] = loc_spec["geo_id"] + "+" + loc_spec["species_index"]
    uni = [x.split("+") for x in loc_spec["geo_spec"].dropna().unique()]

    a = []
    b = []

    for x in uni:
        a.append(x[0])
        b.append(x[1])

    df = pandas.DataFrame({"geo_location_id": a, "species_id": b})

    return df


def structure_micro_habitat(data_frame: object) -> object:
    """Structures data for micro_habitat table.

    Args:
        data_frame(object): Pandas DataFrame object

    Returns:
        micro_habitat_frame(object):Pandas DataFrame object with micro_habitat data
    """
    print("Habitat")

    micro = data_frame["Microhabitat"].dropna().unique()
    df = pandas.DataFrame(micro, columns=["micro_habitat_name"])
    return df


def structure_activity(data_frame: object) -> object:
    """Structures data for activity table.

    Args:
        data_frame(object): Pandas DataFrame object

    Returns:
        activity_frame(object):Pandas DataFrame object with activity data
    """
    print("Activity")

    activity = data_frame["Activity"].dropna().unique()
    df = pandas.DataFrame(activity, columns=["activity_kind"])
    return df


def structure_nesting_site(data_frame: object) -> object:
    """Structures data for nesting_site table.

    Args:
        data_frame(object): Pandas DataFrame object

    Returns:
        nesting_site_frame(object):Pandas DataFrame object with nesting_site data
    """
    print("Nesting")

    nesting_site = data_frame["NestingSite"].dropna().unique()
    df = pandas.DataFrame(nesting_site, columns=["nesting_site_desc"])
    return df


def structure_species(
    data_frame: object,
    genus: object,
    parity_mode: object,
    iucn: object,
    pop_trend: object,
) -> object:
    """Structures data for species table.

    Args:
        data_frame(object): Pandas DataFrame object
        genus(object): Pandas DataFrame object
        parity_mode(object): Pandas DataFrame object
        iucn(object): Pandas DataFrame object
        pop_trend(object): Pandas DataFrame object

    Returns:
        species_frame(object):Pandas DataFrame object with species data
    """
    print("Struct Spec")

    print(data_frame["ElevationMin"].head())

    species = data_frame[
        [
            "Species",
            "SVLMMx",
            "SVLFMx",
            "SVLMx",
            "Longevity",
            "ClutchMin",
            "ClutchMax",
            "Clutch",
            "EggDiameter",
            "RangeSize",
            "ElevationMin",
            "ElevationMax",
            "Elevation",
            "ParityMode",
            "PopTrend",
            "IUCN",
            "Genus",
        ]
    ]

    species["Genus"] = species["Genus"].map(
        lambda x: str(genus.index[genus["genus_name"] == x].tolist()[0] + 1)
        if x != ""
        else x
    )

    def iucn_check(x):
        return (
            str(iucn.index[iucn["iucn_status"] == x].tolist()[0] + 1)
            if x is not None
            else x
        )

    species["IUCN"] = species["IUCN"].map(lambda x: iucn_check(x))

    species["PopTrend"] = species["PopTrend"].map(
        lambda x: str(
            pop_trend.index[pop_trend["pop_trend_status"] == x].tolist()[0] + 1
        )
        if x is not None
        else x
    )

    species["ParityMode"] = species["ParityMode"].map(
        lambda x: str(
            parity_mode.index[parity_mode["parity_mode_desc"] == x].tolist()[0] + 1
        )
        if x is not None
        else x
    )

    species.insert(13, "img_url_female", "")
    species.insert(14, "img_url_male", "")
    species.insert(15, "verif_status", True)

    print(species["ElevationMin"].head())

    species.columns = [
        "species_name_latin",
        "size_max_male",
        "size_max_female",
        "size_max_record",
        "longevity",
        "clutch_min",
        "clutch_max",
        "clutch_avg",
        "egg_diameter",
        "range_size",
        "elevation_min",
        "elevation_max",
        "elevation_avg",
        "img_uri_female",
        "img_uri_male",
        "verif_status",
        "parity_mode_id",
        "pop_trend_id",
        "iucn_id",
        "genus_id",
    ]

    print(species["elevation_min"].head())

    return species


def structure_micro_habitat_species(
    data_frame: object, species: object, micro_habitat: object
) -> object:
    """Structures data for micro_habitiat_species table.

    Args:
        data_frame(object): Pandas DataFrame object
        species(object): Pandas DataFrame object
        micro_habitat(object): Pandas DataFrame object

    Returns:
        micro_habitat_species_frame(object):Pandas DataFrame object with m_h_s data
    """
    print("hab spec")
    print(species["elevation_min"].head())

    print(micro_habitat)
    micro_habitat_species = data_frame[["Species", "Microhabitat"]]
    print("spec")
    micro_habitat_species["species_index"] = micro_habitat_species["Species"].map(
        lambda x: str(species.index[species["species_name_latin"] == x].tolist()[0] + 1)
    )

    print("hab")

    def hab(x):
        b = (
            micro_habitat.index[micro_habitat["micro_habitat_name"] == x].tolist()
            if x is not None or x != "nan"
            else x
        )
        if len(b) > 0:
            a = str(b[0] + 1)
        else:
            a = None
        return a

    micro_habitat_species["habitat_index"] = micro_habitat_species["Microhabitat"].map(
        lambda x: hab(x)
    )

    print(micro_habitat_species["habitat_index"].value_counts())

    micro_habitat_species["spec_ind_hab_ind"] = "+".join(
        [
            micro_habitat_species["species_index"],
            micro_habitat_species["habitat_index"].dropna(),
        ]
    )

    uni = [
        x.split("+")
        for x in micro_habitat_species["spec_ind_hab_ind"].dropna().unique()
    ]

    a = []
    b = []

    for x in uni:
        a.append(x[0])
        b.append(x[1])

    df = pandas.DataFrame({"species_id": a, "micro_habitat_id": b})

    return df


def structure_nesting_site_species(
    data_frame: object, species: object, nesting_site: object
) -> object:
    """Structures data for nesting_site_species table.

    Args:
        data_frame(object): Pandas DataFrame object
        species(object): Pandas DataFrame object
        nesting_site(object): Pandas DataFrame object

    Returns:
        nesting_site_species_frame(object):Pandas DataFrame object with data
    """
    print("nest spec")
    print(species["elevation_min"].head())

    nesting_site_species = data_frame[["Species", "NestingSite"]]

    nesting_site_species["species_index"] = nesting_site_species["Species"].map(
        lambda x: str(species.index[species["species_name_latin"] == x].tolist()[0] + 1)
    )

    nesting_site_species["nesting_site_index"] = nesting_site_species[
        "NestingSite"
    ].map(
        lambda x: str(
            nesting_site.index[nesting_site["nesting_site_desc"] == x].tolist()[0] + 1
        )
        if x is not None
        else x
    )

    nesting_site_species["spec_ind_hab_ind"] = "+".join(
        [
            nesting_site_species["species_index"],
            nesting_site_species["nesting_site_index"].dropna(),
        ]
    )

    uni = [
        x.split("+") for x in nesting_site_species["spec_ind_hab_ind"].dropna().unique()
    ]

    a = []
    b = []

    for x in uni:
        a.append(x[0])
        b.append(x[1])

    df = pandas.DataFrame({"species_id": a, "nesting_site_id": b})

    return df


def structure_activity_species(
    data_frame: object, species: object, nesting_site: object
) -> object:
    """Structures data for activity_species table.

    Args:
        data_frame(object): Pandas DataFrame object
        species(object): Pandas DataFrame object
        nesting_site(object): Pandas DataFrame object

    Returns:
        activity_species_frame(object):Pandas DataFrame object with data
    """
    print("act spec")
    print(species["elevation_min"].head())

    activity_species = data_frame[["Species", "Activity"]]

    activity_species["species_index"] = activity_species["Species"].map(
        lambda x: str(species.index[species["species_name_latin"] == x].tolist()[0] + 1)
    )

    activity_species["activity_index"] = activity_species["Activity"].map(
        lambda x: str(
            nesting_site.index[nesting_site["activity_kind"] == x].tolist()[0] + 1
        )
        if x is not None
        else x
    )

    activity_species["spec_ind_hab_ind"] = "+".join(
        [activity_species["species_index"], activity_species["activity_index"].dropna()]
    )

    uni = [x.split("+") for x in activity_species["spec_ind_hab_ind"].dropna().unique()]

    a = []
    b = []

    for x in uni:
        a.append(x[0])
        b.append(x[1])

    df = pandas.DataFrame({"species_id": a, "activity_id": b})

    return df
