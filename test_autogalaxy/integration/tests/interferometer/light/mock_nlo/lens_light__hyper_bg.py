from test_autogalaxy.integration.tests.interferometer.galaxy_x1 import (
    galaxy_light__hyper_bg,
)
from test_autogalaxy.integration.tests.interferometer.runner import run_a_mock


class TestCase:
    def _test__galaxy_light__hyper_bg(self):
        run_a_mock(galaxy_light__hyper_bg)