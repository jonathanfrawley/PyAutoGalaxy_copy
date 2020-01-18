from autoarray.plot import plotters
from autoastro.plot import lensing_plotters, profile_plots


@plotters.set_labels
def profile_image(
    galaxy,
    grid,
    mask=None,
    positions=None,
    include=lensing_plotters.Include(),
    plotter=lensing_plotters.Plotter(),
):
    """Plot the image (e.g. the datas) of a galaxy, on a grid of (y,x) coordinates.

    Set *autoastro.datas.arrays.plotters.plotters* for a description of all innput parameters not described below.

    Parameters
    -----------
    galaxy : model.galaxy.aast.Galaxy
        The galaxy whose image are plotted.
    grid : ndarray or datas.arrays.grid_stacks.Grid
        The (y,x) coordinates of the grid, in an arrays of shape (total_coordinates, 2)
    """
    plotter.plot_array(
        array=galaxy.profile_image_from_grid(grid=grid),
        mask=mask,
        positions=positions,
        critical_curves=include.critical_curves_from_obj(obj=galaxy),
        light_profile_centres=include.light_profile_centres_from_obj(obj=galaxy),
        mass_profile_centres=include.mass_profile_centres_from_obj(obj=galaxy),
        include_origin=include.origin,
    )


@plotters.set_labels
def convergence(
    galaxy,
    grid,
    mask=None,
    positions=None,
    include=lensing_plotters.Include(),
    plotter=lensing_plotters.Plotter(),
):
    """Plot the convergence of a galaxy, on a grid of (y,x) coordinates.

    Set *autoastro.datas.arrays.plotters.plotters* for a description of all innput parameters not described below.

    Parameters
    -----------
    galaxy : model.galaxy.aast.Galaxy
        The galaxy whose convergence is plotted.
    grid : ndarray or datas.arrays.grid_stacks.Grid
        The (y,x) coordinates of the grid, in an arrays of shape (total_coordinates, 2)
    """
    plotter.plot_array(
        array=galaxy.convergence_from_grid(grid=grid),
        mask=mask,
        positions=positions,
        critical_curves=include.critical_curves_from_obj(obj=galaxy),
        light_profile_centres=include.light_profile_centres_from_obj(obj=galaxy),
        mass_profile_centres=include.mass_profile_centres_from_obj(obj=galaxy),
        include_origin=include.origin,
    )


@plotters.set_labels
def potential(
    galaxy,
    grid,
    mask=None,
    positions=None,
    include=lensing_plotters.Include(),
    plotter=lensing_plotters.Plotter(),
):
    """Plot the potential of a galaxy, on a grid of (y,x) coordinates.

     Set *autoastro.datas.arrays.plotters.plotters* for a description of all innput parameters not described below.

     Parameters
     -----------
    galaxy : model.galaxy.aast.Galaxy
         The galaxy whose potential is plotted.
    grid : ndarray or datas.arrays.grid_stacks.Grid
         The (y,x) coordinates of the grid, in an arrays of shape (total_coordinates, 2)
     """
    plotter.plot_array(
        array=galaxy.potential_from_grid(grid=grid),
        mask=mask,
        positions=positions,
        critical_curves=include.critical_curves_from_obj(obj=galaxy),
        light_profile_centres=include.light_profile_centres_from_obj(obj=galaxy),
        mass_profile_centres=include.mass_profile_centres_from_obj(obj=galaxy),
        include_origin=include.origin,
    )


@plotters.set_labels
def deflections_y(
    galaxy,
    grid,
    mask=None,
    positions=None,
    include=lensing_plotters.Include(),
    plotter=lensing_plotters.Plotter(),
):
    """Plot the y component of the deflection angles of a galaxy, on a grid of (y,x) coordinates.

    Set *autoastro.datas.arrays.plotters.plotters* for a description of all innput parameters not described below.

    Parameters
    -----------
    galaxy : model.galaxy.aast.Galaxy
        The galaxy whose y deflecton angles are plotted.
    grid : ndarray or datas.arrays.grid_stacks.Grid
        The (y,x) coordinates of the grid, in an arrays of shape (total_coordinates, 2)
    """
    deflections = galaxy.deflections_from_grid(grid=grid)
    deflections_y = grid.mapping.array_stored_1d_from_sub_array_1d(
        sub_array_1d=deflections[:, 0]
    )

    plotter.plot_array(
        array=deflections_y,
        mask=mask,
        positions=positions,
        critical_curves=include.critical_curves_from_obj(obj=galaxy),
        light_profile_centres=include.light_profile_centres_from_obj(obj=galaxy),
        mass_profile_centres=include.mass_profile_centres_from_obj(obj=galaxy),
        include_origin=include.origin,
    )


@plotters.set_labels
def deflections_x(
    galaxy,
    grid,
    mask=None,
    positions=None,
    include=lensing_plotters.Include(),
    plotter=lensing_plotters.Plotter(),
):
    """Plot the x component of the deflection angles of a galaxy, on a grid of (y,x) coordinates.

     Set *autoastro.datas.arrays.plotters.plotters* for a description of all innput parameters not described below.

     Parameters
     -----------
    galaxy : model.galaxy.aast.Galaxy
         The galaxy whose x deflecton angles are plotted.
     grid : ndarray or datas.arrays.grid_stacks.Grid
         The (y,x) coordinates of the grid, in an arrays of shape (total_coordinates, 2)
     """
    deflections = galaxy.deflections_from_grid(grid=grid)
    deflections_x = grid.mapping.array_stored_1d_from_sub_array_1d(
        sub_array_1d=deflections[:, 1]
    )
    plotter.plot_array(
        array=deflections_x,
        mask=mask,
        positions=positions,
        critical_curves=include.critical_curves_from_obj(obj=galaxy),
        light_profile_centres=include.light_profile_centres_from_obj(obj=galaxy),
        mass_profile_centres=include.mass_profile_centres_from_obj(obj=galaxy),
        include_origin=include.origin,
    )


@plotters.set_labels
def magnification(
    galaxy,
    grid,
    mask=None,
    positions=None,
    include=lensing_plotters.Include(),
    plotter=lensing_plotters.Plotter(),
):
    """Plot the magnification of a galaxy, on a grid of (y,x) coordinates.

     Set *autoastro.datas.arrays.plotters.plotters* for a description of all innput parameters not described below.

     Parameters
     -----------
    galaxy : model.galaxy.aast.Galaxy
         The galaxy whose magnification is plotted.
    grid : ndarray or datas.arrays.grid_stacks.Grid
         The (y,x) coordinates of the grid, in an arrays of shape (total_coordinates, 2)
     """

    plotter.plot_array(
        array=galaxy.magnification_from_grid(grid=grid),
        mask=mask,
        positions=positions,
        critical_curves=include.critical_curves_from_obj(obj=galaxy),
        light_profile_centres=include.light_profile_centres_from_obj(obj=galaxy),
        mass_profile_centres=include.mass_profile_centres_from_obj(obj=galaxy),
        include_origin=include.origin,
    )


@plotters.set_labels
def profile_image_subplot(
    galaxy,
    grid,
    mask=None,
    positions=None,
    include=lensing_plotters.Include(),
    sub_plotter=lensing_plotters.SubPlotter(),
):

    number_subplots = len(galaxy.light_profiles)

    sub_plotter.open_subplot_figure(number_subplots=number_subplots)

    for i, light_profile in enumerate(galaxy.light_profiles):

        sub_plotter.setup_subplot(number_subplots=number_subplots, subplot_index=i + 1)

        profile_plots.image(
            light_profile=light_profile,
            grid=grid,
            mask=mask,
            positions=positions,
            include=include,
            plotter=sub_plotter,
        )

    sub_plotter.output.subplot_to_figure()
    sub_plotter.figure.close()


@plotters.set_labels
def convergence_subplot(
    galaxy,
    grid,
    mask=None,
    positions=None,
    include=lensing_plotters.Include(),
    sub_plotter=lensing_plotters.SubPlotter(),
):

    number_subplots = len(galaxy.mass_profiles)

    sub_plotter.open_subplot_figure(number_subplots=number_subplots)

    for i, mass_profile in enumerate(galaxy.mass_profiles):

        sub_plotter.setup_subplot(number_subplots=number_subplots, subplot_index=i + 1)

        profile_plots.convergence(
            mass_profile=mass_profile,
            grid=grid,
            mask=mask,
            positions=positions,
            include=include,
            plotter=sub_plotter,
        )

    sub_plotter.output.subplot_to_figure()
    sub_plotter.figure.close()


@plotters.set_labels
def potential_subplot(
    galaxy,
    grid,
    mask=None,
    positions=None,
    include=lensing_plotters.Include(),
    sub_plotter=lensing_plotters.SubPlotter(),
):

    number_subplots = len(galaxy.mass_profiles)

    sub_plotter.open_subplot_figure(number_subplots=number_subplots)

    for i, mass_profile in enumerate(galaxy.mass_profiles):

        sub_plotter.setup_subplot(number_subplots=number_subplots, subplot_index=i + 1)

        profile_plots.potential(
            mass_profile=mass_profile,
            grid=grid,
            mask=mask,
            positions=positions,
            include=include,
            plotter=sub_plotter,
        )

    sub_plotter.output.subplot_to_figure()
    sub_plotter.figure.close()


@plotters.set_labels
def deflections_y_subplot(
    galaxy,
    grid,
    mask=None,
    positions=None,
    include=lensing_plotters.Include(),
    sub_plotter=lensing_plotters.SubPlotter(),
):

    number_subplots = len(galaxy.mass_profiles)

    sub_plotter.open_subplot_figure(number_subplots=number_subplots)

    for i, mass_profile in enumerate(galaxy.mass_profiles):

        sub_plotter.setup_subplot(number_subplots=number_subplots, subplot_index=i + 1)

        profile_plots.deflections_y(
            mass_profile=mass_profile,
            grid=grid,
            mask=mask,
            positions=positions,
            include=include,
            plotter=sub_plotter,
        )

    sub_plotter.output.subplot_to_figure()
    sub_plotter.figure.close()


@plotters.set_labels
def deflections_x_subplot(
    galaxy,
    grid,
    mask=None,
    positions=None,
    include=lensing_plotters.Include(),
    sub_plotter=lensing_plotters.SubPlotter(),
):

    number_subplots = len(galaxy.mass_profiles)

    sub_plotter.open_subplot_figure(number_subplots=number_subplots)

    for i, mass_profile in enumerate(galaxy.mass_profiles):

        sub_plotter.setup_subplot(number_subplots=number_subplots, subplot_index=i + 1)

        profile_plots.deflections_x(
            mass_profile=mass_profile,
            grid=grid,
            mask=mask,
            positions=positions,
            include=include,
            plotter=sub_plotter,
        )

    sub_plotter.output.subplot_to_figure()
    sub_plotter.figure.close()


@plotters.set_labels
def contribution_map(
    galaxy,
    mask=None,
    positions=None,
    include=lensing_plotters.Include(),
    plotter=lensing_plotters.Plotter(),
):
    """Plot the summed contribution maps of a hyper_galaxies-fit.

    Set *autolens.datas.arrays.plotters.plotters* for a description of all input parameters not described below.

    Parameters
    -----------
    fit : datas.fitting.fitting.AbstractLensHyperFit
        The hyper_galaxies-fit to the datas, which includes a list of every model image, residual_map, chi-squareds, etc.
    image_index : int
        The index of the datas in the datas-set of which the contribution_maps are plotted.
    """

    plotter.plot_array(
        array=galaxy.contribution_map,
        mask=mask,
        positions=positions,
        critical_curves=include.critical_curves_from_obj(obj=galaxy),
        light_profile_centres=include.light_profile_centres_from_obj(obj=galaxy),
        mass_profile_centres=include.mass_profile_centres_from_obj(obj=galaxy),
        include_origin=include.origin,
    )
