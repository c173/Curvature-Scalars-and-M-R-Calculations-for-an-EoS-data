import matplotlib.pyplot as plt
import numpy as np

rho_c1, Mass1, Radius1, stiffness1, compactness1, moi1 = np.loadtxt('MR1.out', float, usecols=(0, 1, 2, 3, 4, 5), unpack=True)
rho_c2, Mass2, Radius2, stiffness2, compactness2, moi2 = np.loadtxt('MR2.out', float, usecols=(0, 1, 2, 3, 4, 5), unpack=True)
rho_c3, Mass3, Radius3, stiffness3, compactness3, moi3 = np.loadtxt('MR3.out', float, usecols=(0, 1, 2, 3, 4, 5), unpack=True)
rho_c4, Mass4, Radius4, stiffness4, compactness4, moi4 = np.loadtxt('MR4.out', float, usecols=(0, 1, 2, 3, 4, 5), unpack=True)
rho_c5, Mass5, Radius5, stiffness5, compactness5, moi5 = np.loadtxt('MR5.out', float, usecols=(0, 1, 2, 3, 4, 5), unpack=True)
rho_c6, Mass6, Radius6, stiffness6, compactness6, moi6 = np.loadtxt('MR6.out', float, usecols=(0, 1, 2, 3, 4, 5), unpack=True)
rho_c7, Mass7, Radius7, stiffness7, compactness7, moi7 = np.loadtxt('MR7.out', float, usecols=(0, 1, 2, 3, 4, 5), unpack=True)
rho_c8, Mass8, Radius8, stiffness8, compactness8, moi8 = np.loadtxt('MR8.out', float, usecols=(0, 1, 2, 3, 4, 5), unpack=True)


# rho_c vs M
plt.figure(1)
plt.plot(rho_c1, Mass1, 'r', label='AP4')
plt.plot(rho_c2, Mass2, 'g', label='Sly4')
plt.plot(rho_c3, Mass3, 'b', label='av18')
plt.plot(rho_c4, Mass4, 'm', label='wff4')
plt.plot(rho_c5, Mass5, 'purple', label='FPS')
plt.plot(rho_c6, Mass6, 'olive', label='Engvik')
plt.plot(rho_c7, Mass7, 'orange', label='gm1nph')
plt.plot(rho_c8, Mass8, 'lime', label='sqm3')
plt.legend()
plt.xscale('log')
plt.xlabel(r'$\rho_{\rm c}$ (g cm$^{-3}$)')
plt.ylabel(r'$M/M_{\odot}$')
plt.savefig("rho_c-mass.pdf", bbox_inches='tight', pad_inches=0)

# P_c/rho_c vs compactness
plt.figure(2)
plt.plot(stiffness1, compactness1, 'r', label='AP4')
plt.plot(stiffness2, compactness2, 'g', label='Sly4')
plt.plot(stiffness3, compactness3, 'b', label='av18')
plt.plot(stiffness4, compactness4, 'm', label='wff4')
plt.plot(stiffness5, compactness5, 'purple', label='FPS')
plt.plot(stiffness6, compactness6, 'olive', label='Engvik')
plt.plot(stiffness7, compactness7, 'orange', label='gm1nph')
plt.plot(stiffness8, compactness8, 'lime', label='sqm3')
plt.legend()
plt.xlabel(r'$P_{\rm c}/\rho_{\rm c}c^2$')
plt.ylabel(r'$2GM/Rc^2$')
plt.savefig("stiffness-compactness.pdf", bbox_inches='tight', pad_inches=0)

# Mass-Radius
plt.figure(3)
plt.xlim(6, 18)
plt.ylim([0,3])
plt.plot(Radius1, Mass1, 'r', label='AP4')
plt.plot(Radius2, Mass2, 'g', label='Sly4')
plt.plot(Radius3, Mass3, 'b', label='av18')
plt.plot(Radius4, Mass4, 'm', label='wff4')
plt.plot(Radius5, Mass5, 'purple', label='FPS')
plt.plot(Radius6, Mass6, 'olive', label='Engvik')
plt.plot(Radius7, Mass7, 'orange', label='gm1nph')
plt.plot(Radius8, Mass8, 'lime', label='sqm3')
plt.legend()
plt.xlabel(r'$R$ (km)')
plt.ylabel(r'$M/M_{\odot}$')
plt.savefig('MR.pdf', bbox_inches='tight', pad_inches=0)

plt.figure(4)
plt.plot(Mass1, moi1, 'r', label='AP4')
plt.plot(Mass2, moi2, 'g', label='Sly4')
plt.plot(Mass3, moi3, 'b', label='av18')
plt.plot(Mass4, moi4, 'm', label='wff4')
plt.plot(Mass5, moi5, 'purple', label='FPS')
plt.plot(Mass6, moi6, 'olive', label='Engvik')
plt.plot(Mass7, moi7, 'orange', label='gm1nph')
plt.plot(Mass8, moi8, 'lime', label='sqm3')
plt.legend()
plt.xlabel(r'$M/M_{\odot}$')
plt.ylabel(r'$I$ [$10^{45}$ g cm$^{2}$]')
plt.savefig("moment-of-inertia.pdf", bbox_inches='tight', pad_inches=0)

plt.show()
