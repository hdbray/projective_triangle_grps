# Projective triangle groups

### Overview

These python scripts will generate the tiling of a convex set in real
projective space by a triangle group acting on a projective triangle. The
inputs are the three generating projective reflections for the group.
Moduli spaces for representations of these groups are explicitly calculated
in Section 2 of the paper of Xin Nie 'on the Hilbert geometry of simplicial
Tits sets' [2014], using the work of Tits and Vinberg on representations of
linear reflection groups. Code for three examples is included. 

### Usage

In ``example_tri_grps.py`` there are examples of how the code is used. The
example groups are set at the beginning, then the fundamental domain,
affine charts and projections are chosen. The script calls functions from
other scripts to create the tilings. 

The script ``generatematrices.py`` contains functions which, given a list of
generating matrices and a length n, will generate all matrices which can be
written as a product of exactly n generators (allowing a generator to be
chosen multiple times) and removes duplicates. 

In addition to a function which writes to a list, there is a function to
write the group elements to a csv file, and functions which write n many
csv files (for k from 1 to n, generates the csv for matrices which can
be written as a product of exactly k generators). 

The script ``triangle_grps.py`` contains functions which read csv files or take
in lists and draw tilings. These functions depend on the choice of
fundamental domain, affine chart, and projection. 

### Python set-up

This software uses Python 3.7. The packages are listed in the text file
``matrixgroups_packages.txt`` and can be installed with

```
pip install matrixgroups_packages.txt
```

Alternatively,  conda environment is saved as `` matrixgroups.yml `` and
includes:

* Python   3.7
* Numpy   1.18.1
* Sympy   1.5.1 (no longer needed)
* Matplotlib   3.1.3

You can use conda to install the developing environment (download at
https://www.anaconda.com/distribution/ and make sure to set the path to
use the command conda).

Then, enter the following to create a new environment from the matrixgroups
yaml:

```
conda env create -f matrixgroups.yml
```

To activate the environment in the terminal:

```
Windows:   activate matrixgroups
Linux, macOS:  source activate matrixgroups
```

Finally, run python in the terminal window with the matrixgroups environment
activated



