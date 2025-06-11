import matplotlib.pyplot as plt

def continuous_plotter(
    ind_var, dep_var,
    title: str = "", graph_label: str = "",
    x_label: str = "", y_label: str = ""
):
    plt.plot(ind_var, dep_var, label=graph_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def discrete_plotter(
    ind_var, dep_var,
    title: str = "", graph_label: str = "",
    x_label: str = "", y_label: str = ""
):
    plt.stem(ind_var, dep_var, linefmt='b-', markerfmt='bo', basefmt=' ', label=graph_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def double_plotter(
    t, ref_signal, new_signal,
    title: str = "", ref_label: str = "Referencia", new_label: str = "Modificada",
    x_label: str = "Tiempo (s)", y_label: str = "Amplitud"
):
    plt.plot(t, ref_signal, 'r--', label=ref_label)
    plt.plot(t, new_signal, 'b-', label=new_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def double_discrete_plotter(
    ind_var, ref_signal, mod_signal,
    title: str = "", ref_label: str = "Referencia", mod_label: str = "Modificada",
    x_label: str = "Tiempo (s)", y_label: str = "Amplitud"
):
    plt.stem(ind_var, ref_signal, linefmt='r-', markerfmt='ro', basefmt=" ", label=ref_label)
    plt.stem(ind_var, mod_signal, linefmt='b-', markerfmt='bo', basefmt=" ", label=mod_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def dac_plotter(entradas_digitales, salida_analogica, bits):
    plt.figure(figsize=(8, 5))
    plt.step(entradas_digitales, salida_analogica, where='post', color='b', linewidth=2, label='Salida DAC')
    plt.scatter(entradas_digitales, salida_analogica, color='r')
    plt.title(f'Salida Analógica del DAC ({bits} bits)')
    plt.xlabel('Entrada Digital')
    plt.ylabel('Voltaje de Salida (V)')
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()
