import json
import pytest

@pytest.fixture
def test_data_dir():
    return "tests/data"

@pytest.fixture
def mappings_data(request, test_data_dir):
    file_path = f"{test_data_dir}/mappings.json"
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

@pytest.fixture
def cross_references_data(request, test_data_dir):
    file_path = f"{test_data_dir}//cross-references.json"
    with open(file_path, "r") as f:
        data = json.load(f)
    return data