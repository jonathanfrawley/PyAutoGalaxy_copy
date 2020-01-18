from autoarray.plot import plotters
from autoastro.plot import lensing_plotters
from autoarray.util import plotter_util


@plotters.set_labels
def profile_image(
    light_profile,
    grid,
    mask=None,
    positions=None,
    include=lensing_plotters.Include(),
    plotter=lensing_plotters.Plotter(),
):
    """Plot the image of a light profile, on a grid of (y,x) coordinates.

    Set *autoastro.hyper_galaxies.arrays.plotters.plotters* for a description of all innput parameters not described below.

    Parameters
    -----------
    light_profile : model.profiles.light_profiles.LightProfile
        The light profile whose image are plotted.
    grid : ndarray or hyper_galaxies.arrays.grid_stacks.Grid
        The (y,x) coordinates of the grid, in an arrays of shape (total_coordinates, 2)
    """
    plotter.plot_array(
        array=light_profile.profile_image_from_grid(grid=grid),
        mask=mask,
        positions=positions,
        light_profile_centres=include.light_profile_centres_from_obj(obj=light_profile),
        include_origin=include.origin,
    )


def luminosity_within_circle_in_electrons_per_second_as_function_of_radius(
    light_profile,
    minimum_radius=1.0e-4,
    maximum_radius=10.0,
    radii_bins=10,
    plot_axis_type="semilogy",
    plotter=lensing_plotters.Plotter(),
):

    radii = plotter_util.quantity_radii_from_minimum_and_maximum_radii_and_radii_points(
        minimum_radius=minimum_radius,
        maximum_radius=maximum_radius,
        radii_points=radii_bins,
    )

    luminosities = list(
        map(
            lambda radius: light_profile.luminosity_within_circle_in_units(
                radius=radius
            ),
            radii,
        )
    )

    plotter.plot_array(
        quantity=luminosities, radii=radii, plot_axis_type=plot_axis_type
    )