from utils import vars

add_branch = True
if add_branch:
    FILENAME = f"data/N{vars.N_ATOMS}/N{vars.N_ATOMS_TOTAL}_lammps.in"
else:
    FILENAME = f"data/N{vars.N_ATOMS}/N{vars.N_ATOMS}_lammps.in"

with open(FILENAME, "w") as file:
    file.write(f"# LAMMPS input file - ionic\n\n")

    # ---- variables ---- #
    file.write(f"# ---- variables ----\n")
    file.write(f"variable      N                  equal {vars.N_ATOMS_TOTAL if add_branch else vars.N_ATOMS}\n")
    file.write(f"variable      print_thermo       equal 1000\n")
    file.write("\n")
    file.write(f"variable      bx                 equal {vars.BX}\n")
    file.write(f"variable      by                 equal {vars.BY}\n")
    file.write(f"variable      bz                 equal {vars.BZ}\n")
    file.write("\n")
    file.write(f"variable      sim_time           equal {vars.SIMULATION_TIME}\n")
    file.write("\n")
    file.write(f"variable      epsP               equal 1.0\n")
    file.write(f"variable      epsP_NP            equal 1.0\n")
    file.write(f"variable      epsNP              equal 1.0\n")
    file.write(f"variable      Th                 equal 4.0\n")
    file.write(f"variable      Th                 equal 4.0\n")
    file.write(f"variable      T                  equal 2.0\n")
    file.write(f"variable      gamma              equal 2.0\n")
    file.write(f"variable      cut                equal 6.0\n")
    file.write("\n")
    file.write(f"variable      kstiff             equal (10/2)\n")
    file.write("\n")
    file.write(f"variable      cutoffS            equal 2^(1/6)\n")
    file.write(f"variable      cutoffL            equal 3.0\n")
    file.write("\n")
    file.write(f"variable      NPD                equal 1.0\n")
    file.write(f"variable      monoD              equal 1.0\n")
    file.write("variable      delta_NPNP         equal (${NPD}-${monoD})     #HEAD-HEAD\n")
    file.write("variable      delta_NPm          equal 0.5*(${NPD}-${monoD}) #HEAD-monomer\n")
    file.write("\n")

    # ---- lennard-jones type of interactions and bonds ----
    file.write(f"# ---- lennard-jones type of interactions and bonds ----\n")
    file.write("units         lj\n")
    file.write("atom_style    hybrid charge bond\n")
    file.write("\n")

    # ---- the style of boundaries for the global simulation box in each dimension ----
    file.write("# ---- periodic boundaries for the global simulation box in each dimension ----\n")
    file.write("boundary      p p p\n")
    file.write("\n")

    # ---- read data ----
    file.write("# ---- read data ----\n")
    file.write("read_data      N${N}\n")
    file.write("\n")

    # ---- group data ----
    file.write("# ---- group atoms ----\n")
    file.write("group         HEAD               type 1\n")
    file.write("group         POLYMER            type 1 2\n")
    file.write("group         TAIL               type 2\n")
    file.write("group         COUNTERION         type 3\n")
    file.write("\n")

    # ---- print thermodynamic data ----
    file.write("# ---- print thermodynamic data ----\n")
    file.write("thermo_style  custom             step temp pe ke ebond etotal press vol density\n")
    file.write("thermo        ${print_thermo}\n")
    file.write("\n")

    # ---- pairwise interactions ----
    file.write("# ---- pairwise interactions ----\n")
    file.write("# multiple styles of superposed pairwise interactions: hybrid/overlay\n")
    file.write("# Lennard-Jones for variable size particles: lj/expand\n")
    file.write("# long-range Coulomb potential: coul/long\n")
    file.write("pair_style    hybrid/overlay    lj/expand 10.0 coul/long ${cut}\n")
    file.write("\n")
    file.write("# modify the parameters of the currently defined pair style\n")
    file.write("# Lennard-Jones potential is shifted at its cutoff to 0.0: shift yes\n")
    file.write("# adds an energy term to each pairwise interaction which will be included in the thermodynamic\n "
               "# output, but does not affect pair forces or atom trajectories\n")
    file.write("pair_modify   pair              lj/expand shift yes\n")
    file.write("\n")
    file.write("# set the formula(s) to compute bond interactions between pairs of atoms\n")
    file.write("# FENE (finite-extensible non-linear elastic) bond\n")
    file.write("bond_style fene/expand\n")
    file.write("\n")
    file.write("# the coefficients associated with a bond style\n")
    file.write("bond_coeff	  1 30.0 1.5 1.0 1.0 ${delta_NPm}\n")
    file.write("\n")
    file.write("# set weighting coefficients for pairwise energy and force contributions between pairs of atoms "
               "that are also permanently bonded to each other\n")
    file.write("# sets the 3 coefficients to 0.0, 1.0, 1.0 for both LJ and Coulombic interactions, which is "
               "# consistent with a coarse-grained polymer model with FENE bonds\n")
    file.write("special_bonds fene\n")
    file.write("\n")
    file.write("# build neighbor lists: 1.0 bin for units = lj, skin = 1.0 sigma (1.0 is a skin distance)\n")
    file.write("neighbor       1.0 bin # 0.3 multi\n")
    file.write("\n")
    file.write("# how often lists are built as a simulation runs\n")
    file.write("# build lists every 1 step (after the delay has passed): every\n")
    file.write("# never build new lists until at least N steps after the previous build: delay\n")
    file.write("# the every and delay settings determine when a build may possibly be performed: check yes\n")
    file.write("# but an actual build only occurs if some atom has moved more than half the skin distance since "
               "# the last build\n")
    file.write("neigh_modify   every 1 delay 0 check yes\n")
    file.write("\n")

    file.write("# the pairwise force field coefficients for one or more pairs of atom types\n")
    file.write("pair_coeff   1 1 coul/long\n")
    file.write("pair_coeff   1 3 coul/long\n")
    file.write("pair_coeff   3 3 coul/long\n")
    file.write("\n")
    file.write("# dielectric constant for Coulombic interactions (pairwise and long-range)\n")
    file.write("dielectric   8.0\n")
    file.write("\n")
    file.write("# define a long-range solver for LAMMPS to use each timestep to compute long-range interactions\n")
    file.write("# particle-particle particle-mesh solver (Hockney) which maps atom charge to a 3d mesh: pppm\n")
    file.write("kspace_style pppm 1.0e-4\n")
    file.write("\n")
    file.write("# HEAD - HEAD interactions\n")
    file.write("pair_coeff   1 1 lj/expand ${epsP} 1.0 ${delta_NPNP} ${cutoffL}\n")
    file.write("# HEAD - TAIL interactions\n")
    file.write("pair_coeff   1 2 lj/expand ${epsP} 1.0 ${delta_NPm}  ${cutoffS}\n")
    file.write("# HEAD - COUNTER interactions\n")
    file.write("pair_coeff   1 3 lj/expand ${epsP} 1.0 ${delta_NPm}  ${cutoffS}\n")
    file.write("\n")
    file.write("# TAIL - TAIL interactions\n")
    file.write("pair_coeff   2 2 lj/expand ${epsP} 1.0 0             ${cutoffL}\n")
    file.write("# TAIL - COUNTER interactions\n")
    file.write("pair_coeff   2 3 lj/expand ${epsP} 1.0 0             ${cutoffS}\n")
    file.write("\n")
    file.write("# COUNTER - COUNTER interactions\n")
    file.write("pair_coeff   3 3 lj/expand ${epsP} 1.0 0             ${cutoffS}\n")
    file.write("\n")

    # ---- set timestep ----
    file.write("# ---- set timestep ----\n")
    file.write(f"timestep     {vars.TIMESTEP}\n")
    file.write("\n")

    # ---- replicate the current simulation ----
    file.write("# ---- replicate the current simulation one or more times in each dimension ----\n")
    file.write(f"replicate    {vars.REPLICA_X} {vars.REPLICA_Y} {vars.REPLICA_Z}\n")
    file.write("\n")

    # ---- run the simulation - increase system density----
    file.write("# ---- run the simulation - increase system density ----\n")
    file.write("# set constant volume, temperature and molecules number\n")
    file.write("fix          2 all nvt temp ${Th} ${Th} 0.1\n")
    file.write("# change the simulation box size/shape - increase density\n")
    file.write("fix          4 all deform 1 x final 0 ${bx} y final 0 ${by} z final 0 ${bz} units box\n")
    file.write("run          ${sim_time}\n")
    file.write("\n")

    # ---- run the simulation to establish the system ----
    file.write("# ---- run the simulation - establish system density ----\n")
    file.write("# turn off changing the simulation box size\n")
    file.write("unfix        4\n")
    file.write("# run the simulation to establish the system with increased density\n")

    # ---- create dump ----
    file.write(f"dump         1 all custom {vars.DUMP_STEP} constant_temp_high_1.dat id mol type x y z\n")
    file.write("dump_modify  1  sort id\n")

    file.write("run          ${sim_time}\n")
    file.write("\n")

    # ---- run the simulation - decrease temperature ----
    file.write("# ---- run the simulation - decrease temperature----\n")
    file.write("# change fix to different temperature: from high to low\n")
    file.write("undump       1\n")
    file.write("unfix        2\n")
    file.write("fix          2 all nvt temp ${Th} ${T} 0.1\n")

    # ---- create dump ----
    file.write(f"dump         2 all custom {vars.DUMP_STEP} temp_high_temp_low_2.dat id mol type x y z\n")
    file.write("dump_modify  2  sort id\n")

    file.write("run          ${sim_time}\n")
    file.write("\n")

    # ---- run the simulation - constant low temperature ----
    file.write("# ---- run the simulation - constant low temperature----\n")
    file.write("# change fix to constant temperature: low\n")
    file.write("undump       2\n")
    file.write("unfix        2\n")
    file.write("fix          2 all nvt temp ${T} ${T} 0.1\n")

    file.write(f"dump         3 all custom {vars.DUMP_STEP} constant_temp_low_3.dat id mol type x y z\n")
    file.write("dump_modify  3  sort id\n")

    file.write("run          ${sim_time}\n")
    file.write("\n")
