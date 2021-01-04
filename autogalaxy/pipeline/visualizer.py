import copy
from os import path

from autoconf import conf
import autofit as af
from autoarray.plot.mat_wrap.wrap import wrap_base
from autoarray.plot.plotters import (
    imaging_plotters,
    interferometer_plotters,
    inversion_plotters,
)
from autogalaxy.plot.plotters import (
    fit_imaging_plotters,
    fit_interferometer_plotters,
    fit_galaxy_plotters,
    hyper_plotters,
)
from autogalaxy.plot.mat_wrap import lensing_mat_plot, lensing_include


def setting(section, name):
    return conf.instance["visualize"]["plots"][section][name]


def plot_setting(section, name):
    return setting(section, name)


class Visualizer:
    def __init__(self, plot_path):

        self.image_path = plot_path

        self.plot_fit_no_hyper = plot_setting("hyper", "fit_no_hyper")

        self.include_2d = lensing_include.Include2D()

    def mat_plot_1d_from(self, subfolders, format="png"):
        return lensing_mat_plot.MatPlot1D(
            output=wrap_base.Output(
                path=path.join(self.image_path, subfolders), format=format
            )
        )

    def mat_plot_2d_from(self, subfolders, format="png"):
        return lensing_mat_plot.MatPlot2D(
            output=wrap_base.Output(
                path=path.join(self.image_path, subfolders), format=format
            )
        )

    def visualize_imaging(self, imaging):
        def should_plot(name):
            return plot_setting(section="dataset", name=name)

        mat_plot_2d = self.mat_plot_2d_from(subfolders="imaging")

        imaging_plotter = imaging_plotters.ImagingPlotter(
            imaging=imaging, mat_plot_2d=mat_plot_2d, include_2d=self.include_2d
        )

        imaging_plotter.figure_individuals(
            plot_image=should_plot("data"),
            plot_noise_map=should_plot("noise_map"),
            plot_psf=should_plot("psf"),
            plot_inverse_noise_map=should_plot("inverse_noise_map"),
            plot_signal_to_noise_map=should_plot("signal_to_noise_map"),
            plot_absolute_signal_to_noise_map=should_plot(
                "absolute_signal_to_noise_map"
            ),
            plot_potential_chi_squared_map=should_plot("potential_chi_squared_map"),
        )

        if should_plot("subplot_dataset"):

            imaging_plotter.subplot_imaging()

    def visualize_fit_imaging(self, fit, during_analysis, subfolders="fit_imaging"):
        def should_plot(name):
            return plot_setting(section="fit", name=name)

        mat_plot_2d = self.mat_plot_2d_from(subfolders=subfolders)

        fit_imaging_plotter = fit_imaging_plotters.FitImagingPlotter(
            fit=fit, mat_plot_2d=mat_plot_2d, include_2d=self.include_2d
        )

        fit_imaging_plotter.figure_individuals(
            plot_image=should_plot("data"),
            plot_noise_map=should_plot("noise_map"),
            plot_signal_to_noise_map=should_plot("signal_to_noise_map"),
            plot_model_image=should_plot("model_data"),
            plot_residual_map=should_plot("residual_map"),
            plot_chi_squared_map=should_plot("chi_squared_map"),
            plot_normalized_residual_map=should_plot("normalized_residual_map"),
            plot_subtracted_images_of_galaxies=should_plot(
                "subtracted_images_of_galaxies"
            ),
            plot_model_images_of_galaxies=should_plot("model_images_of_galaxies"),
        )

        if should_plot("subplot_fit"):
            fit_imaging_plotter.subplot_fit_imaging()

        if should_plot("subplots_of_galaxies_fits"):
            fit_imaging_plotter.subplots_of_all_galaxies()

        if not during_analysis:

            if should_plot("all_at_end_png"):

                fit_imaging_plotter.figure_individuals(
                    plot_image=True,
                    plot_noise_map=True,
                    plot_signal_to_noise_map=True,
                    plot_model_image=True,
                    plot_residual_map=True,
                    plot_normalized_residual_map=True,
                    plot_chi_squared_map=True,
                    plot_subtracted_images_of_galaxies=True,
                    plot_model_images_of_galaxies=True,
                )

            if should_plot("all_at_end_fits"):

                mat_plot_2d = self.mat_plot_2d_from(
                    subfolders="fit_imaging/fits", format="fits"
                )

                fit_imaging_plotter = fit_imaging_plotters.FitImagingPlotter(
                    fit=fit, mat_plot_2d=mat_plot_2d, include_2d=self.include_2d
                )

                fit_imaging_plotter.figure_individuals(
                    plot_image=True,
                    plot_noise_map=True,
                    plot_signal_to_noise_map=True,
                    plot_model_image=True,
                    plot_residual_map=True,
                    plot_normalized_residual_map=True,
                    plot_chi_squared_map=True,
                    plot_subtracted_images_of_galaxies=True,
                    plot_model_images_of_galaxies=True,
                )

    def visualize_interferometer(self, interferometer):
        def should_plot(name):
            return plot_setting(section="dataset", name=name)

        mat_plot_2d = self.mat_plot_2d_from(subfolders="interferometer")

        interferometer_plotter = interferometer_plotters.InterferometerPlotter(
            interferometer=interferometer,
            include_2d=self.include_2d,
            mat_plot_2d=mat_plot_2d,
        )

        if should_plot("subplot_dataset"):
            interferometer_plotter.subplot_interferometer()

        interferometer_plotter.figure_individuals(
            plot_visibilities=should_plot("data"),
            plot_u_wavelengths=should_plot("uv_wavelengths"),
            plot_v_wavelengths=should_plot("uv_wavelengths"),
        )

    def visualize_fit_interferometer(
        self, fit, during_analysis, subfolders="fit_interferometer"
    ):
        def should_plot(name):
            return plot_setting(section="fit", name=name)

        mat_plot_1d = self.mat_plot_1d_from(subfolders=subfolders)
        mat_plot_2d = self.mat_plot_2d_from(subfolders=subfolders)

        fit_interferometer_plotter = fit_interferometer_plotters.FitInterferometerPlotter(
            fit=fit,
            include_2d=self.include_2d,
            mat_plot_1d=mat_plot_1d,
            mat_plot_2d=mat_plot_2d,
        )

        if should_plot("subplot_fit"):
            fit_interferometer_plotter.subplot_fit_interferometer()
            fit_interferometer_plotter.subplot_fit_real_space()

        fit_interferometer_plotter.figure_individuals(
            plot_visibilities=should_plot("data"),
            plot_noise_map=should_plot("noise_map"),
            plot_signal_to_noise_map=should_plot("signal_to_noise_map"),
            plot_model_visibilities=should_plot("model_data"),
            plot_residual_map=should_plot("residual_map"),
            plot_chi_squared_map=should_plot("chi_squared_map"),
            plot_normalized_residual_map=should_plot("normalized_residual_map"),
        )

        if not during_analysis:

            if should_plot("all_at_end_png"):

                fit_interferometer_plotter.figure_individuals(
                    plot_visibilities=True,
                    plot_noise_map=True,
                    plot_signal_to_noise_map=True,
                    plot_model_visibilities=True,
                    plot_residual_map=True,
                    plot_normalized_residual_map=True,
                    plot_chi_squared_map=True,
                )

            if should_plot("all_at_end_fits"):

                mat_plot_2d = self.mat_plot_2d_from(
                    subfolders="fit_interferometer/fits", format="fits"
                )

                fit_interferometer_plotter = fit_interferometer_plotters.FitInterferometerPlotter(
                    fit=fit, include_2d=self.include_2d, mat_plot_2d=mat_plot_2d
                )

                fit_interferometer_plotter.figure_individuals(
                    plot_visibilities=True,
                    plot_noise_map=True,
                    plot_signal_to_noise_map=True,
                    plot_model_visibilities=True,
                    plot_residual_map=True,
                    plot_normalized_residual_map=True,
                    plot_chi_squared_map=True,
                )

    def visualize_inversion(self, inversion, during_analysis):
        def should_plot(name):
            return plot_setting(section="inversion", name=name)

        mat_plot_2d = self.mat_plot_2d_from(subfolders="inversion")

        inversion_plotter = inversion_plotters.InversionPlotter(
            inversion=inversion, mat_plot_2d=mat_plot_2d, include_2d=self.include_2d
        )

        if should_plot("subplot_inversion"):
            inversion_plotter.subplot_inversion()

        inversion_plotter.figure_individuals(
            plot_reconstructed_image=should_plot("reconstruction"),
            plot_reconstruction=should_plot("reconstruction"),
            plot_errors=should_plot("errors"),
            plot_residual_map=should_plot("residual_map"),
            plot_normalized_residual_map=should_plot("normalized_residual_map"),
            plot_chi_squared_map=should_plot("chi_squared_map"),
            plot_regularization_weights=should_plot("regularization_weights"),
            plot_interpolated_reconstruction=should_plot("interpolated_reconstruction"),
            plot_interpolated_errors=should_plot("interpolated_errors"),
        )

        if not during_analysis:

            inversion_plotter.figure_individuals(
                plot_reconstructed_image=True,
                plot_reconstruction=True,
                plot_errors=True,
                plot_residual_map=True,
                plot_normalized_residual_map=True,
                plot_chi_squared_map=True,
                plot_regularization_weights=True,
                plot_interpolated_reconstruction=True,
                plot_interpolated_errors=True,
            )

    def visualize_hyper_images(
        self,
        hyper_galaxy_image_path_dict,
        hyper_model_image,
        contribution_maps_of_galaxies,
    ):
        def should_plot(name):
            return plot_setting(section="hyper", name=name)

        mat_plot_2d = self.mat_plot_2d_from(subfolders="hyper")

        hyper_plotter = hyper_plotters.HyperPlotter(
            mat_plot_2d=mat_plot_2d, include_2d=self.include_2d
        )

        if should_plot("model_image"):
            hyper_plotter.figure_hyper_model_image(hyper_model_image=hyper_model_image)

        if should_plot("images_of_galaxies"):

            hyper_plotter.subplot_hyper_images_of_galaxies(
                hyper_galaxy_image_path_dict=hyper_galaxy_image_path_dict
            )

        if should_plot("contribution_maps_of_galaxies"):
            hyper_plotter.subplot_contribution_maps_of_galaxies(
                contribution_maps_of_galaxies=contribution_maps_of_galaxies
            )

    def visualize_galaxy_fit(self, fit, visuals_2d=None):
        def should_plot(name):
            return plot_setting(section="galaxy_fit", name=name)

        mat_plot_2d = self.mat_plot_2d_from(subfolders="galaxy_fit")

        fit_galaxy_plotter = fit_galaxy_plotters.FitGalaxyPlotter(
            fit=fit,
            mat_plot_2d=mat_plot_2d,
            visuals_2d=visuals_2d,
            include_2d=self.include_2d,
        )

        if should_plot("subplot_galaxy_fit"):
            fit_galaxy_plotter.subplot_fit_galaxy()

        mat_plot_2d = self.mat_plot_2d_from(subfolders="galaxy_fit")

        fit_galaxy_plotter = fit_galaxy_plotters.FitGalaxyPlotter(
            fit=fit,
            mat_plot_2d=mat_plot_2d,
            visuals_2d=visuals_2d,
            include_2d=self.include_2d,
        )

        fit_galaxy_plotter.figure_individuals(
            plot_image=should_plot("image"),
            plot_noise_map=should_plot("noise_map"),
            plot_model_image=should_plot("model_image"),
            plot_residual_map=should_plot("residual_map"),
            plot_chi_squared_map=should_plot("chi_squared_map"),
        )
