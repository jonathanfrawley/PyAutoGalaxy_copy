from test_autogalaxy.integration.tests.interferometer.galaxy_x1 import (
    galaxy_x2__sersics__hyper,
)
from test_autogalaxy.integration.tests.interferometer.runner import run_a_mock


class TestCase:
    def _test__galaxy_x2__sersics__hyper(self):
        run_a_mock(galaxy_x2__sersics__hyper)
