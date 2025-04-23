import pandapower as pp
import pandapower.networks as pn
import pandapower.plotting as plot
import matplotlib.pyplot as plt

# Ustvari primer omrežja
net = pn.simple_mv_open_ring_net()

# Dodaj obremenitev (load)
pp.create_load(net, bus=5, p_mw=0.2, q_mvar=0.05)

# Izvedi power flow
pp.runpp(net)

# Izpiši rezultate
print(net.res_bus)
print(net.res_line)

# Izriši rezultate
plot.simple_plot(net, show_plot=True)