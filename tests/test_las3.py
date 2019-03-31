import os, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import fnmatch

import numpy as np
import pytest

import lasio
from lasio import read, las

import logging

logger = logging.getLogger(__name__)

test_dir = os.path.dirname(__file__)

egfn = lambda fn: os.path.join(os.path.dirname(__file__), "examples", fn)
stegfn = lambda vers, fn: os.path.join(os.path.dirname(__file__), "examples", vers, fn)


def test_read_section_titles():
    l = lasio.read(egfn("standard_v3.las"))
    assert set(l.sections.keys()) == set(
        [
            "Version",
            "Well",
            "Curves",
            "Parameter",
            "Other",
            "Drilling_Definition",
            "Drilling",
            "Core_Definition",
            "Core[1]",
            "Core[2]",
            "Inclinometry_Definition",
            "Inclinometry",
            "Test_Definition",
            "TEST",
            "TOPS_Definition",
            "TOPS",
            "Perforations_Definition",
            "Perforations",
        ]
    )
