from scraper import get_citations_needed_count

def test_get_citations_needed_count():

    actual=get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico')

    expect=12

    assert actual == expect