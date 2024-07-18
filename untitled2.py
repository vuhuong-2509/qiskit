import math
from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

# Tạo một mạch lượng tử với 2 qubit
qc = QuantumCircuit(2)

# Thay thế giá trị này bằng giá trị thực của mu' * Delta
mu_prime_delta = 1.0

# Thay thế giá trị này bằng giá trị thực của a
a = math.pi  # Pi

#cổng S
qc.sdg(0)

#cổng S
qc.sdg(1)

#cổng H
qc.h(0)

#cổng H
qc.h(1)


#cổng CNOT 
qc.cx(0,1)

#côngRz
qc.rz(mu_prime_delta,1)

#cổng CNOT
qc.cx(0,1)

#cổng H
qc.h(0)

#cổng H
qc.h(1)

#cổng S
qc.s(0)

#cổng S
qc.s(1)

# Vẽ mạch
qc.draw('mpl')
plt.show()
