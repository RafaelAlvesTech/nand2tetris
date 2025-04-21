import pennylane as qml
from pennylane import numpy as np

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def nand_circuit(a, b):
    # Prepara os qubits conforme os bits de entrada
    if a:
        qml.PauliX(wires=0)
    if b:
        qml.PauliX(wires=1)
    # AND clássico pode ser simulado com Toffoli, mas para NAND:
    # Usamos um truque: AND e depois NOT
    # Em dois qubits, NAND(a, b) = NOT(AND(a, b))
    # Para dois qubits, AND pode ser (a & b)
    # Mas em circuito quântico, AND é Toffoli (precisa de 3 qubits)
    # Aqui, simulamos NAND apenas para entradas clássicas:
    return int(not (a and b))
