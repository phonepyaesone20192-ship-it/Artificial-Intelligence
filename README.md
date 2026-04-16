# Artificial-Intelligence
A Python-based program that solves a maze using the Breadth-First Search (BFS) algorithm to find the shortest path from the start (top-left) to the goal (bottom-right).
# 🧩 Maze Solver (BFS Algorithm)

This project is a Python program that solves a maze using the **Breadth-First Search (BFS)** algorithm.
It finds the **shortest path** from the start position (top-left corner) to the goal (bottom-right corner).

---

## 🚀 Features

* ✅ Reads maze from a text file
* 🔄 Converts maze into a graph using an adjacency matrix
* 🔍 Uses BFS to find the shortest path
* 📍 Displays path and distance
* 🧱 Visual maze output with symbols

---

## 🧠 How It Works

### 1. Read Maze

The maze is loaded from a text file where:

* `0` = open path
* `1` = wall

Handled in: 

---

### 2. Convert to Graph

* Each open cell becomes a **node**
* Connections are created between adjacent cells (up, down, left, right)
* Stored in an **adjacency matrix**

---

### 3. BFS Algorithm

* Uses a queue (FIFO)
* Explores nodes level-by-level
* Guarantees shortest path

---

### 4. Output

* Displays:

  * Shortest distance
  * Path coordinates
  * Visual maze

Example symbols:

```id="ex1"
S = Start
E = End
# = Wall
. = Path
```

---

## 📁 Project Structure

```id="ex2"
project/
│── AI.py
│── maze.txt
```

---

## 📄 Example Maze

File: 

```id="ex3"
0 0 0 0 1 1 1 1 0
1 0 1 0 0 0 0 0 0
...
```

---

## ▶️ How to Run

### 1. Make sure Python is installed

### 2. Run the program

```bash id="ex4"
python AI.py
```

---

## ⚙️ Requirements

* Python 3.x
* No external libraries required

---

## ⚠️ Important Notes

* Maze must:

  * Not be empty
  * Have equal row lengths
  * Start and end must be `0`

* Start = `(0,0)`

* End = `(last row, last column)`

---

## 📊 Example Output

```id="ex5"
Shortest distance: 14
Path: [(0,0), (0,1), ... , (7,8)]
```

---

## 🛠️ Concepts Used

* Breadth-First Search (BFS)
* Graph representation (Adjacency Matrix)
* Queue (Deque)
* Path reconstruction

---

## 👤 Author

Phone Pyae Sone
Computer Science Student 

---

## 📄 License

This project is for educational purposes.
