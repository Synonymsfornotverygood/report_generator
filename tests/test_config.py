import report_generator.config as c


def test_load_config():
    cf = c.load_config()
    assert "author_name" in cf.keys()


def test_dump_config():
    cf = c.load_config()
    cf["Test"] = "Test"
    c.dump_config(cf)

    cf2 = c.load_config()
    assert "Test" in cf2.keys()
    assert "Test" == cf2["Test"]

    cf2.pop("Test")
    c.dump_config(cf2)
