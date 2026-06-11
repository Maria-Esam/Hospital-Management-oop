# Hospital Management System - OOP in Python 🏥

## About The Project
This is a console-based Hospital Management System built using Python. The primary goal of this project is to demonstrate a solid understanding and practical application of Object-Oriented Programming (OOP) concepts. 

The system simulates the basic operations of a hospital, managing interactions between Doctors, Patients, and Staff.

## Key Features
* **Patient Management:** Track patient details, medical history, prescriptions, and appointments.
* **Doctor Management:** Differentiate between General Doctors and Specialists, assign patients, make diagnoses, and prescribe medicine.
* **Staff Operations:** Schedule and cancel appointments for patients.
* **Hospital Overview:** Display a comprehensive list of all registered doctors, patients, and staff.

## OOP Concepts Demonstrated
This project heavily relies on core OOP principles to keep the code modular, scalable, and clean:

1. **Inheritance:** * `Patient`, `Doctor`, and `Staff` classes inherit from a base `Person` class to reuse common attributes (Name, ID, Contact Info).
   * `GeneralDoctor` and `SpecialistDoctor` inherit from the base `Doctor` class.
2. **Encapsulation:** * Sensitive data like a patient's `__medical_history`, `__prescriptions`, and `__appointments` are made private using double underscores to prevent direct external modification. Access is provided via getter and setter methods.
3. **Polymorphism (Method Overriding):**
   * The `diagnose` method is overridden in both `GeneralDoctor` and `SpecialistDoctor` classes to provide specific diagnostic outputs based on the doctor's specialty.
4. **Composition/Aggregation:**
   * The `Hospital` class aggregates multiple `Doctor`, `Patient`, and `Staff` objects.

## How to Run
1. Ensure you have Python installed on your system.
2. Clone this repository:
   ```bash
   git clone https://github.com/Maria-Esam/Hospital-Management-oop.git
