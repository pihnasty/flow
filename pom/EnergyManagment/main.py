
import sys

# universal .csv
from InitData.inizialize_data import experiments
import Flow as fw


experiment = experiments["0001"]

tau_d = experiment["tau_d"]
tau_number = experiment["tau_number"]
delta_tau_d = tau_d / tau_number

tau=[0.0] * tau_number

flow = fw.Flows(experiment)


u1_assumes = flow.get_mode_u1()
u2_assumes = flow.get_mode_u2()
u3_assumes = flow.get_mode_u3()



i = 0

n1_position = 'middle'
n2_position = 'middle'

for item in tau:
    tau[i] = i * delta_tau_d

    hamilton_value_max = - sys.float_info.max
    u1_assume_optimum = -1.0
    u2_assume_optimum = -1.0
    u3_assume_optimum = -1.0
    flow.set_tau(tau[i])
    flow.set_G(tau[i])
    flow.set_mass(tau[i])
    flow.set_psi3(tau[i])

    flow.set_n1(tau[i])
    flow.set_n2(tau[i])
    flow.set_z(tau[i])

    for u3_assume in u3_assumes:
        for u2_assume in u2_assumes:
            for u1_assume in u1_assumes:
                if flow.get_n1(tau[i]) < flow.get_n1_min():
                    n1_position = 'bottom'
                if flow.get_n1(tau[i]) > flow.get_n1_max():
                    n1_position = 'top'
                if flow.get_n2(tau[i]) < flow.get_n2_min():
                    n2_position = 'bottom'
                if flow.get_n2(tau[i]) > flow.get_n2_max():
                    n2_position = 'top'

                if(flow.gamma0(tau[i]) <= u1_assume) and  u1_assume != min(u1_assumes) and n1_position == 'bottom':
                    continue
                if(flow.gamma0(tau[i]) >= u1_assume) and  u1_assume != max(u1_assumes) and n1_position == 'top':
                    continue

                if(flow.tetta_output_1(tau[i-1]) <= u2_assume) and  u2_assume != min(u2_assumes) and n2_position == 'bottom':
                    continue
                if(flow.tetta_output_1(tau[i-1]) >= u2_assume) and  u2_assume != max(u2_assumes) and n2_position == 'top':
                    continue

                if u1_assume - u3_assume > 0:
                    continue




                hamilton_value = flow.Hamiltonian(tau[i], u1_assume, u2_assume, u3_assume)
                if hamilton_value > hamilton_value_max:
                    hamilton_value_max = hamilton_value
                    u1_assume_optimum = u1_assume
                    u2_assume_optimum = u2_assume
                    u3_assume_optimum = u3_assume

    flow.set_u1(tau[i], u1_assume_optimum)
    flow.set_u2(tau[i], u2_assume_optimum)
    flow.set_u3(tau[i], u3_assume_optimum)

    flow.set_criterium_with_z(tau[i])
    flow.set_criterium_without_z(tau[i])

    i += 1

print('R', flow.get_criterium_r())

flow.show_1()
flow.show_2()
flow.show_3()

sys.exit()
