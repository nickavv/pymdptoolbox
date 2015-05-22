# -*- coding: utf-8 -*-
"""Markov Decision Process (MDP) Toolbox
=====================================

The MDP toolbox provides classes and functions for the resolution of
descrete-time Markov Decision Processes.

Available modules
-----------------

:mod:`~mdptoolbox.example`
    Examples of transition and reward matrices that form valid MDPs
:mod:`~mdptoolbox.mdp`
    Makov decision process algorithms
:mod:`~mdptoolbox.util`
    Functions for validating and working with an MDP

How to use the documentation
----------------------------
Documentation is available both as docstrings provided with the code and
in html or pdf format from
`The MDP toolbox homepage <http://www.somewhere.com>`_. The docstring
examples assume that the ``mdptoolbox`` package is imported like so::

  >>> import mdptoolbox

To use the built-in examples, then the ``example`` module must be imported::

  >>> import mdptoolbox.example

Once the ``example`` module has been imported, then it is no longer neccesary
to issue ``import mdptoolbox``.

Code snippets are indicated by three greater-than signs::

  >>> x = 17
  >>> x = x + 1
  >>> x
  18

The documentation can be displayed with
`IPython <http://ipython.scipy.org>`_. For example, to view the docstring of
the ValueIteration class use ``mdp.ValueIteration?<ENTER>``, and to view its
source code use ``mdp.ValueIteration??<ENTER>``.

Acknowledgments
---------------
This module is modified from the MDPtoolbox (c) 2009 INRA available at
http://www.inra.fr/mia/T/MDPtoolbox/.

"""

# Inverse Reinforcement Learning (IRL) Augmentation for PyMDPToolbox
# Copyright (c) 2015 United States Government as represented by the Administrator of the 
# National Aeronautics and Space Administration.  No copyright is claimed in the United 
# States under Title 17, U.S.Code. All Other Rights Reserved.
#  
# NASA software is a modification to the following:
# PyMDPToolbox
# Copyright (c) 2011-2015 Steven A. W. Cordwell
# Copyright (c) 2009 INRA
# All rights reserved.
#  
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#  
# 1.     Redistributions of source code must retain the above copyright notice, this list 
# of conditions and the following disclaimer.
# 2.     Redistributions in binary form must reproduce the above copyright notice, this 
# list of conditions and the following disclaimer in the documentation and/or other 
# materials provided with the distribution.
# 3.     Neither the name of the <ORGANIZATION> nor the names of its contributors may be 
# used to endorse or promote products derived from this software without specific prior 
# written permission.
#  
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF 
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL 
# THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT 
# OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) 
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR 
# TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, 
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# NASA Disclaimers
# 
# No Warranty: THE SUBJECT SOFTWARE IS PROVIDED "AS IS" WITHOUT ANY WARRANTY OF ANY KIND, 
# EITHER EXPRESSED, IMPLIED, OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, ANY WARRANTY THAT 
# THE SUBJECT SOFTWARE WILL CONFORM TO SPECIFICATIONS, ANY IMPLIED WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR FREEDOM FROM INFRINGEMENT, ANY 
# WARRANTY THAT THE SUBJECT SOFTWARE WILL BE ERROR FREE, OR ANY WARRANTY THAT DOCUMENTATION, 
# IF PROVIDED, WILL CONFORM TO THE SUBJECT SOFTWARE. THIS AGREEMENT DOES NOT, IN ANY MANNER, 
# CONSTITUTE AN ENDORSEMENT BY GOVERNMENT AGENCY OR ANY PRIOR RECIPIENT OF ANY RESULTS, 
# RESULTING DESIGNS, HARDWARE, SOFTWARE PRODUCTS OR ANY OTHER APPLICATIONS RESULTING FROM 
# USE OF THE SUBJECT SOFTWARE.  FURTHER, GOVERNMENT AGENCY DISCLAIMS ALL WARRANTIES AND 
# LIABILITIES REGARDING THIRD-PARTY SOFTWARE, IF PRESENT IN THE ORIGINAL SOFTWARE, AND 
# DISTRIBUTES IT "AS IS."
# 
# Waiver and Indemnity:  RECIPIENT AGREES TO WAIVE ANY AND ALL CLAIMS AGAINST THE UNITED 
# STATES GOVERNMENT, ITS CONTRACTORS AND SUBCONTRACTORS, AS WELL AS ANY PRIOR RECIPIENT.  
# IF RECIPIENT'S USE OF THE SUBJECT SOFTWARE RESULTS IN ANY LIABILITIES, DEMANDS, DAMAGES, 
# EXPENSES OR LOSSES ARISING FROM SUCH USE, INCLUDING ANY DAMAGES FROM PRODUCTS BASED ON, OR 
# RESULTING FROM, RECIPIENT'S USE OF THE SUBJECT SOFTWARE, RECIPIENT SHALL INDEMNIFY AND HOLD 
# HARMLESS THE UNITED STATES GOVERNMENT, ITS CONTRACTORS AND SUBCONTRACTORS, AS WELL AS ANY 
# PRIOR RECIPIENT, TO THE EXTENT PERMITTED BY LAW.  RECIPIENT'S SOLE REMEDY FOR ANY SUCH 
# MATTER SHALL BE THE IMMEDIATE, UNILATERAL TERMINATION OF THIS AGREEMENT.

from . import mdp
