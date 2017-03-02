from functools import partial

import click

from criteo_downloader import config, downloader
from criteo_downloader.config import CriteoAccount


def config_option(config_function, **kwargs):
    """Helper decorator that turns an option function into a cli option"""

    def decorator(function):
        default = kwargs.pop('default', None)
        if default is None:
            default = config_function()
        if kwargs.get('multiple'):
            default = [default]
        return click.option('--' + config_function.__name__, default=default,
                            help=config_function.__doc__ + '. Default: "' + str(default) + '"',
                            **kwargs)(function)

    return decorator


def apply_options(**kwargs):
    """Applies passed cli parameters to config.py"""
    for key, value in kwargs.items():
        if key == 'accounts':
            setattr(config, key, partial(lambda v: [CriteoAccount(*args) for args in v], value))
        else:
            setattr(config, key, partial(lambda v: v, value))


@click.command()
@config_option(config.accounts, type=(str, str, str, str), multiple=True,
               default=('accountname', 'username', 'password', 'token'))
@config_option(config.data_dir)
@config_option(config.first_date)
def download_data(**kwargs):
    """
    Downloads data.
    When options are not specified, then the defaults from config.py are used.
    """
    apply_options(**kwargs)
    downloader.download_data()
