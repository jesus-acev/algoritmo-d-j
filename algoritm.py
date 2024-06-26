import numpy as np

def hadamard_gate(n):
    """Crea una matriz de Hadamard para n qubits."""
    H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
    H_n = H
    for _ in range(n - 1):
        H_n = np.kron(H_n, H)
    return H_n

def oracle(n, is_constant):
    """Crea una matriz de Oracle para una función constante o balanceada."""
    I = np.eye(2**n)
    if is_constant:
        return I  # Oracle para una función constante no cambia nada
    else:
        # Para una función balanceada, aplicar X a los últimos qubits
        for i in range(2**(n - 1), 2**n):
            I[i, i] = -1
        return I

def deutsch_jozsa(n, is_constant):
    """Implementa el algoritmo de Deutsch-Jozsa."""
    # Inicializar el estado en |0...01>
    state = np.zeros(2**(n + 1))
    state[-1] = 1

    # Aplicar Hadamard a todos los qubits
    H = hadamard_gate(n + 1)
    state = H @ state

    # Aplicar el Oracle
    U_f = oracle(n + 1, is_constant)
    state = U_f @ state

    # Aplicar Hadamard a los primeros n qubits de nuevo
    H_n = hadamard_gate(n)
    I_2 = np.eye(2)
    H_n_I = np.kron(H_n, I_2)
    state = H_n_I @ state

    # Medir los primeros n qubits
    measurement = np.abs(state[:2**n])**2
    return measurement


n = 3  # Número de qubits de entrada
is_constant = True  # Cambiar a False para una función balanceada

measurement = deutsch_jozsa(n, is_constant)
print(f"Resultado de la medición: {measurement}")
