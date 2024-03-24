import json

import pytest


@pytest.fixture(scope="session")
def target_id_path_cases() -> list[dict]:
    return json.load(open("tests/functional/api/test_data.json"))
