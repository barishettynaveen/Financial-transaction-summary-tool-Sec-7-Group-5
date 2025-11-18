
def test_total_income():
    df = pd.DataFrame({'Amount': [1000, -200, 500]})
    assert total_income(df) == 1500
