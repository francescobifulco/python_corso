Perfetto!
Ecco un **tutorial completo, dettagliato e suddiviso in lezioni** sulla libreria **`time`** di Python, aggiornato e con *tutti i concetti fondamentali + quelli avanzati e meno conosciuti*.
Puoi chiedere anche esercizi, PDF, infografiche, esempi avanzati o tabelle riassuntive.

---

# ⏰ **TUTORIAL COMPLETO SU `time` – Python**

## **Indice delle Lezioni**

1. Introduzione alla libreria `time`
2. Il concetto di timestamp e funzioni base (`time()`, `ctime()`, `asctime()`)
3. Lavorare con gli oggetti `struct_time`
4. Convertire tempo: `localtime()`, `gmtime()`, `mktime()`
5. Formattare e parsare date: `strftime()` e `strptime()`
6. Misurare la durata di operazioni: `sleep()`, `perf_counter()`, `process_time()`
7. Timer ad alta precisione e benchmark
8. Funzioni avanzate: `monotonic()`, `monotonic_ns()`, `time_ns()`, `perf_counter_ns()`
9. Timezone e UTC (concetti base)
10. Mini-progetto finale: Timer CLI professionale

---

# 📚 **LEZIONE 1 — Introduzione alla libreria `time`**

### 🔍 Cos’è la libreria `time`?

`time` è un modulo integrato di Python che permette di:

* gestire tempi e date in stile Unix
* mettere in pausa lo script
* misurare esecuzioni con alta precisione
* convertire valori temporali
* formattare date e orari

### ➕ Importazione

```python
import time
```

---

# 📚 **LEZIONE 2 — Timestamp e funzioni base**

## 🕒 Che cos’è un timestamp?

È un numero **float** che rappresenta i secondi passati dal **1 gennaio 1970 (Epoch)**.

### ✔ Ottenere il timestamp attuale

```python
import time
print(time.time())
```

### ✔ Convertire un timestamp in una stringa leggibile

```python
print(time.ctime(time.time()))
```

### ✔ Convertire un `struct_time` in stringa

```python
t = time.localtime()
print(time.asctime(t))
```

---

# 📚 **LEZIONE 3 — Lavorare con `struct_time`**

`struct_time` è una struttura che rappresenta data/ora dettagliata.

### ✔ Ottenere l'ora attuale come `struct_time`

```python
t = time.localtime()
print(t)
```

Output tipico:

```
time.struct_time(tm_year=2025, tm_mon=2, tm_mday=7,
                 tm_hour=14, tm_min=30, tm_sec=10,
                 tm_wday=4, tm_yday=38, tm_isdst=1)
```

### ✔ Accedere ai campi

```python
print(t.tm_year)
print(t.tm_hour)
print(t.tm_yday)
```

---

# 📚 **LEZIONE 4 — Conversioni**

### ✔ `localtime()` – timestamp → ora locale

```python
time.localtime(1707300000)
```

### ✔ `gmtime()` – timestamp → tempo in UTC

```python
time.gmtime()
```

### ✔ `mktime()` – struct_time → timestamp

```python
ts = time.mktime(time.localtime())
```

---

# 📚 **LEZIONE 5 — Formattare e parsare date**

## 🎨 `strftime()`: formattazione

```python
print(time.strftime("%Y-%m-%d %H:%M:%S"))
```

### Formati comuni:

* `%Y` — anno
* `%m` — mese
* `%d` — giorno
* `%H` — ora
* `%M` — minuti
* `%S` — secondi
* `%A` — giorno della settimana
* `%B` — nome del mese

## 🔍 `strptime()`: parsing stringa → struct_time

```python
data = "2025-02-07 14:00"
t = time.strptime(data, "%Y-%m-%d %H:%M")
print(t)
```

---

# 📚 **LEZIONE 6 — Pausa e misurazione base**

### ⏸ Mettere in pausa lo script

```python
time.sleep(2.5)  # pausa di 2.5 secondi
```

### ⏱ `perf_counter()` e `process_time()`

* `perf_counter()` → misura il tempo reale (alta precisione)
* `process_time()` → misura solo CPU time

```python
start = time.perf_counter()
# ... operazioni
end = time.perf_counter()
print("Tempo:", end - start)
```

---

# 📚 **LEZIONE 7 — Benchmark professionali**

Usare `time.perf_counter()` è fondamentale per misurazioni precise.

### ✔ Esempio di benchmark

```python
import time

def test():
    sum(range(10_000_000))

start = time.perf_counter()
test()
print("Durata:", time.perf_counter() - start)
```

---

# 📚 **LEZIONE 8 — Funzioni avanzate**

### 🟦 `time.time_ns()`

Timestamp in **nanosecondi**

```python
print(time.time_ns())
```

### 🟪 `time.monotonic()`

Tempo **solo crescente** (non può andare indietro)

```python
print(time.monotonic())
```

### 🟩 Versione in ns

```python
time.monotonic_ns()
```

### 🟥 `perf_counter_ns()`

Massima precisione

```python
time.perf_counter_ns()
```

### 📌 Perché servono?

* cronometri ad alta precisione
* profiling
* evitare errori quando l’orologio di sistema cambia

---

# 📚 **LEZIONE 9 — Timezone (concetti base)**

> Nota: la gestione avanzata dei fusi orari si fa con **`datetime`** o **pytz**, non con `time`.
> Ma `time` permette conoscenze base.

### ✔ Offset del fuso orario locale

```python
print(time.timezone)         # in secondi
print(time.altzone)          # DST
print(time.daylight)         # 0 o 1
```

---

# 📚 **LEZIONE 10 — Mini-progetto finale: Timer CLI professionale**

### 🎯 Obiettivo

Creare un timer da terminale con:

* pausa regolabile
* timer ad alta precisione
* formattazione tempo

### ✔ Codice

```python
import time
import sys

def format_time(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

if len(sys.argv) != 2:
    print("Uso: python timer.py <secondi>")
    sys.exit(1)

durata = int(sys.argv[1])

start = time.perf_counter()

while True:
    elapsed = time.perf_counter() - start
    remaining = durata - elapsed

    if remaining <= 0:
        print("\rFINE!", end="")
        break

    print(f"\rTempo restante: {format_time(int(remaining))}", end="")
    time.sleep(0.2)
```

Esecuzione:

```
python timer.py 10
```

---

# 🎉 Tutorial completato!

## Vuoi anche:

* la versione **PDF**?
* **esercizi** per ogni lezione?
* una **tabella riassuntiva** di tutte le funzioni?
* un tutorial sulla libreria **`datetime`** (complementare a `time`)?

