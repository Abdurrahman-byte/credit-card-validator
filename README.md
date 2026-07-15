💳 Credit Card Validator

A Python command-line application that validates credit card numbers using the Luhn Algorithm.



📌 Overview

This project checks whether a credit card number is valid by applying the Luhn checksum algorithm.

The program removes spaces and hyphens from the input, processes the digits according to the algorithm, calculates a checksum value, and determines whether the card number is valid.

This type of validation is widely used by banks, payment processors, and online shopping platforms.



Features

* 💳 Credit card validation
* Luhn Algorithm implementation
* Removes spaces and hyphens automatically
* Fast checksum calculation
* Command-line interface
* Real-world algorithm practice



Technologies Used

* Python 3
* Tkinter
* Luhn Algorithm



How to Run

1. Clone the repository

```bash
git clone https://github.com/Abdurrahman-byte/credit-card-validator.git
```

2. Navigate to the project folder

```bash
cd credit-card-validator
```

3. Run the program

```bash
python main.py
```



Example Usage

Input

```text
Enter a credit card: 4539 1488 0343 6467
```

Output

```text
VALID
```

---

Input

```text
Enter a credit card: 1234 5678 9012 3456
```

Output

```text
INVALID
```

---

Project Structure

```text
credit-card-validator/
│
├── README.md
└── credit.py
```



How the Algorithm Works

The program follows these steps:

1. Clean Input

Removes:

* Spaces
* Hyphens

Example:

```text
4539-1488-0343-6467
```

becomes:

```text
4539148803436467
```



2. Reverse the Number

The digits are reversed so processing can begin from the rightmost digit.



3. Sum Odd-Position Digits

Every other digit is added directly to the total.



4. Process Even-Position Digits

Each digit is:

* Multiplied by 2
* If the result is greater than 9, its digits are summed

Example:

```text
8 × 2 = 16

1 + 6 = 7
```



5. Calculate Checksum

The odd and even sums are combined.



6. Validate

If the final checksum satisfies:

```python
total % 10 == 0
```

the card number is considered valid.



Concepts Practiced

This project helped reinforce:

* String manipulation
* Slicing
* Loops
* Arithmetic operations
* Input validation
* Algorithm implementation
* Checksum calculations
* Real-world problem solving



Example Walkthrough

Card Number:

```text
4539148803436467
```

Process:

```text
Sum odd digits
+
Process even digits
=
Final checksum
```

Result:

```text
VALID
```



Future Improvements

* 💳 Detect card type (Visa, Mastercard, American Express)
* 📋 Validate multiple card numbers from a file
* 🌐 Build a web-based validator
* 📊 Display detailed checksum calculations
* 🧪 Add automated unit tests



Known Limitations

* Only performs checksum validation
* Does not verify whether a card actually exists
* No card issuer detection




Author

Abdurrahman

Python Developer | Aspiring AI/ML Engineer



Project Goal

This project was built to learn how validation algorithms work in real-world financial systems. It demonstrates the implementation of the Luhn Algorithm, a widely used checksum technique for verifying credit card numbers.

The project strengthens problem-solving skills, algorithmic thinking, and practical Python programming experience.
