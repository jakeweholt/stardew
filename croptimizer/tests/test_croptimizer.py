from croptimizer.utilities import calculate_potential_harvests

def load_test_config():
    import json
    with open('mockConfig.json') as json_file:
        data = json.load(json_file)
    return data


def test_1():
    assert 1==1


def test_firstDay_1():
    from croptimizer.croptimizer import Scheduler
    test_config = load_test_config()['firstDay']
    s = Scheduler(test_config)


def test_calculate_potential_harvests() -> None:
    """
    Unit tests for calculate_potential_harvests()
    """
    assert calculate_potential_harvests(7,6,6) == 1
    assert calculate_potential_harvests(13,6,6) == 2
    assert calculate_potential_harvests(6,6,1) == 0
    assert calculate_potential_harvests(100,1,1) == 99
