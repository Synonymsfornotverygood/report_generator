# import pytest
# import pandas

# from report_generator.excel_extraction import data_structure
# from report_generator.read_from_db import query_db


# data_frame =  query_db.read_from_db({})
# ord = data_structure.structure_order(data_frame)
# fam = data_structure.structure_family(data_frame, ord)
# gen = data_structure.structure_genus(data_frame, fam)
# pm = data_structure.structure_parity_mode(data_frame)
# ic = data_structure.structure_iucn(data_frame)
# pt = data_structure.structure_pop_trend(data_frame)
# sp = data_structure.structure_species(data_frame, gen, pm, ic, pt)
# mc = data_structure.structure_micro_habitat(data_frame)
# act = data_structure.structure_activity(data_frame)
# ns = data_structure.structure_nesting_site(data_frame)

# @pytest.mark.filterwarnings('ignore::RuntimeWarning')

# # def test_structure_data():
# #     sd = data_structure.structure_data(data_frame)
# #     assert type(sd) == dict

# def test_structure_order():
#     so = data_structure.structure_order(data_frame)
#     assert list(so.columns) == ["order_taxon_name"]

# def test_structure_family():
#     so = data_structure.structure_family(data_frame, ord)
#     assert list(so.columns) == ["family_name", "order_id"]

# def test_structure_genus():
#     so = data_structure.structure_genus(data_frame, fam)
#     assert list(so.columns) == ["genus_name", "family_id"]

# def test_structure_pop_trend():
#     so = data_structure.structure_pop_trend(data_frame)
#     assert list(so.columns) == ["pop_trend_status"]

# def test_structure_iucn():
#     so = data_structure.structure_iucn(data_frame)
#     assert list(so.columns) == ["iucn_status"]

# def test_structure_parity_mode():
#     so = data_structure.structure_parity_mode(data_frame)
#     assert list(so.columns) == ["parity_mode_desc"]

# def test_structure_geo_location():
#     # sp = data_structure.structure_species(data_frame)
#     # gp = data_structure.structure_genus(data_frame)
#     # gl = data_structure.structure_geo_location(data_frame, sp, gp)

#     # assert len(gl) == 4
#     pass

# def test_structure_microhabitat():
#     mc = data_structure.structure_micro_habitat(data_frame)
#     assert list(mc.columns) == ["micro_habitat_name"]

# def test_structure_activity():
#     act = data_structure.structure_activity(data_frame)
#     assert list(act.columns) == ["activity_kind"]

# def test_structure_nesting_site():
#     ns = data_structure.structure_nesting_site(data_frame)
#     assert list(ns.columns) == ["nesting_site_desc"]

# def test_structure_species():
#     assert list(sp.columns) == [
#         "species_name_latin",
#         "size_max_male",
#         "size_max_female",
#         "size_max_record",
#         "longevity",
#         "clutch_min",
#         "clutch_max",
#         "clutch_avg",
#         "egg_diameter",
#         "range_size",
#         "elevation_min",
#         "elevation_max",
#         "elevation_avg",
#         "img_uri_female",
#         "img_uri_male",
#         "verif_status",
#         "parity_mode_id",
#         "pop_trend_id",
#         "iucn_id",
#         "genus_id"
#     ]

# def test_structure_micro_habitat_species():
#     mhs = data_structure.structure_micro_habitat_species(data_frame, sp, mc)
#     assert list(mhs.columns) == ["species_id", "micro_habitat_id"]

# def test_structure_nesting_site_species():
#     nss = data_structure.structure_nesting_site_species(data_frame, sp, ns)
#     assert list(nss.columns) == ["species_id", "nesting_site_id"]

# def test_structure_activity_species():
#     acts = data_structure.structure_activity_species(data_frame, sp, act)
#     assert list(acts.columns) == ["species_id", "activity_id"]
