from src.game import won, CROSS, ZERO


def test_won_rows():
    fields = [[CROSS, CROSS, CROSS], [ZERO, ZERO, ZERO], [ZERO, ZERO, ZERO]]
    result = won(fields, CROSS)
    assert result == True


def test_won_columns():
    fields = [[CROSS, ZERO, ZERO], [CROSS, ZERO, ZERO], [CROSS, ZERO, ZERO]]
    result = won(fields, CROSS)
    assert result == True


def test_won_diagonals():
    fields = [[CROSS, ZERO, ZERO], [ZERO, CROSS, ZERO], [ZERO, ZERO, CROSS]]
    result = won(fields, CROSS)
    assert result == True


def test_not_won():
    fields = [[CROSS, ZERO, ZERO], [ZERO, CROSS, ZERO], [ZERO, ZERO, CROSS]]
    result = won(fields, ZERO)
    assert result == False
