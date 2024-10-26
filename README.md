# Prime-Palindrome Finder

## Overview
This Python program helps you find "special numbers" within a specified range. Special numbers are both prime (divisible only by 1 and themselves) and palindromic (read the same forwards and backwards).

Given two integers, `m` and `n`, the program counts and lists all special numbers between them (inclusive). If fewer than six special numbers are found, it lists all of them. Otherwise, it displays the first three smallest and last three largest special numbers in the range.

## Features
- **Prime Check**: Only considers numbers that are prime.
- **Palindrome Check**: Ensures numbers read the same forwards and backwards.
- **Dynamic Display**: Shows all special numbers if there are fewer than six; otherwise, it lists the first three and last three special numbers.
- **Efficient Execution**: Designed to handle large ranges without exceeding a one-hour runtime limit for any test case.

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/prime-palindrome-finder.git
2. Navigate to the Project Directory
  cd prime-palindrome-finder
3. Run the Program
   python special_numbers.py
4. Input your values for m and n when prompted

##Example Output

For an input range m=1 and n=200, the ouput is 
Total Special Numbers: 10
Special Numbers: 2, 3, 5, 151, 181, 191

##Test Cases

The program is tested with various ranges to ensure efficiency and accuracy:

	•	Range: 1 - 2,000
	•	Range: 100 - 10,000
	•	Range: 1 - 1,000,000,000,000
## Requirements
• Python 3.x

## Notes
The program does not use any hard-coded lists or external files for computation. It relies on Python’s built-in libraries for prime checking and palindrome verification to ensure efficiency and readability.

##Contributing
The program does not use any hard-coded lists or external files for computation. It relies on Python’s built-in libraries for prime checking and palindrome verification to ensure efficiency and readability.

##License 
MIT License

### File Structure

```plaintext
prime-palindrome-finder/
│
├── README.md               # Project overview and usage instructions
├── LICENSE                 # License file (e.g., MIT)
└── special_numbers.py      # Main Python program


 



