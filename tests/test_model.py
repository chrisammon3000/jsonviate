import pytest
from .model_fixtures import (
    test_data_dir,
    raw_data,
    classes_map,
    cross_references_map,
    expected_classes_data,
    expected_references_data,
)
from jsonviate import JsonToWeaviate


def test_raw_data(raw_data):
    print(type(raw_data))
    assert isinstance(raw_data, list)


def test_classes_map(classes_map):
    print(type(classes_map))
    assert isinstance(classes_map, list)


def test_cross_references(cross_references_map):
    print(type(cross_references_map))
    assert isinstance(cross_references_map, list)


def test_expected_classes_data(expected_classes_data):
    print(type(expected_classes_data))
    assert isinstance(expected_classes_data, list)


def test_expected_references_data(expected_references_data):
    print(type(expected_references_data))
    assert isinstance(expected_references_data, list)


# TODO _build_objects
# TODO _build_references
# TODO get_parent_alignment

# TODO 1) load mappings & references 2) test that from_uuid/to_uuid are correct
def test_jsonmapper_cross_references(raw_data, classes_map, cross_references_map):
    # factory = JsonToWeaviate(classes_map, cross_references_map)
    # # print(classes_map)
    # builder = JsonToWeaviate.from_json(factory, raw_data[0])

    # classes = set([ item["class"] for item in classes_map ])

    # assert builder.Dataset.data_objects[0]["class"] in classes

    assert True
