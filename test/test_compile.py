


def test_compile():
    try:
        import tiddlywebplugins.templates
        assert True
    except ImportError as exc:
        assert False, exc
