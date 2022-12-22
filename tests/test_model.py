import pytest
from .model_fixtures import (
    test_data_dir,
    mappings_data,
    cross_references_data,
)
from jsonviate import JsonToWeaviate

def test_mappings(mappings_data):
    print(type(mappings_data))
    assert isinstance(mappings_data, list)

# TODO _build_objects
# TODO _build_references
# TODO get_parent_alignment

# TODO 1) load mappings & references 2) test that from_uuid/to_uuid are correct