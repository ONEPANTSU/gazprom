import json

import pytest


@pytest.fixture(scope="session")
def shortest_path_cases() -> list[dict]:
    return json.load(open("tests/test_data.json"))
