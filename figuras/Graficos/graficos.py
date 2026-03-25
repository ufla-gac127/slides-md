import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# 1. Gerar dados assimétricos
# -----------------------------
np.random.seed(0)
data = np.random.exponential(scale=50, size=1000)

# -----------------------------
# 2. Aplicar transformação log
# log1p = log(1 + x) (evita problema com zero)
# -----------------------------
log_data = np.log1p(data)

# -----------------------------
# 3. Plotar distribuição original
# -----------------------------
plt.figure()
plt.hist(data, bins=30)
plt.title("Distribuição original (assimétrica)")
plt.xlabel("Valores")
plt.ylabel("Frequência")
plt.show()

# -----------------------------
# 4. Plotar distribuição transformada
# -----------------------------
plt.figure()
plt.hist(log_data, bins=30)
plt.title("Distribuição após transformação log")
plt.xlabel("Valores transformados")
plt.ylabel("Frequência")
plt.show()