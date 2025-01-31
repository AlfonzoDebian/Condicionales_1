# Input
c_minutos = int(input("Inserte la cantidad de minutos: "))

# if, else
if c_minutos <= 3:
    v_llamada = 300
else:
    v_llamada = 300 + 50 * (c_minutos - 3)

# Final
print(f"Debe pagar: {v_llamada} COP")
