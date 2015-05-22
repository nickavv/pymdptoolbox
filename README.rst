Inverse Reinforcement Learning (IRL) Augmentation for Markov Decision Process (MDP) Toolbox for Python
================================================

The `MDP toolbox for Python <https://github.com/sawcordwell/pymdptoolbox/>`_ by Sam Cordwell provides classes and functions for the resolution of
descrete-time Markov Decision Processes. The list of algorithms that have been
implemented includes backwards induction, linear programming, policy iteration,
q-learning and value iteration along with several variations.

This IRL augmentation for this toolbox will provide additional classes and functions related to infinite time horizon maximum causal entropy IRL. The list of algorithms for deriving soft Bellman policies that will be implemented includes soft value iteration, soft q-learning, and convex optimization. These algorithms are described in 'Infinite time horizon maximum causal entropy inverse reinforcement learning' by Michael Bloem and Nicholas Bambos, IEEE Conference on Decision and Control, Los Angeles, CA, 2014 doi `10.1109/CDC.2014.7040156 <http://dx.doi.org/10.1109/CDC.2014.7040156>`_

Features under development
--------------------------
  - Three algorithms for deriving soft Bellman policies
  - Three algorithms for policy evaluation
  - Gradient algorithm for tuning parameters in soft Bellman policies

PLEASE NOTE: the linear programming algorithm is currently unavailable except
for testing purposes due to incorrect behaviour.

Installation
------------
NumPy and SciPy must be on your system to use this toolbox. Please have a
look at their documentation to get them installed. If you are installing
onto Ubuntu or Debian and using Python 2 then this will pull in all the
dependencies:

  ``sudo apt-get install python-numpy python-scipy python-cvxopt``

On the other hand, if you are using Python 3 then cvxopt will have to be
compiled (pip will do it automatically). To get NumPy, SciPy and all the
dependencies to have a fully featured cvxopt then run:

  ``sudo apt-get install python3-numpy python3-scipy liblapack-dev libatlas-base-dev libgsl0-dev fftw-dev libglpk-dev libdsdp-dev``

The main way to download the package is from GitHub. 

  1. To clone the Git repository

     ``git clone https://github.com/nasa/pymdptoolbox.git``

  2. Change to the PyMDPtoolbox directory

     ``cd pymdptoolbox``

  3. Install via Setuptools, either to the root filesystem or to your home
     directory if you don't have administrative access.

     ``python setup.py install``

     ``python setup.py install --user``

     Read the `Setuptools documentation <https://pythonhosted.org/setuptools/>`_ for
     more advanced information.

To learn how to use Git then you might consider reading the freely available `Pro Git book <http://git-scm.com/book>`_ written by Scott Chacon and Ben Straub and published by Apress.

Quick Use
---------
Start Python in your favorite way. The following example shows you how to
import the module, set up an example Markov decision problem using a discount
value of 0.9, solve it using the value iteration algorithm, and then check the
optimal policy.

.. code:: python

  import mdptoolbox.example
  P, R = mdptoolbox.example.forest()
  vi = mdptoolbox.mdp.ValueIteration(P, R, 0.9)
  vi.run()
  vi.policy # result is (0, 0, 0)

Documentation
-------------
Documentation is available as docstrings in the module code.
If you use `IPython <http://ipython.scipy.org>`_ to work with the toolbox,
then you can view the docstrings by using a question mark ``?``. For example:

.. code:: python

    import mdptoolbox
    mdptoolbox?<ENTER>
    mdptoolbox.mdp?<ENTER>
    mdptoolbox.mdp.ValueIteration?<ENTER>

will display the relevant documentation.

Contribute
----------
Source Code: https://github.com/nasa/pymdptoolbox

License
-------
See `<LICENSE.txt>`_ for details.

