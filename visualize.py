import matplotlib.pyplot as plt


def plot_customers(customer_ids, values, title="Analiza klientów"):
    """Tworzy wykres wartości dla klientów."""
    plt.figure(figsize=(8, 5))
    plt.bar(customer_ids, values)
    plt.title(title)
    plt.xlabel("Klient")
    plt.ylabel("Wartość")
    plt.tight_layout()
    plt.show()
