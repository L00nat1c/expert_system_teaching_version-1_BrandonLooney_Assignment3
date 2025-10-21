# Expert System Mini Project (Teaching Version)

## Overview
You will build a simple **rule-based expert system** using **forward chaining**.

### Files Provided
| File | Description | Status |
|------|--------------|---------|
| `engine.py` | Core inference engine | Incomplete (you implement key functions) |
| `kb_loader.py` | Loads JSON knowledge base | Complete |
| `kb/laptop_rules.json` | Sample KB (1 rule only) | Incomplete (you add 9 more) |
| `main.py` | Command-line interface | Incomplete |
| `tests/` | Folder for test cases | Empty |

---

## Your Tasks

1. **Implement the inference logic**
   - Complete `can_fire()`, `run()`, and `conclusions()` in `engine.py`.

2. **Expand the knowledge base**
   - Add at least **9 more rules** to `kb/laptop_rules.json`.

3. **Complete `main.py`**
   - Load rules.
   - Collect user facts.
   - Run inference.
   - Display recommendations and which rules fired.

4. **(Optional) Bonus**
   - Implement explanations: *“Why”* and *“How”* reasoning.
   - Add uncertainty or confidence factors.

---

## Example Run (after completion)

```
Is portability important? (y/n): y
Do you need long battery life? (y/n): y
Is your budget high? (y/n): y

=> Recommendation: premium_ultrabook
=> Explanation: derived from rule 'Premium Ultrabook'
```

---

## Grading Rubric (100 pts)

| Component | Points |
|------------|--------|
| Inference engine (`engine.py`) | 40 |
| Rule base completeness | 20 |
| Correct reasoning output | 20 |
| Code readability & structure | 10 |
| Report / explanation clarity | 10 |

---


# Report

I have completed the missing parts of the code and it should run like the given example. <br>
I used Visual Studio Code to edit the files for this assignment. <br>
To run the code, I went to the main.py file, and ran the code using the built-in terminal.<br>
A user will need to enter 13 different inputs isntead of 3 now. And there are now 10 different rules in the laptop_rules.json file. <br>
There are brief comments in the code to explain what each section is supposed to do. <br>
<br>

I have a testing.py file with at least five example tests with their expected inputs and output. They will not run like the expected output example, but it will run the five tests and will show whether they failed or if they are "OK". <br>
<br>
To run the testing.py file, you must input the following command in the terminal.
```
python -m unittest tests/testing.py
```

<br>
