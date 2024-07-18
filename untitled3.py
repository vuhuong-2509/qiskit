from qiskit import QuantumCircuit, Aer, execute
import matplotlib.pyplot as plt

# Tạo một mạch lượng tử với 1 qubit
qc = QuantumCircuit(1, 1)

# Áp dụng cổng S vào qubit 0
qc.s(0)

# Áp dụng cổng S+ (S cộng ngược, hay Sdg) vào qubit 0
qc.sdg(0)

# Thêm cổng đo lường
qc.measure(0, 0)

# Vẽ mạch
qc.draw('mpl')
plt.show()

# Sử dụng statevector simulator để mô phỏng mạch
backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
statevector = result.get_statevector()

print("Statevector:", statevector)

# Sử dụng qasm simulator để đếm số lần đo lường
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts()

print("Counts:", counts)

# Vẽ histogram của kết quả đo lường
from qiskit.visualization import plot_histogram
plot_histogram(counts)
plt.show()
