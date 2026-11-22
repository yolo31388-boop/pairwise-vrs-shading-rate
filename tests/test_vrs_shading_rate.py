import pytest
import render.vrs_shading_rate as mod

CASES = [
    ("content_tiles", (16, 16)),
    ("follow_velocity", (0.5, 0.2)),
    ("motion_vectors", (2.0, 1.0)),
    ("shadow_rate", (2, 4)),
    ("transparent_keep", (1, 2)),
    ("msaa_compat", (4, 2)),
    ("incremental_update", (1, 2)),
    ("capability_check", (1, 2)),
    ("ui_exclude", (1, 2)),
    ("quality_baseline", (0.9, 0.8)),
    ("rate_texture", (1920, 1080)),
    ("tile_size", (16, 8)),
    ("edge_protect", (1, 2)),
    ("fallback_rate", (1, 2)),
    ("stats_compare", (1.0, 2.0)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
