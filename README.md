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

### Install

The developing environment is saved as `` matrixgroups.yml `` and includes:

* Python   3.7
* Numpy   1.18.1
* Sympy   1.5.1 (no longer needed)
* Matplotlib   3.1.3

You can use conda to install the developing environment (download at
https://www.anaconda.com/distribution/).

You will need to set the path to use the command conda in terminal.

Then, download the ``matrixgroups.yml`` file to access the developing environment. In terminal, enter the following to create a new environment from this file:

```
conda env create -f matrixgroups.yml
```

Then activate the environment in the terminal:

```
Windows:   activate matrixgroups
Linux, macOS:  source activate matrixgroups
```

and run python in the terminal window with the matrixgroups environment
activated



