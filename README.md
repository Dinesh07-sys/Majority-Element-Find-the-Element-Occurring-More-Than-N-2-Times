# Majority Element

A Python implementation of the Boyer–Moore majority vote approach for identifying the majority element in an array.

## Overview

The program searches for an element that appears more than half the time in the given array.

Instead of storing frequencies for every value, it maintains:

* A `candidate` representing the current possible majority element.
* A `balance` representing the candidate's current advantage.

The candidate changes whenever the balance reaches zero. Matching values increase the balance, while different values decrease it.

## How It Works

The algorithm starts with:

```python
candidate = 0
balance = 0
```

The array is then processed one element at a time.

When the balance becomes zero, the current value becomes the new candidate:

```python
if balance == 0:
    candidate = value
```

If the current value matches the candidate, the balance increases:

```python
if value == candidate:
    balance += 1
```

Otherwise, the balance decreases:

```python
else:
    balance -= 1
```

This process continues until every element has been examined. The remaining candidate is then returned.

## Example

The program uses:

```python
nums = [2, 3, 2, 3, 3, 1, 3, 3]
```

The value `3` occurs more frequently than any other value and appears more than half of the time.

The program therefore returns:

```text
3
```

The sample input is defined in `main()` and passed to `majorityElement()`.

## Algorithm

1. Initialize `candidate` and `balance`.
2. Traverse every value in the array.
3. If the balance is zero, select the current value as the candidate.
4. Increase the balance when the value matches the candidate.
5. Decrease it when the value differs.
6. Return the final candidate.

## Why the Balance Works

Think of matching and different elements as opposing each other.

A value equal to the current candidate adds one to its balance. A different value removes one. When enough opposing values cancel the candidate's current advantage, the balance reaches zero and the next element gets an opportunity to become the candidate.

For an array guaranteed to contain a majority element, the final candidate is that majority element.

## Complexity

| Metric          | Complexity |
| --------------- | ---------- |
| Time            | O(N)       |
| Auxiliary Space | O(1)       |

The array is scanned once and only two main variables are maintained during the process.

## Important Note

The uploaded implementation returns the final candidate directly. It does not perform a second pass to verify that the candidate actually occurs more than `N / 2` times. Therefore, the algorithm assumes the input satisfies the majority-element condition.

## Running the Program

Run the file with:

```bash
python "2 Times.py"
```

Expected output:

```text
3
```
