# Git Assignment - Hero Vired

## Repository Overview

This repository contains a series of tasks related to Git and GitHub, involving creating branches, merging, handling large files with Git LFS, and implementing features for a calculator and geometry calculator.

### Files in Repository
- `CalculatorPlus.py`: A Python script with basic calculator functions.
- `geo_cal.py`: A Python script for geometry calculations.
- `large_file.bin`: A large binary file used for demonstrating Git LFS.
- `README.md`: This file.

## Getting Started

### Cloning the Repository
To clone the repository to your local machine, run:
```bash
git clone https://github.com/Ravikishans/git_assignment_HeroVired.git
cd git_assignment_HeroVired
```

### Task 1: Basic Calculator Features

1. **Create and Switch to `dev` Branch**
    ```bash
    git checkout -b dev
    ```

2. **Create and Edit `CalculatorPlus.py`**
    ```bash
    touch CalculatorPlus.py
    code .
    ```
    Write the Python script for calculating addition, subtraction, division, and multiplication.

3. **Commit Changes in `dev` Branch**
    ```bash
    git add .
    git commit -m "Initial version of CalculatorPlus.py"
    ```

4. **Merge `dev` Branch into `main` and Push**
    ```bash
    git checkout main
    git merge dev
    git push origin main
    ```

5. **Add Collaborator to Repository**

6. **Create `feature/sqrt` Branch and Implement Square Root Feature**
    ```bash
    git checkout -b feature/sqrt
    # Add partial sqrt code to CalculatorPlus.py
    git commit -a -m "Add partial sqrt code"
    ```

7. **Switch Back to `dev` Branch and Fix Errors**
    ```bash
    git checkout dev
    # Fix errors in CalculatorPlus.py
    git commit -a -m "Fix errors in CalculatorPlus.py"
    ```

8. **Complete Square Root Feature in `feature/sqrt` Branch**
    ```bash
    git checkout feature/sqrt
    # Complete sqrt code
    git commit -a -m "Complete sqrt code"
    ```

9. **Merge `feature/sqrt` into `dev` and Push for Review**
    ```bash
    git checkout dev
    git merge feature/sqrt
    # Push for collaborator review
    ```

10. **Resolve Conflicts and Merge into `main`**
    ```bash
    git checkout main
    git merge dev
    git push origin main
    ```

### Task 2: Handling Large Files with Git LFS

1. **Install Git LFS**
    ```bash
    git lfs install
    ```

2. **Create and Switch to `lfs` Branch**
    ```bash
    git checkout -b lfs
    ```

3. **Create Large Binary File**
    ```bash
    dd if=/dev/urandom of=large_file.bin bs=1M count=200
    ```

4. **Track and Commit Large File**
    ```bash
    git lfs track "*.bin"
    git add .gitattributes
    git add large_file.bin
    git commit -m "Add large binary file"
    git push origin lfs
    ```

5. **Merge `lfs` Branch into `main`**
    ```bash
    git checkout main
    git merge lfs
    git push origin main
    ```

### Task 3: Geometry Calculator

1. **Create and Switch to `geometry-calculator` Branch**
    ```bash
    git checkout -b geometry-calculator
    touch geo_cal.py
    ```

2. **Commit Initial Version of `geo_cal.py`**
    ```bash
    git add geo_cal.py
    git commit -m "Add initial geo_cal.py"
    ```

3. **Create `feature/circle-area` Branch and Cherry-Pick Commit**
    ```bash
    git checkout -b feature/circle-area
    git cherry-pick <commit-id>
    ```

4. **Implement Circle Area Feature and Stash Changes**
    ```bash
    # Write circle area code
    git stash
    ```

5. **Create `feature/rectangle-area` Branch and Cherry-Pick Commit**
    ```bash
    git checkout -b feature/rectangle-area
    git cherry-pick <commit-id>
    ```

6. **Implement Rectangle Area Feature and Stash Changes**
    ```bash
    # Write rectangle area code
    git stash
    ```

7. **Apply Stashed Changes in `feature/circle-area` Branch**
    ```bash
    git checkout feature/circle-area
    git stash apply
    git add .
    git commit -m "Complete circle area feature"
    ```

8. **Apply Stashed Changes in `feature/rectangle-area` Branch**
    ```bash
    git checkout feature/rectangle-area
    git stash apply
    git add .
    git commit -m "Complete rectangle area feature"
    ```

9. **Merge `feature/circle-area` and `feature/rectangle-area` into `geometry-calculator`**
    ```bash
    git checkout geometry-calculator
    git merge feature/circle-area
    git merge feature/rectangle-area
    ```

10. **Resolve Conflicts, Merge into `main`, and Push**
    ```bash
    git checkout main
    git merge geometry-calculator
    git push origin main
