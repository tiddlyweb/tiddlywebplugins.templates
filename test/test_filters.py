"""
Test the filters added to the jinja loader.
"""

from tiddlyweb.fixups import unquote
from tiddlywebplugins.templates import uri, format_modified, rfc3339


def test_uri():
    encoded_name = 'aaa%25%E3%81%86%E3%81%8F%E3%81%99'
    name = unquote(encoded_name)

    assert uri(name) == encoded_name


def test_format_modified():
    timestring = '201307111654'
    output = format_modified(timestring)

    assert output == 'Thu, 11 Jul 2013 16:54:00 GMT'


def test_rfc3339():
    timestring = '20130711165401'
    output = rfc3339(timestring)

    assert output == '2013-07-11T16:54:01Z'

