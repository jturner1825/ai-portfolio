# 📘 OOP Basics – Python Practice  

This folder contains my practice exercises for learning **Object-Oriented Programming (OOP) in Python**. Each example demonstrates a different core OOP principle, with simple, real-world–style classes.  

---

## 🔑 Covered Concepts  

1. **Encapsulation** – *BankAccount*  
   - Shows how to hide internal data (`_balance`) and use methods or `@property` to safely manage state.  

2. **Inheritance** – *Person → Student / Faculty*  
   - Demonstrates how child classes reuse parent attributes and add their own (e.g., `student_id`, `GPA`).  

3. **Polymorphism** – *Animal → Dog / Cat*  
   - Each subclass implements its own version of `speak()`, but you can treat them all as `Animal`.  

4. **Composition** – *Playlist & Song* **(WIP)**  
   - Models a “has-a” relationship. A playlist *has* songs, and can calculate total duration.  

5. **Special (Dunder) Methods** – **(WIP)**  
   - Examples like `__str__` for nice printing, `__len__` for counting courses, and `__eq__` for comparing students.  

6. **Static & Class Methods** – *Person utility methods* **(WIP)**  
   - Shows how to add methods that belong to the class itself (`is_adult`, `from_birth_year`).  

7. **(Optional) Abstract Classes** – *Shape → Circle / Rectangle* **(WIP)**  
   - Blueprint for forcing subclasses to implement methods like `area()` and `perimeter()`.  

---

## 🚀 How to Use
- Open the Jupyter notebook (`oop_basics.ipynb`) to view interactive examples with explanations.  
- Or run the Python scripts (`.py` files) directly if you prefer a clean code version.  

---

## 📝 Notes
- These examples are not production-level apps; they’re **practice exercises** to build intuition with OOP.  
- The focus is on **clarity and demonstrating concepts**, not efficiency.  
