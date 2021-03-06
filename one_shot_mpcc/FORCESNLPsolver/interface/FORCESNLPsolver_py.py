#FORCESNLPsolver : A fast customized optimization solver.
#
#Copyright (C) 2013-2016 EMBOTECH GMBH [info@embotech.com]. All rights reserved.
#
#
#This software is intended for simulation and testing purposes only. 
#Use of this software for any commercial purpose is prohibited.
#
#This program is distributed in the hope that it will be useful.
#EMBOTECH makes NO WARRANTIES with respect to the use of the software 
#without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
#PARTICULAR PURPOSE. 
#
#EMBOTECH shall not have any liability for any damage arising from the use
#of the software.
#
#This Agreement shall exclusively be governed by and interpreted in 
#accordance with the laws of Switzerland, excluding its principles
#of conflict of laws. The Courts of Zurich-City shall have exclusive 
#jurisdiction in case of any dispute.
#
#def __init__():
'''
a Python wrapper for a fast solver generated by FORCES Pro

   OUTPUT = FORCESNLPsolver_py.FORCESNLPsolver_solve(PARAMS) solves a multistage problem
   subject to the parameters supplied in the following dictionary:
       PARAMS['x0'] - column vector of length 3220
       PARAMS['xinit'] - column vector of length 15
       PARAMS['all_parameters'] - column vector of length 2898

   OUTPUT returns the values of the last iteration of the solver where
       OUTPUT['x001'] - column vector of size 20
       OUTPUT['x002'] - column vector of size 20
       OUTPUT['x003'] - column vector of size 20
       OUTPUT['x004'] - column vector of size 20
       OUTPUT['x005'] - column vector of size 20
       OUTPUT['x006'] - column vector of size 20
       OUTPUT['x007'] - column vector of size 20
       OUTPUT['x008'] - column vector of size 20
       OUTPUT['x009'] - column vector of size 20
       OUTPUT['x010'] - column vector of size 20
       OUTPUT['x011'] - column vector of size 20
       OUTPUT['x012'] - column vector of size 20
       OUTPUT['x013'] - column vector of size 20
       OUTPUT['x014'] - column vector of size 20
       OUTPUT['x015'] - column vector of size 20
       OUTPUT['x016'] - column vector of size 20
       OUTPUT['x017'] - column vector of size 20
       OUTPUT['x018'] - column vector of size 20
       OUTPUT['x019'] - column vector of size 20
       OUTPUT['x020'] - column vector of size 20
       OUTPUT['x021'] - column vector of size 20
       OUTPUT['x022'] - column vector of size 20
       OUTPUT['x023'] - column vector of size 20
       OUTPUT['x024'] - column vector of size 20
       OUTPUT['x025'] - column vector of size 20
       OUTPUT['x026'] - column vector of size 20
       OUTPUT['x027'] - column vector of size 20
       OUTPUT['x028'] - column vector of size 20
       OUTPUT['x029'] - column vector of size 20
       OUTPUT['x030'] - column vector of size 20
       OUTPUT['x031'] - column vector of size 20
       OUTPUT['x032'] - column vector of size 20
       OUTPUT['x033'] - column vector of size 20
       OUTPUT['x034'] - column vector of size 20
       OUTPUT['x035'] - column vector of size 20
       OUTPUT['x036'] - column vector of size 20
       OUTPUT['x037'] - column vector of size 20
       OUTPUT['x038'] - column vector of size 20
       OUTPUT['x039'] - column vector of size 20
       OUTPUT['x040'] - column vector of size 20
       OUTPUT['x041'] - column vector of size 20
       OUTPUT['x042'] - column vector of size 20
       OUTPUT['x043'] - column vector of size 20
       OUTPUT['x044'] - column vector of size 20
       OUTPUT['x045'] - column vector of size 20
       OUTPUT['x046'] - column vector of size 20
       OUTPUT['x047'] - column vector of size 20
       OUTPUT['x048'] - column vector of size 20
       OUTPUT['x049'] - column vector of size 20
       OUTPUT['x050'] - column vector of size 20
       OUTPUT['x051'] - column vector of size 20
       OUTPUT['x052'] - column vector of size 20
       OUTPUT['x053'] - column vector of size 20
       OUTPUT['x054'] - column vector of size 20
       OUTPUT['x055'] - column vector of size 20
       OUTPUT['x056'] - column vector of size 20
       OUTPUT['x057'] - column vector of size 20
       OUTPUT['x058'] - column vector of size 20
       OUTPUT['x059'] - column vector of size 20
       OUTPUT['x060'] - column vector of size 20
       OUTPUT['x061'] - column vector of size 20
       OUTPUT['x062'] - column vector of size 20
       OUTPUT['x063'] - column vector of size 20
       OUTPUT['x064'] - column vector of size 20
       OUTPUT['x065'] - column vector of size 20
       OUTPUT['x066'] - column vector of size 20
       OUTPUT['x067'] - column vector of size 20
       OUTPUT['x068'] - column vector of size 20
       OUTPUT['x069'] - column vector of size 20
       OUTPUT['x070'] - column vector of size 20
       OUTPUT['x071'] - column vector of size 20
       OUTPUT['x072'] - column vector of size 20
       OUTPUT['x073'] - column vector of size 20
       OUTPUT['x074'] - column vector of size 20
       OUTPUT['x075'] - column vector of size 20
       OUTPUT['x076'] - column vector of size 20
       OUTPUT['x077'] - column vector of size 20
       OUTPUT['x078'] - column vector of size 20
       OUTPUT['x079'] - column vector of size 20
       OUTPUT['x080'] - column vector of size 20
       OUTPUT['x081'] - column vector of size 20
       OUTPUT['x082'] - column vector of size 20
       OUTPUT['x083'] - column vector of size 20
       OUTPUT['x084'] - column vector of size 20
       OUTPUT['x085'] - column vector of size 20
       OUTPUT['x086'] - column vector of size 20
       OUTPUT['x087'] - column vector of size 20
       OUTPUT['x088'] - column vector of size 20
       OUTPUT['x089'] - column vector of size 20
       OUTPUT['x090'] - column vector of size 20
       OUTPUT['x091'] - column vector of size 20
       OUTPUT['x092'] - column vector of size 20
       OUTPUT['x093'] - column vector of size 20
       OUTPUT['x094'] - column vector of size 20
       OUTPUT['x095'] - column vector of size 20
       OUTPUT['x096'] - column vector of size 20
       OUTPUT['x097'] - column vector of size 20
       OUTPUT['x098'] - column vector of size 20
       OUTPUT['x099'] - column vector of size 20
       OUTPUT['x100'] - column vector of size 20
       OUTPUT['x101'] - column vector of size 20
       OUTPUT['x102'] - column vector of size 20
       OUTPUT['x103'] - column vector of size 20
       OUTPUT['x104'] - column vector of size 20
       OUTPUT['x105'] - column vector of size 20
       OUTPUT['x106'] - column vector of size 20
       OUTPUT['x107'] - column vector of size 20
       OUTPUT['x108'] - column vector of size 20
       OUTPUT['x109'] - column vector of size 20
       OUTPUT['x110'] - column vector of size 20
       OUTPUT['x111'] - column vector of size 20
       OUTPUT['x112'] - column vector of size 20
       OUTPUT['x113'] - column vector of size 20
       OUTPUT['x114'] - column vector of size 20
       OUTPUT['x115'] - column vector of size 20
       OUTPUT['x116'] - column vector of size 20
       OUTPUT['x117'] - column vector of size 20
       OUTPUT['x118'] - column vector of size 20
       OUTPUT['x119'] - column vector of size 20
       OUTPUT['x120'] - column vector of size 20
       OUTPUT['x121'] - column vector of size 20
       OUTPUT['x122'] - column vector of size 20
       OUTPUT['x123'] - column vector of size 20
       OUTPUT['x124'] - column vector of size 20
       OUTPUT['x125'] - column vector of size 20
       OUTPUT['x126'] - column vector of size 20
       OUTPUT['x127'] - column vector of size 20
       OUTPUT['x128'] - column vector of size 20
       OUTPUT['x129'] - column vector of size 20
       OUTPUT['x130'] - column vector of size 20
       OUTPUT['x131'] - column vector of size 20
       OUTPUT['x132'] - column vector of size 20
       OUTPUT['x133'] - column vector of size 20
       OUTPUT['x134'] - column vector of size 20
       OUTPUT['x135'] - column vector of size 20
       OUTPUT['x136'] - column vector of size 20
       OUTPUT['x137'] - column vector of size 20
       OUTPUT['x138'] - column vector of size 20
       OUTPUT['x139'] - column vector of size 20
       OUTPUT['x140'] - column vector of size 20
       OUTPUT['x141'] - column vector of size 20
       OUTPUT['x142'] - column vector of size 20
       OUTPUT['x143'] - column vector of size 20
       OUTPUT['x144'] - column vector of size 20
       OUTPUT['x145'] - column vector of size 20
       OUTPUT['x146'] - column vector of size 20
       OUTPUT['x147'] - column vector of size 20
       OUTPUT['x148'] - column vector of size 20
       OUTPUT['x149'] - column vector of size 20
       OUTPUT['x150'] - column vector of size 20
       OUTPUT['x151'] - column vector of size 20
       OUTPUT['x152'] - column vector of size 20
       OUTPUT['x153'] - column vector of size 20
       OUTPUT['x154'] - column vector of size 20
       OUTPUT['x155'] - column vector of size 20
       OUTPUT['x156'] - column vector of size 20
       OUTPUT['x157'] - column vector of size 20
       OUTPUT['x158'] - column vector of size 20
       OUTPUT['x159'] - column vector of size 20
       OUTPUT['x160'] - column vector of size 20
       OUTPUT['x161'] - column vector of size 20

   [OUTPUT, EXITFLAG] = FORCESNLPsolver_py.FORCESNLPsolver_solve(PARAMS) returns additionally
   the integer EXITFLAG indicating the state of the solution with 
       1 - Optimal solution has been found (subject to desired accuracy)
       2 - (only branch-and-bound) A feasible point has been identified for which the objective value is no more than codeoptions.mip.mipgap*100 per cent worse than the global optimum 
       0 - Timeout - maximum number of iterations reached
      -1 - (only branch-and-bound) Infeasible problem (problems solving the root relaxation to the desired accuracy)
      -2 - (only branch-and-bound) Out of memory - cannot fit branch and bound nodes into pre-allocated memory.
      -6 - NaN or INF occured during evaluation of functions and derivatives. Please check your initial guess.
      -7 - Method could not progress. Problem may be infeasible. Run FORCESdiagnostics on your problem to check for most common errors in the formulation.
     -10 - The convex solver could not proceed due to an internal error
    -100 - License error

   [OUTPUT, EXITFLAG, INFO] = FORCESNLPsolver_py.FORCESNLPsolver_solve(PARAMS) returns 
   additional information about the last iterate:
       INFO.it        - number of iterations that lead to this result
       INFO.it2opt    - number of convex solves
       INFO.res_eq    - max. equality constraint residual
       INFO.res_ineq  - max. inequality constraint residual
       INFO.pobj      - primal objective
       INFO.mu        - duality measure
       INFO.solvetime - Time needed for solve (wall clock time)
       INFO.fevalstime - Time needed for solve (wall clock time)

 See also COPYING

'''

import ctypes
import os
import numpy as np
import numpy.ctypeslib as npct
import sys

#_lib = ctypes.CDLL(os.path.join(os.getcwd(),'FORCESNLPsolver/lib/FORCESNLPsolver.so')) 
try:
	_lib = ctypes.CDLL(os.path.join(os.path.dirname(os.path.abspath(__file__)),'FORCESNLPsolver/lib/FORCESNLPsolver.so'))
	csolver = getattr(_lib,'FORCESNLPsolver_solve')
except:
	_lib = ctypes.CDLL(os.path.join(os.path.dirname(os.path.abspath(__file__)),'FORCESNLPsolver/lib/libFORCESNLPsolver.so'))
	csolver = getattr(_lib,'FORCESNLPsolver_solve')

class FORCESNLPsolver_params_ctypes(ctypes.Structure):
#	@classmethod
#	def from_param(self):
#		return self
	_fields_ = [('x0', ctypes.c_double * 3220),
('xinit', ctypes.c_double * 15),
('all_parameters', ctypes.c_double * 2898),
]

FORCESNLPsolver_params = {'x0' : np.array([]),
'xinit' : np.array([]),
'all_parameters' : np.array([]),
}
params = {'x0' : np.array([]),
'xinit' : np.array([]),
'all_parameters' : np.array([]),
}

class FORCESNLPsolver_outputs_ctypes(ctypes.Structure):
#	@classmethod
#	def from_param(self):
#		return self
	_fields_ = [('x001', ctypes.c_double * 20),
('x002', ctypes.c_double * 20),
('x003', ctypes.c_double * 20),
('x004', ctypes.c_double * 20),
('x005', ctypes.c_double * 20),
('x006', ctypes.c_double * 20),
('x007', ctypes.c_double * 20),
('x008', ctypes.c_double * 20),
('x009', ctypes.c_double * 20),
('x010', ctypes.c_double * 20),
('x011', ctypes.c_double * 20),
('x012', ctypes.c_double * 20),
('x013', ctypes.c_double * 20),
('x014', ctypes.c_double * 20),
('x015', ctypes.c_double * 20),
('x016', ctypes.c_double * 20),
('x017', ctypes.c_double * 20),
('x018', ctypes.c_double * 20),
('x019', ctypes.c_double * 20),
('x020', ctypes.c_double * 20),
('x021', ctypes.c_double * 20),
('x022', ctypes.c_double * 20),
('x023', ctypes.c_double * 20),
('x024', ctypes.c_double * 20),
('x025', ctypes.c_double * 20),
('x026', ctypes.c_double * 20),
('x027', ctypes.c_double * 20),
('x028', ctypes.c_double * 20),
('x029', ctypes.c_double * 20),
('x030', ctypes.c_double * 20),
('x031', ctypes.c_double * 20),
('x032', ctypes.c_double * 20),
('x033', ctypes.c_double * 20),
('x034', ctypes.c_double * 20),
('x035', ctypes.c_double * 20),
('x036', ctypes.c_double * 20),
('x037', ctypes.c_double * 20),
('x038', ctypes.c_double * 20),
('x039', ctypes.c_double * 20),
('x040', ctypes.c_double * 20),
('x041', ctypes.c_double * 20),
('x042', ctypes.c_double * 20),
('x043', ctypes.c_double * 20),
('x044', ctypes.c_double * 20),
('x045', ctypes.c_double * 20),
('x046', ctypes.c_double * 20),
('x047', ctypes.c_double * 20),
('x048', ctypes.c_double * 20),
('x049', ctypes.c_double * 20),
('x050', ctypes.c_double * 20),
('x051', ctypes.c_double * 20),
('x052', ctypes.c_double * 20),
('x053', ctypes.c_double * 20),
('x054', ctypes.c_double * 20),
('x055', ctypes.c_double * 20),
('x056', ctypes.c_double * 20),
('x057', ctypes.c_double * 20),
('x058', ctypes.c_double * 20),
('x059', ctypes.c_double * 20),
('x060', ctypes.c_double * 20),
('x061', ctypes.c_double * 20),
('x062', ctypes.c_double * 20),
('x063', ctypes.c_double * 20),
('x064', ctypes.c_double * 20),
('x065', ctypes.c_double * 20),
('x066', ctypes.c_double * 20),
('x067', ctypes.c_double * 20),
('x068', ctypes.c_double * 20),
('x069', ctypes.c_double * 20),
('x070', ctypes.c_double * 20),
('x071', ctypes.c_double * 20),
('x072', ctypes.c_double * 20),
('x073', ctypes.c_double * 20),
('x074', ctypes.c_double * 20),
('x075', ctypes.c_double * 20),
('x076', ctypes.c_double * 20),
('x077', ctypes.c_double * 20),
('x078', ctypes.c_double * 20),
('x079', ctypes.c_double * 20),
('x080', ctypes.c_double * 20),
('x081', ctypes.c_double * 20),
('x082', ctypes.c_double * 20),
('x083', ctypes.c_double * 20),
('x084', ctypes.c_double * 20),
('x085', ctypes.c_double * 20),
('x086', ctypes.c_double * 20),
('x087', ctypes.c_double * 20),
('x088', ctypes.c_double * 20),
('x089', ctypes.c_double * 20),
('x090', ctypes.c_double * 20),
('x091', ctypes.c_double * 20),
('x092', ctypes.c_double * 20),
('x093', ctypes.c_double * 20),
('x094', ctypes.c_double * 20),
('x095', ctypes.c_double * 20),
('x096', ctypes.c_double * 20),
('x097', ctypes.c_double * 20),
('x098', ctypes.c_double * 20),
('x099', ctypes.c_double * 20),
('x100', ctypes.c_double * 20),
('x101', ctypes.c_double * 20),
('x102', ctypes.c_double * 20),
('x103', ctypes.c_double * 20),
('x104', ctypes.c_double * 20),
('x105', ctypes.c_double * 20),
('x106', ctypes.c_double * 20),
('x107', ctypes.c_double * 20),
('x108', ctypes.c_double * 20),
('x109', ctypes.c_double * 20),
('x110', ctypes.c_double * 20),
('x111', ctypes.c_double * 20),
('x112', ctypes.c_double * 20),
('x113', ctypes.c_double * 20),
('x114', ctypes.c_double * 20),
('x115', ctypes.c_double * 20),
('x116', ctypes.c_double * 20),
('x117', ctypes.c_double * 20),
('x118', ctypes.c_double * 20),
('x119', ctypes.c_double * 20),
('x120', ctypes.c_double * 20),
('x121', ctypes.c_double * 20),
('x122', ctypes.c_double * 20),
('x123', ctypes.c_double * 20),
('x124', ctypes.c_double * 20),
('x125', ctypes.c_double * 20),
('x126', ctypes.c_double * 20),
('x127', ctypes.c_double * 20),
('x128', ctypes.c_double * 20),
('x129', ctypes.c_double * 20),
('x130', ctypes.c_double * 20),
('x131', ctypes.c_double * 20),
('x132', ctypes.c_double * 20),
('x133', ctypes.c_double * 20),
('x134', ctypes.c_double * 20),
('x135', ctypes.c_double * 20),
('x136', ctypes.c_double * 20),
('x137', ctypes.c_double * 20),
('x138', ctypes.c_double * 20),
('x139', ctypes.c_double * 20),
('x140', ctypes.c_double * 20),
('x141', ctypes.c_double * 20),
('x142', ctypes.c_double * 20),
('x143', ctypes.c_double * 20),
('x144', ctypes.c_double * 20),
('x145', ctypes.c_double * 20),
('x146', ctypes.c_double * 20),
('x147', ctypes.c_double * 20),
('x148', ctypes.c_double * 20),
('x149', ctypes.c_double * 20),
('x150', ctypes.c_double * 20),
('x151', ctypes.c_double * 20),
('x152', ctypes.c_double * 20),
('x153', ctypes.c_double * 20),
('x154', ctypes.c_double * 20),
('x155', ctypes.c_double * 20),
('x156', ctypes.c_double * 20),
('x157', ctypes.c_double * 20),
('x158', ctypes.c_double * 20),
('x159', ctypes.c_double * 20),
('x160', ctypes.c_double * 20),
('x161', ctypes.c_double * 20),
]

FORCESNLPsolver_outputs = {'x001' : np.array([]),
'x002' : np.array([]),
'x003' : np.array([]),
'x004' : np.array([]),
'x005' : np.array([]),
'x006' : np.array([]),
'x007' : np.array([]),
'x008' : np.array([]),
'x009' : np.array([]),
'x010' : np.array([]),
'x011' : np.array([]),
'x012' : np.array([]),
'x013' : np.array([]),
'x014' : np.array([]),
'x015' : np.array([]),
'x016' : np.array([]),
'x017' : np.array([]),
'x018' : np.array([]),
'x019' : np.array([]),
'x020' : np.array([]),
'x021' : np.array([]),
'x022' : np.array([]),
'x023' : np.array([]),
'x024' : np.array([]),
'x025' : np.array([]),
'x026' : np.array([]),
'x027' : np.array([]),
'x028' : np.array([]),
'x029' : np.array([]),
'x030' : np.array([]),
'x031' : np.array([]),
'x032' : np.array([]),
'x033' : np.array([]),
'x034' : np.array([]),
'x035' : np.array([]),
'x036' : np.array([]),
'x037' : np.array([]),
'x038' : np.array([]),
'x039' : np.array([]),
'x040' : np.array([]),
'x041' : np.array([]),
'x042' : np.array([]),
'x043' : np.array([]),
'x044' : np.array([]),
'x045' : np.array([]),
'x046' : np.array([]),
'x047' : np.array([]),
'x048' : np.array([]),
'x049' : np.array([]),
'x050' : np.array([]),
'x051' : np.array([]),
'x052' : np.array([]),
'x053' : np.array([]),
'x054' : np.array([]),
'x055' : np.array([]),
'x056' : np.array([]),
'x057' : np.array([]),
'x058' : np.array([]),
'x059' : np.array([]),
'x060' : np.array([]),
'x061' : np.array([]),
'x062' : np.array([]),
'x063' : np.array([]),
'x064' : np.array([]),
'x065' : np.array([]),
'x066' : np.array([]),
'x067' : np.array([]),
'x068' : np.array([]),
'x069' : np.array([]),
'x070' : np.array([]),
'x071' : np.array([]),
'x072' : np.array([]),
'x073' : np.array([]),
'x074' : np.array([]),
'x075' : np.array([]),
'x076' : np.array([]),
'x077' : np.array([]),
'x078' : np.array([]),
'x079' : np.array([]),
'x080' : np.array([]),
'x081' : np.array([]),
'x082' : np.array([]),
'x083' : np.array([]),
'x084' : np.array([]),
'x085' : np.array([]),
'x086' : np.array([]),
'x087' : np.array([]),
'x088' : np.array([]),
'x089' : np.array([]),
'x090' : np.array([]),
'x091' : np.array([]),
'x092' : np.array([]),
'x093' : np.array([]),
'x094' : np.array([]),
'x095' : np.array([]),
'x096' : np.array([]),
'x097' : np.array([]),
'x098' : np.array([]),
'x099' : np.array([]),
'x100' : np.array([]),
'x101' : np.array([]),
'x102' : np.array([]),
'x103' : np.array([]),
'x104' : np.array([]),
'x105' : np.array([]),
'x106' : np.array([]),
'x107' : np.array([]),
'x108' : np.array([]),
'x109' : np.array([]),
'x110' : np.array([]),
'x111' : np.array([]),
'x112' : np.array([]),
'x113' : np.array([]),
'x114' : np.array([]),
'x115' : np.array([]),
'x116' : np.array([]),
'x117' : np.array([]),
'x118' : np.array([]),
'x119' : np.array([]),
'x120' : np.array([]),
'x121' : np.array([]),
'x122' : np.array([]),
'x123' : np.array([]),
'x124' : np.array([]),
'x125' : np.array([]),
'x126' : np.array([]),
'x127' : np.array([]),
'x128' : np.array([]),
'x129' : np.array([]),
'x130' : np.array([]),
'x131' : np.array([]),
'x132' : np.array([]),
'x133' : np.array([]),
'x134' : np.array([]),
'x135' : np.array([]),
'x136' : np.array([]),
'x137' : np.array([]),
'x138' : np.array([]),
'x139' : np.array([]),
'x140' : np.array([]),
'x141' : np.array([]),
'x142' : np.array([]),
'x143' : np.array([]),
'x144' : np.array([]),
'x145' : np.array([]),
'x146' : np.array([]),
'x147' : np.array([]),
'x148' : np.array([]),
'x149' : np.array([]),
'x150' : np.array([]),
'x151' : np.array([]),
'x152' : np.array([]),
'x153' : np.array([]),
'x154' : np.array([]),
'x155' : np.array([]),
'x156' : np.array([]),
'x157' : np.array([]),
'x158' : np.array([]),
'x159' : np.array([]),
'x160' : np.array([]),
'x161' : np.array([]),
}


class FORCESNLPsolver_info(ctypes.Structure):
#	@classmethod
#	def from_param(self):
#		return self
	_fields_ = [('it', ctypes.c_int),
('it2opt', ctypes.c_int),
('res_eq', ctypes.c_double),
('res_ineq', ctypes.c_double),
('pobj',ctypes.c_double),
('mu',ctypes.c_double),
('solvetime',ctypes.c_double)
('fevalstime',ctypes.c_double)
]

class FILE(ctypes.Structure):
        pass
if sys.version_info.major == 2:
	PyFile_AsFile = ctypes.pythonapi.PyFile_AsFile # problem here with python 3 http://stackoverflow.com/questions/16130268/python-3-replacement-for-pyfile-asfile
	PyFile_AsFile.argtypes = [ctypes.py_object]
	PyFile_AsFile.restype = ctypes.POINTER(FILE)

# determine data types for solver function prototype 
csolver.argtypes = ( ctypes.POINTER(FORCESNLPsolver_params_ctypes), ctypes.POINTER(FORCESNLPsolver_outputs_ctypes), ctypes.POINTER(FORCESNLPsolver_info), ctypes.POINTER(FILE))
csolver.restype = ctypes.c_int

def FORCESNLPsolver_solve(params_arg):
	'''
a Python wrapper for a fast solver generated by FORCES Pro

   OUTPUT = FORCESNLPsolver_py.FORCESNLPsolver_solve(PARAMS) solves a multistage problem
   subject to the parameters supplied in the following dictionary:
       PARAMS['x0'] - column vector of length 3220
       PARAMS['xinit'] - column vector of length 15
       PARAMS['all_parameters'] - column vector of length 2898

   OUTPUT returns the values of the last iteration of the solver where
       OUTPUT['x001'] - column vector of size 20
       OUTPUT['x002'] - column vector of size 20
       OUTPUT['x003'] - column vector of size 20
       OUTPUT['x004'] - column vector of size 20
       OUTPUT['x005'] - column vector of size 20
       OUTPUT['x006'] - column vector of size 20
       OUTPUT['x007'] - column vector of size 20
       OUTPUT['x008'] - column vector of size 20
       OUTPUT['x009'] - column vector of size 20
       OUTPUT['x010'] - column vector of size 20
       OUTPUT['x011'] - column vector of size 20
       OUTPUT['x012'] - column vector of size 20
       OUTPUT['x013'] - column vector of size 20
       OUTPUT['x014'] - column vector of size 20
       OUTPUT['x015'] - column vector of size 20
       OUTPUT['x016'] - column vector of size 20
       OUTPUT['x017'] - column vector of size 20
       OUTPUT['x018'] - column vector of size 20
       OUTPUT['x019'] - column vector of size 20
       OUTPUT['x020'] - column vector of size 20
       OUTPUT['x021'] - column vector of size 20
       OUTPUT['x022'] - column vector of size 20
       OUTPUT['x023'] - column vector of size 20
       OUTPUT['x024'] - column vector of size 20
       OUTPUT['x025'] - column vector of size 20
       OUTPUT['x026'] - column vector of size 20
       OUTPUT['x027'] - column vector of size 20
       OUTPUT['x028'] - column vector of size 20
       OUTPUT['x029'] - column vector of size 20
       OUTPUT['x030'] - column vector of size 20
       OUTPUT['x031'] - column vector of size 20
       OUTPUT['x032'] - column vector of size 20
       OUTPUT['x033'] - column vector of size 20
       OUTPUT['x034'] - column vector of size 20
       OUTPUT['x035'] - column vector of size 20
       OUTPUT['x036'] - column vector of size 20
       OUTPUT['x037'] - column vector of size 20
       OUTPUT['x038'] - column vector of size 20
       OUTPUT['x039'] - column vector of size 20
       OUTPUT['x040'] - column vector of size 20
       OUTPUT['x041'] - column vector of size 20
       OUTPUT['x042'] - column vector of size 20
       OUTPUT['x043'] - column vector of size 20
       OUTPUT['x044'] - column vector of size 20
       OUTPUT['x045'] - column vector of size 20
       OUTPUT['x046'] - column vector of size 20
       OUTPUT['x047'] - column vector of size 20
       OUTPUT['x048'] - column vector of size 20
       OUTPUT['x049'] - column vector of size 20
       OUTPUT['x050'] - column vector of size 20
       OUTPUT['x051'] - column vector of size 20
       OUTPUT['x052'] - column vector of size 20
       OUTPUT['x053'] - column vector of size 20
       OUTPUT['x054'] - column vector of size 20
       OUTPUT['x055'] - column vector of size 20
       OUTPUT['x056'] - column vector of size 20
       OUTPUT['x057'] - column vector of size 20
       OUTPUT['x058'] - column vector of size 20
       OUTPUT['x059'] - column vector of size 20
       OUTPUT['x060'] - column vector of size 20
       OUTPUT['x061'] - column vector of size 20
       OUTPUT['x062'] - column vector of size 20
       OUTPUT['x063'] - column vector of size 20
       OUTPUT['x064'] - column vector of size 20
       OUTPUT['x065'] - column vector of size 20
       OUTPUT['x066'] - column vector of size 20
       OUTPUT['x067'] - column vector of size 20
       OUTPUT['x068'] - column vector of size 20
       OUTPUT['x069'] - column vector of size 20
       OUTPUT['x070'] - column vector of size 20
       OUTPUT['x071'] - column vector of size 20
       OUTPUT['x072'] - column vector of size 20
       OUTPUT['x073'] - column vector of size 20
       OUTPUT['x074'] - column vector of size 20
       OUTPUT['x075'] - column vector of size 20
       OUTPUT['x076'] - column vector of size 20
       OUTPUT['x077'] - column vector of size 20
       OUTPUT['x078'] - column vector of size 20
       OUTPUT['x079'] - column vector of size 20
       OUTPUT['x080'] - column vector of size 20
       OUTPUT['x081'] - column vector of size 20
       OUTPUT['x082'] - column vector of size 20
       OUTPUT['x083'] - column vector of size 20
       OUTPUT['x084'] - column vector of size 20
       OUTPUT['x085'] - column vector of size 20
       OUTPUT['x086'] - column vector of size 20
       OUTPUT['x087'] - column vector of size 20
       OUTPUT['x088'] - column vector of size 20
       OUTPUT['x089'] - column vector of size 20
       OUTPUT['x090'] - column vector of size 20
       OUTPUT['x091'] - column vector of size 20
       OUTPUT['x092'] - column vector of size 20
       OUTPUT['x093'] - column vector of size 20
       OUTPUT['x094'] - column vector of size 20
       OUTPUT['x095'] - column vector of size 20
       OUTPUT['x096'] - column vector of size 20
       OUTPUT['x097'] - column vector of size 20
       OUTPUT['x098'] - column vector of size 20
       OUTPUT['x099'] - column vector of size 20
       OUTPUT['x100'] - column vector of size 20
       OUTPUT['x101'] - column vector of size 20
       OUTPUT['x102'] - column vector of size 20
       OUTPUT['x103'] - column vector of size 20
       OUTPUT['x104'] - column vector of size 20
       OUTPUT['x105'] - column vector of size 20
       OUTPUT['x106'] - column vector of size 20
       OUTPUT['x107'] - column vector of size 20
       OUTPUT['x108'] - column vector of size 20
       OUTPUT['x109'] - column vector of size 20
       OUTPUT['x110'] - column vector of size 20
       OUTPUT['x111'] - column vector of size 20
       OUTPUT['x112'] - column vector of size 20
       OUTPUT['x113'] - column vector of size 20
       OUTPUT['x114'] - column vector of size 20
       OUTPUT['x115'] - column vector of size 20
       OUTPUT['x116'] - column vector of size 20
       OUTPUT['x117'] - column vector of size 20
       OUTPUT['x118'] - column vector of size 20
       OUTPUT['x119'] - column vector of size 20
       OUTPUT['x120'] - column vector of size 20
       OUTPUT['x121'] - column vector of size 20
       OUTPUT['x122'] - column vector of size 20
       OUTPUT['x123'] - column vector of size 20
       OUTPUT['x124'] - column vector of size 20
       OUTPUT['x125'] - column vector of size 20
       OUTPUT['x126'] - column vector of size 20
       OUTPUT['x127'] - column vector of size 20
       OUTPUT['x128'] - column vector of size 20
       OUTPUT['x129'] - column vector of size 20
       OUTPUT['x130'] - column vector of size 20
       OUTPUT['x131'] - column vector of size 20
       OUTPUT['x132'] - column vector of size 20
       OUTPUT['x133'] - column vector of size 20
       OUTPUT['x134'] - column vector of size 20
       OUTPUT['x135'] - column vector of size 20
       OUTPUT['x136'] - column vector of size 20
       OUTPUT['x137'] - column vector of size 20
       OUTPUT['x138'] - column vector of size 20
       OUTPUT['x139'] - column vector of size 20
       OUTPUT['x140'] - column vector of size 20
       OUTPUT['x141'] - column vector of size 20
       OUTPUT['x142'] - column vector of size 20
       OUTPUT['x143'] - column vector of size 20
       OUTPUT['x144'] - column vector of size 20
       OUTPUT['x145'] - column vector of size 20
       OUTPUT['x146'] - column vector of size 20
       OUTPUT['x147'] - column vector of size 20
       OUTPUT['x148'] - column vector of size 20
       OUTPUT['x149'] - column vector of size 20
       OUTPUT['x150'] - column vector of size 20
       OUTPUT['x151'] - column vector of size 20
       OUTPUT['x152'] - column vector of size 20
       OUTPUT['x153'] - column vector of size 20
       OUTPUT['x154'] - column vector of size 20
       OUTPUT['x155'] - column vector of size 20
       OUTPUT['x156'] - column vector of size 20
       OUTPUT['x157'] - column vector of size 20
       OUTPUT['x158'] - column vector of size 20
       OUTPUT['x159'] - column vector of size 20
       OUTPUT['x160'] - column vector of size 20
       OUTPUT['x161'] - column vector of size 20

   [OUTPUT, EXITFLAG] = FORCESNLPsolver_py.FORCESNLPsolver_solve(PARAMS) returns additionally
   the integer EXITFLAG indicating the state of the solution with 
       1 - Optimal solution has been found (subject to desired accuracy)
       2 - (only branch-and-bound) A feasible point has been identified for which the objective value is no more than codeoptions.mip.mipgap*100 per cent worse than the global optimum 
       0 - Timeout - maximum number of iterations reached
      -1 - (only branch-and-bound) Infeasible problem (problems solving the root relaxation to the desired accuracy)
      -2 - (only branch-and-bound) Out of memory - cannot fit branch and bound nodes into pre-allocated memory.
      -6 - NaN or INF occured during evaluation of functions and derivatives. Please check your initial guess.
      -7 - Method could not progress. Problem may be infeasible. Run FORCESdiagnostics on your problem to check for most common errors in the formulation.
     -10 - The convex solver could not proceed due to an internal error
    -100 - License error

   [OUTPUT, EXITFLAG, INFO] = FORCESNLPsolver_py.FORCESNLPsolver_solve(PARAMS) returns 
   additional information about the last iterate:
       INFO.it        - number of iterations that lead to this result
       INFO.it2opt    - number of convex solves
       INFO.res_eq    - max. equality constraint residual
       INFO.res_ineq  - max. inequality constraint residual
       INFO.pobj      - primal objective
       INFO.mu        - duality measure
       INFO.solvetime - Time needed for solve (wall clock time)
       INFO.fevalstime - Time needed for solve (wall clock time)

 See also COPYING

	'''
	global _lib

	# convert parameters
	params_py = FORCESNLPsolver_params_ctypes()
	for par in params_arg:
		try:
			#setattr(params_py, par, npct.as_ctypes(np.reshape(params_arg[par],np.size(params_arg[par]),order='A'))) 
			params_arg[par] = np.require(params_arg[par], dtype=np.float64, requirements='F')
			setattr(params_py, par, npct.as_ctypes(np.reshape(params_arg[par],np.size(params_arg[par]),order='F')))  
		except:
			raise ValueError('Parameter ' + par + ' does not have the appropriate dimensions or data type. Please use numpy arrays for parameters.')
    
	outputs_py = FORCESNLPsolver_outputs_ctypes()
	info_py = FORCESNLPsolver_info()
	if sys.version_info.major == 2:
		if sys.platform.startswith('win'):
			fp = None # if set to none, the solver prints to stdout by default - necessary because we have an access violation otherwise under windows
		else:
			#fp = open('stdout_temp.txt','w')
			fp = sys.stdout
		try:
			PyFile_AsFile.restype = ctypes.POINTER(FILE)
			exitflag = _lib.FORCESNLPsolver_solve( params_py, ctypes.byref(outputs_py), ctypes.byref(info_py), PyFile_AsFile(fp) )
			#fp = open('stdout_temp.txt','r')
			#print (fp.read())
			#fp.close()
		except:
			#print 'Problem with solver'
			raise
	elif sys.version_info.major == 3:
		if sys.platform.startswith('win'):
			libc = ctypes.cdll.msvcrt
		elif sys.platform.startswith('darwin'):
			libc = ctypes.CDLL('libc.dylib')
		else:
			libc = ctypes.CDLL('libc.so.6')       # Open libc
		cfopen = getattr(libc,'fopen')        # Get its fopen
		cfopen.restype = ctypes.POINTER(FILE) # Yes, fopen gives a file pointer
		cfopen.argtypes = [ctypes.c_char_p, ctypes.c_char_p] # Yes, fopen gives a file pointer 
		fp = cfopen('stdout_temp.txt'.encode('utf-8'),'w'.encode('utf-8'))    # Use that fopen 

		try:
			if sys.platform.startswith('win'):
				exitflag = _lib.FORCESNLPsolver_solve( params_py, ctypes.byref(outputs_py), ctypes.byref(info_py), None )
			else:
				exitflag = _lib.FORCESNLPsolver_solve( params_py, ctypes.byref(outputs_py), ctypes.byref(info_py), fp )
			libc.fclose(fp)
			fptemp = open('stdout_temp.txt','r')
			print (fptemp.read())
			fptemp.close()			
		except:
			#print 'Problem with solver'
			raise

	# convert outputs
	for out in FORCESNLPsolver_outputs:
		FORCESNLPsolver_outputs[out] = npct.as_array(getattr(outputs_py,out))

	return FORCESNLPsolver_outputs,int(exitflag),info_py

solve = FORCESNLPsolver_solve


