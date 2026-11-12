from repopulse.render import BLOCKS, sparkline

def test_sparkline_all_zero_is_flat():
    assert sparkline([0, 0, 0]) == BLOCKS[0] * 3

def test_sparkline_peak_gets_full_block():
    result = sparkline([0, 5, 10])
    assert len(result) == 3
    assert result[0] == BLOCKS[0]
    assert result[-1] == BLOCKS[-1]
