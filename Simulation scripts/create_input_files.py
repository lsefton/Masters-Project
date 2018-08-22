import os
import math

vol_fracs = [0.654, 0.652]
timestep = 0.0001 # duration
timesteps = 1000000 # number of timesteps to run for
n_particles = 2500
particle_vol = 0.5 * n_particles * (4 / 3) * math.pi * (0.5 ** 3 + 0.7 ** 3)

# run command for each volume fraction and amplitude
for v in range(len(vol_fracs)):
    vol_frac = vol_fracs[v]
    box_dim = round((particle_vol / vol_frac) ** (1 / 3), 4) # rounds to 4dp
    print(box_dim)
    command = "~/Desktop/mylammps/src/lmp_serial -var vol_frac %.3f -var box_dim %g -var timestep %g -var timesteps %i -var half_n_particles %i -in in.create" % (vol_frac, box_dim, timestep, timesteps, n_particles/2)
    os.system(command)
