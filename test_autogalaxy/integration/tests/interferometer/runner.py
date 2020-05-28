import os
import numpy as np
from autoconf import conf
import autofit as af
import autogalaxy as ag
from autofit.optimize.non_linear.mock_nlo import MockNLO
from test_autogalaxy.simulators.interferometer import instrument_util


def run(module, test_name=None, non_linear_class=af.MultiNest, config_folder="config"):
    test_name = test_name or module.test_name
    test_path = "{}/../../".format(os.path.dirname(os.path.realpath(__file__)))
    output_path = f"{test_path}/output/interferometer/"
    config_path = test_path + config_folder
    conf.instance = conf.Config(config_path=config_path, output_path=output_path)

    interferometer = instrument_util.load_test_interferometer(
        data_label=module.data_label, instrument=module.instrument
    )

    pixel_scales = instrument_util.pixel_scale_from_instrument(
        instrument=module.instrument
    )
    grid = instrument_util.grid_from_instrument(instrument=module.instrument)

    real_space_mask = ag.Mask.circular(
        shape_2d=grid.shape_2d, pixel_scales=pixel_scales, radius=2.0
    )

    visibilities_mask = np.full(
        fill_value=False, shape=interferometer.visibilities.shape
    )

    module.make_pipeline(
        name=test_name,
        phase_folders=[module.test_type, test_name],
        non_linear_class=non_linear_class,
        real_space_mask=real_space_mask,
    ).run(dataset=interferometer, mask=visibilities_mask)


def run_a_mock(module):
    # noinspection PyTypeChecker
    run(
        module,
        test_name=f"{module.test_name}_mock",
        non_linear_class=MockNLO,
        config_folder="config_mock",
    )


def run_with_multi_nest(module):
    # noinspection PyTypeChecker
    run(
        module,
        test_name=f"{module.test_name}_nest",
        non_linear_class=af.MultiNest,
        config_folder="config_mock",
    )