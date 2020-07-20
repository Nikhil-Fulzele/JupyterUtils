import sys

from IPython.core.magic import line_cell_magic, magics_class, Magics
from io import StringIO

from load_dependencies_magic.load_ipynb_local import NotebookFinder

from load_dependencies_magic.load_dependencies_magic import parse_cell


@magics_class
class LoadDependencies(Magics):

    @line_cell_magic
    def load_dependencies(self, line=None, cell=None):

        if not line:
            load_nbloader = True

        else:
            sio = StringIO(cell)
            load_nbloader = parse_cell(sio)

        if load_nbloader:
            sys.meta_path.append(NotebookFinder())


def load_ipython_extension(ipython):
    """
    Any module file that define a function named `load_ipython_extension`
    can be loaded via `%load_ext module.path` or be configured to be
    autoloaded by IPython at startup time.
    """
    ipython.register_magics(LoadDependencies)
