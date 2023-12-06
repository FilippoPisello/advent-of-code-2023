from advent_of_code.day3.sacha.solution import main, mapping_symbol, Symbol

def test_mapping():
    data='...*...........197.261'
    return mapping_symbol(data) == Symbol(symbol='*', x=3, y=0)
