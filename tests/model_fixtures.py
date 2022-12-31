import json

import pytest


@pytest.fixture
def test_data_dir(request):
    return "tests/data"


@pytest.fixture
def classes_map(request, test_data_dir):
    file_path = f"{test_data_dir}/mappings/mappings-spec.json"
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


@pytest.fixture
def cross_references_map(request, test_data_dir):
    file_path = f"{test_data_dir}/mappings/references-spec.json"
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


@pytest.fixture
def expected_classes_data(request, test_data_dir):
    file_path = f"{test_data_dir}/expected/data-objects.json"
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


@pytest.fixture
def expected_references_data(request, test_data_dir):
    file_path = f"{test_data_dir}/expected/cross-references.json"
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


@pytest.fixture
def raw_data(request, test_data_dir):
    file_path = f"{test_data_dir}/raw/aws-odr.json"
    with open(file_path, "r") as f:
        data = json.load(f)
    return data
