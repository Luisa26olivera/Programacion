from cuenta import Cuenta
print()
cuenta1=Cuenta(12345,'26/01/2004',20000)
print(cuenta1.retirar())
print(cuenta1.consigna())
print('\ncuenta')
print(cuenta1.informacion())
from cuenta import cuentaCorriente
cuenta2=cuentaCorriente(5467,'02/02/2022',30000,889)
print()
print(cuenta2.retirar())
print(cuenta2.consigna())
print('\ncuenta corriente')
print(cuenta2.informacion())
print(cuenta2.Chequera())