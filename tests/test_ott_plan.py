from src.ott_plan import calculate_total
import pytest
def test_sample1():
    plan={
        "Netflix":20,
        "Amazon Prime":10,
        "Hotstar":50

    }
    assert calculate_total(plan)==34
def test_sample2():
    plan={
        "Netflix":10,
        "Amazon Prime":0,
        "Hotstar":100

    }
    assert calculate_total(plan)==30
def test_sample3():
    plan={
        "Netflix":10,
        "Amazon Prime":2,      

    }
    with pytest.raises(ValueError) as exc_info:
        calculate_total(plan)
    assert str(exc_info.value)==("Amazon Prime allows viewing hours in multiples of 5 only")