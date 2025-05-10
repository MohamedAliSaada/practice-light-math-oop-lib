# practice-light-math-oop-lib

**A lightweight educational Python library to practice OOP through math, geometry, and tensor logic.**

This library is designed to help Python learners, students, and educators understand the principles of object-oriented programming (OOP) by building core math concepts, geometric logic, and multi-dimensional tensors from scratch.

---

## ✨ Features

### 🔢 Core Math (`core_math.py`)
- `Number`: a safe wrapper for `int`/`float` with encapsulation
- `Fraction`: basic arithmetic and simplification using `Number`
- `Vector2D`: 2D vector class with `add`, `sub`, `dot`, and `magnitude` operations

### 📐 Geometry 2D (`geometry2d.py`)
- `Point`: represents a 2D point using `Number`
- `Line`: defined by two `Point`s, with slope, length, and midpoint calculations

### 🧱 Advanced 2D Shapes (`advancedgeometry2d.py`)
- `Shape`: abstract base class for geometric shapes
- `Rectangle`, `Triangle`, `Circle`, `Polygon`: concrete 2D shapes with area & perimeter calculations

### 🧮 Tensors & 3D Vectors (`geometry3d.py`)
- `Vector3D`: a simple 3D vector class
- `Tensor`: supports 1D, 2D, 3D tensors with:
  - `.ones()` and `.zeros()` methods
  - element-wise `+`, `-`, `*`
  - automatic shape detection and jagged list validation

---

## 📦 Installation

### Install Locally

1. Clone the repository:

```bash
git clone https://github.com/yourusername/practice-light-math-oop-lib.git
cd practice-light-math-oop-lib
