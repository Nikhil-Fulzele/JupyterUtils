Notebook Magic to import one .ipynb from another .ipynb. Special case is handled when the notebook to be imported is location on some remote path.

Usage:

## Setup and installation
A. Install Python 3.7+

B. Install the package from load_deps_magic branch - 
```bash
pip install git+https://github.com/Nikhil-Fulzele/JupyterUtils.git@load_deps_magic#subdirectory=load_dependencies_magic
```

C. Open jupyter notebook and load the extension
```markdown
%load_ext load_dependencies_magic
```

## Usage
A. import all the .ipynb files given they are in the same folder as working notebook
```markdown
%load_dependencies
```

B. import a notebook from remote path - should be served by the same notebook server
```markdown
%%load_dependencies
<Complete url path for remote notebook to be imported> --alias <save as>
```

That's it. Now simply test it by importing. :-)
