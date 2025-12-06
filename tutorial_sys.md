Ecco un **tutorial completo e dettagliato sulla libreria `sys` di Python**, organizzato in **lezioni**, con spiegazioni, esempi pratici e casi d’uso reali.
Puoi chiedere in seguito esercizi, approfondimenti o una versione PDF/markdown.

---

# 📘 **TUTORIAL COMPLETO SU `sys` – Python**

## **Indice delle Lezioni**

1. **Introduzione alla libreria `sys`**
2. **`sys.argv`: leggere argomenti da riga di comando**
3. **`sys.exit`: terminare l’esecuzione**
4. **`sys.stdin`, `sys.stdout`, `sys.stderr`: input/output basso livello**
5. **Informazioni sull’interprete: `sys.version`, `sys.executable`, `sys.platform`**
6. **Gestione del modulo: `sys.modules`, `sys.path`**
7. **Gestione memoria e limiti: `sys.getsizeof`, `sys.getrecursionlimit`, `sys.setrecursionlimit`**
8. **Funzioni avanzate: `sys.getrefcount`, `sys.flags`, `sys.implementation`, `sys.thread_info`**
9. **Ricostruzione completa: creare strumenti da linea di comando con `sys`**

---

# 📚 **LEZIONE 1 — Introduzione alla libreria `sys`**

### 🔍 Cos’è la libreria `sys`?

`sys` è un modulo integrato (built-in) in Python che permette di:

* interagire con l’interprete Python
* leggere argomenti da riga di comando
* accedere a stream di input/output
* modificare il path dei moduli
* controllare la ricorsione
* ottenere informazioni di runtime

### ➕ Come importarla

```python
import sys
```

### 🎯 Quando si usa?

* scrittura di script da terminale
* debug
* gestione output
* strumenti CLI
* introspezione del sistema

---

# 📚 **LEZIONE 2 — `sys.argv`: Argomenti da riga di comando**

### 📌 Cosa sono?

`sys.argv` è una lista delle stringhe passate allo script Python da terminale.

### ✔ Esempio

script: `script.py`

```python
import sys

print("Tutti gli argomenti:", sys.argv)
print("Nome script:", sys.argv[0])
if len(sys.argv) > 1:
    print("Primo argomento:", sys.argv[1])
```

Esecuzione:

```
python script.py ciao 123
```

Risultato:

```
Tutti gli argomenti: ['script.py', 'ciao', '123']
Nome script: script.py
Primo argomento: ciao
```

### 🧰 Caso reale: mini-calcolatrice CLI

```python
# calc.py
import sys

if len(sys.argv) != 4:
    print("Uso: python calc.py <num1> <op> <num2>")
    sys.exit(1)

n1 = float(sys.argv[1])
op = sys.argv[2]
n2 = float(sys.argv[3])

if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
else:
    print("Operatore non supportato")
```

---

# 📚 **LEZIONE 3 — `sys.exit`: terminare lo script**

### ✔ Come funziona

```python
sys.exit()          # termina con successo (codice 0)
sys.exit(1)         # termina con errore generico
sys.exit("Errore!") # stampa il messaggio e termina con codice 1
```

### ✔ Quando usarlo

* validazione input
* interruzione su errori
* terminare un programma CLI

---

# 📚 **LEZIONE 4 — Input/Output: `sys.stdin`, `sys.stdout`, `sys.stderr`**

### 📌 Differenza rispetto a `input()` e `print()`

* **`stdin`** gestisce input in modo più raw (lettura anche da pipe)
* **`stdout`** è l’output standard
* **`stderr`** è l’output per errori (non va in pipe)

### ✔ Esempio con pipe:

```python
import sys

data = sys.stdin.read()
print("Ho letto:", data)
```

Da terminale:

```
echo "testo pipato" | python script.py
```

### ✔ Scrivere su stderr

```python
sys.stderr.write("Attenzione! Errore.\n")
```

---

# 📚 **LEZIONE 5 — Informazioni sull’interprete**

### ✔ Versione Python

```python
print(sys.version)
print(sys.version_info)
```

### ✔ Dove si trova Python

```python
print(sys.executable)
```

### ✔ Sistema operativo

```python
print(sys.platform)
```

---

# 📚 **LEZIONE 6 — Moduli e percorso: `sys.path`, `sys.modules`**

### ✔ `sys.path`: dove Python cerca i moduli

```python
import sys
print(sys.path)
```

Aggiungere una directory:

```python
sys.path.append("/my/custom/modules")
```

### ✔ `sys.modules`: moduli già importati

```python
print(sys.modules.keys())
```

---

# 📚 **LEZIONE 7 — Memoria e limiti**

### ✔ `sys.getsizeof(obj)`

Restituisce la memoria occupata da un oggetto.

```python
import sys
print(sys.getsizeof("ciao"))
```

### ✔ Limite di ricorsione

```python
print(sys.getrecursionlimit())
sys.setrecursionlimit(3000)
```

⚠ Attenzione: aumentare troppo può causare crash.

---

# 📚 **LEZIONE 8 — Funzioni avanzate**

### ✔ Riferimenti all’oggetto

```python
import sys
a = []
print(sys.getrefcount(a))
```

### ✔ Flag dell'interprete

```python
print(sys.flags)
```

### ✔ Info implementazione (CPython, PyPy…)

```python
print(sys.implementation)
```

### ✔ Info thread

```python
print(sys.thread_info)
```

---

# 📚 **LEZIONE 9 — Mini-progetto finale**

Costruiamo un **programma da linea di comando completo**.

### 🧰 Obiettivo

Creare uno script che:

* legga argomenti
* supporti flags
* usi stdin/stdout
* gestisca errori con stderr

### ✔ Programma: `text_tool.py`

```python
import sys

def usage():
    sys.stderr.write("Uso: text_tool.py [-u|-l] [file]\n")
    sys.exit(1)

args = sys.argv[1:]

if not args:
    usage()

mode = args[0]
if mode not in ("-u", "-l"):
    usage()

# Se c’è un file, lo leggiamo. Altrimenti leggiamo da stdin.
if len(args) > 1:
    try:
        text = open(args[1]).read()
    except:
        sys.stderr.write("Errore: impossibile aprire il file\n")
        sys.exit(1)
else:
    text = sys.stdin.read()

if mode == "-u":
    sys.stdout.write(text.upper())
else:
    sys.stdout.write(text.lower())
```

### ✔ Uso

```
python text_tool.py -u testo.txt
cat testo.txt | python text_tool.py -l
```

---

# ✅ Vuoi aggiungere esercizi, esempi pratici, diagrammi o un PDF?

Posso anche creare una **versione più avanzata**, un **riassunto**, o una **versione per principianti**.
