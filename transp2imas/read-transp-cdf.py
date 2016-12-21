import sys
#import array
#import numpy
import matplotlib.pyplot as plt
from netCDF4 import Dataset

plt.rcParams.update({'font.size': 16})

#dtst = Dataset("38601I02.CDF", "r", format = "NETCDF3") # load whole dataset from dump file
dtst = Dataset("38530B10.CDF", "r", format = "NETCDF3")
#print dtst.data_model, '\n'
#print dtst, '\n'
dtstvars = [var for var in dtst.variables]  # list of all variables in data set
print 'Number of output variables: ', len(dtstvars), '\n'
#sys.exit(0)

#for var in dtstvars:
#  print var, " ,", dtst.variables[var].dimensions, " ,", dtst.variables[var].size

for var in dtstvars:
  print dtst.variables[var]

sys.exit(0)

#print 'dtst.variables[\'ZIMP\']:\n', dtst.variables['ZIMP']
#print 'dtst.variables[\'ZIMP\'][:] =', dtst.variables['ZIMP'][:], '\n\n'

#print 'dtst.variables[\'CZIMP\']:\n', dtst.variables['CZIMP']
#print 'dtst.variables[\'CZIMP\'][:] =', dtst.variables['CZIMP'][:], '\n\n'

print 'dtst.variables[\'AIMP\']:\n', dtst.variables['AIMP']
print 'dtst.variables[\'AIMP\'][:] =', dtst.variables['AIMP'][:], '\n\n'

print 'dtst.variables[\'XZIMP\']:\n', dtst.variables['XZIMP']
print 'dtst.variables[\'XZIMP\'][:] =', dtst.variables['XZIMP'][:], '\n\n'

print 'dtst.variables[\'NIMP_BE_4\']:\n', dtst.variables['NIMP_BE_4']
print 'dtst.variables[\'NIMP_BE_4\'][:] =', dtst.variables['NIMP_BE_4'][:], '\n\n'

sys.exit(0)

#plt.plot(dtst.variables['TIME'], dtst.variables['GSERROR'])
#plt.show()

print dtst.variables['LHCUR'].shape
print dtst.variables['LHCUR']
#print dtst.variables['CUR'][:, :]
print dtst.variables['X'].shape
print dtst.variables['X']

#sys.exit(0)

#plt.plot(dtst.variables['TIME'], dtst.variables['CURXT'][:, 45])
#plt.plot(dtst.variables['TIME'], dtst.variables['CURXTU'][:, 45])
#plt.show()

#plt.ylim([-1.0e-8, 1.0e-8])
#for n in range(718):
#  plt.plot(dtst.variables['X'][n, :], dtst.variables['LHCUR'][n, :])
for j in range(-1, -7, -1):
  plt.plot(dtst.variables['X'][j, :], dtst.variables['LHCUR'][j, :])
#plt.plot(dtst.variables['X'][-1, :], dtst.variables['LHCUR'][-1, :])

plt.xlabel('X')
plt.ylabel('LHCUR')
plt.grid(True)
plt.tight_layout()
plt.savefig('lhcur-final6.png', format = 'png')
plt.show()
plt.close()