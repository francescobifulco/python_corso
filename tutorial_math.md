Perfetto!
Ecco un **tutorial completo, dettagliato e organizzato in lezioni** sulla libreria **`math`** di Python, con spiegazioni, esempi pratici, casi reali e concetti avanzati.

Puoi chiedermi anche:

* esercizi per ogni lezione
* schede riassuntive
* una versione PDF/Markdown
* esempi scientifici/ingegneristici

---

# 🧮 **TUTORIAL COMPLETO SU `math` – Python**

## 📘 **Indice delle Lezioni**

1. Introduzione alla libreria `math`
2. Costanti matematiche (`pi`, `e`, `tau`, `inf`, `nan`)
3. Funzioni aritmetiche di base (`ceil`, `floor`, `trunc`, `copysign`)
4. Radicali, potenze e logaritmi: `sqrt`, `pow`, `log`, `log10`, `exp`
5. Funzioni trigonometriche: `sin`, `cos`, `tan`, `radians`, `degrees`
6. Funzioni iperboliche
7. Funzioni statistiche e combinatorie (`factorial`, `comb`, `perm`, `fsum`)
8. Numeri complessi e confronto tra `math` e `cmath`
9. Funzioni avanzate: `isfinite`, `isnan`, `isinf`, `frexp`, `ldexp`, `modf`
10. Mini-progetto finale: Calcolatrice scientifica CLI

---

# 📚 **LEZIONE 1 — Introduzione alla libreria `math`**

### 🔍 Cos’è la libreria `math`?

`math` è un modulo built-in che offre funzioni matematiche **veloci e precise**, scritte in C.

### ➕ Importazione

```python
import math
```

---

# 📚 **LEZIONE 2 — Costanti matematiche**

### ✔ Costanti principali

```python
import math

print(math.pi)   # 3.141592653589793
print(math.e)    # 2.718281828459045
print(math.tau)  # 6.283185307179586 (2π)
print(math.inf)  # infinito
print(math.nan)  # "not a number"
```

### 🧠 Quando serve?

* geometria (`pi`)
* probabilità/analisi (`e`)
* rappresentare overflow (`inf`)
* gestire risultati indeterminati (`nan`)

---

# 📚 **LEZIONE 3 — Funzioni aritmetiche di base**

### ✔ Arrotondamenti

```python
math.ceil(3.14)   # → 4
math.floor(3.14)  # → 3
math.trunc(3.99)  # → 3
```

### ✔ Copiare il segno

```python
math.copysign(3, -1)  # → -3.0
```

### ✔ Valore assoluto

```python
math.fabs(-3.5)  # → 3.5
```

---

# 📚 **LEZIONE 4 — Potenze, radici e logaritmi**

### 🟦 Radice quadrata

```python
math.sqrt(25)  # 5.0
```

### 🟧 Potenza matematica

```python
math.pow(2, 3)   # 8.0 (sempre float)
```

### 🟨 Logaritmi

```python
math.log(8, 2)      # log base 2 → 3.0
math.log10(1000)    # 3.0
math.log2(1024)     # 10.0
```

### 🟪 Esponenziale

```python
math.exp(1)   # ≈ 2.718281...
```

---

# 📚 **LEZIONE 5 — Funzioni trigonometriche**

### ✔ Trigonometria standard (in radianti)

```python
math.sin(math.pi/2)  # 1.0
math.cos(0)          # 1.0
math.tan(math.pi/4)  # 1.0
```

### ✔ Conversione gradi ↔ radianti

```python
math.radians(180)  # π
math.degrees(math.pi)  # 180
```

---

# 📚 **LEZIONE 6 — Funzioni iperboliche**

```python
math.sinh(1)
math.cosh(1)
math.tanh(1)
```

Utile in:

* modelli fisici
* funzioni di attivazione nel machine learning
* calcoli relativistici

---

# 📚 **LEZIONE 7 — Funzioni statistiche e combinatorie**

### ✔ Fattoriale

```python
math.factorial(5)  # 120
```

### ✔ Combinazioni e permutazioni

```python
math.comb(5, 2)  # 10
math.perm(5, 2)  # 20
```

### ✔ Somma precisa (evita errori floating point)

```python
math.fsum([0.1] * 10)  # 1.0
sum([0.1] * 10)        # 0.99999999999999
```

---

# 📚 **LEZIONE 8 — `math` vs `cmath`**

`math` lavora **solo con numeri reali**.
`cmath` gestisce numeri **complessi**.

### Esempio:

```python
import math, cmath

# math genera errore
# math.sqrt(-1)

cmath.sqrt(-1)   # → 1j
```

---

# 📚 **LEZIONE 9 — Funzioni avanzate**

### ✔ Controlli numerici

```python
math.isfinite(x)
math.isinf(x)
math.isnan(x)
```

### ✔ `modf`: separa parte intera e decimale

```python
math.modf(3.14)  # → (0.140000..., 3.0)
```

### ✔ `frexp`: rappresentazione mantissa/esponente

```python
math.frexp(8)  # → (0.5, 4)
```

### ✔ `ldexp`: inverso di frexp

```python
math.ldexp(0.5, 4)  # → 8.0
```

---

# 📚 **LEZIONE 10 — Mini-progetto finale: Calcolatrice scientifica CLI**

### 🎯 Obiettivo

Una calcolatrice che supporta:

* funzioni trigonometriche
* radici
* logaritmi
* fattoriale

### ✔ Codice

```python
import math
import sys

def calc(expr):
    try:
        return eval(expr, {"__builtins__": {}}, math.__dict__)
    except Exception as e:
        return f"Errore: {e}"

print("Calcolatrice scientifica (math). Digita 'exit' per uscire.")

while True:
    expr = input(">>> ")
    if expr == "exit":
        break
    print(calc(expr))
```

Esempio:

```
>>> sin(pi/2)
1.0
>>> log(100, 10)
2.0
>>> factorial(6)
720
```

---

# 🎉 Tutorial completato!

## Vuoi anche:

* esercizi con soluzioni?
* una versione più breve tipo “bigino”?
* una versione per principianti?
* aggiungere grafici (usando matplotlib) per visualizzare funzioni trigonometriche?
