# Hamming

Welcome to Hamming on Exercism's Python Track.
If you need help running the tests or submitting your code, check out `HELP.md`.

## Introduction

Your body is made up of cells that contain DNA.
Those cells regularly wear out and need replacing, which they achieve by dividing into daughter cells.
In fact, the average human body experiences about 10 quadrillion cell divisions in a lifetime!

When cells divide, their DNA replicates too.
Sometimes during this process mistakes happen and single pieces of DNA get encoded with the incorrect information.
If we compare two strands of DNA and count the differences between them, we can see how many mistakes occurred.
This is known as the "Hamming distance".

The Hamming distance is useful in many areas of science, not just biology, so it's a nice phrase to be familiar with :)

## Instructions

Calculate the Hamming distance between two DNA strands.

We read DNA using the letters C, A, G and T.
Two strands might look like this:

    GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT
    ^ ^ ^  ^ ^    ^^

They have 7 differences, and therefore the Hamming distance is 7.

## Implementation notes

The Hamming distance is only defined for sequences of equal length, so an attempt to calculate it between sequences of different lengths should not work.

Note:   zip(a, b) pairs the characters from both strands into tuples, 
        e.g. a = "abc", b = "def", then zip() returns positional pairs ("a", "d"), ("b", "e"), ...

Note:   We can iterate over the tuples e.g., (function for a, b in zip(strand_a, strand_b) if condition)
        and consume the returned generator expression in a sum() function

## Exception messages

Sometimes it is necessary to [raise an exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). When you do this, you should always include a **meaningful error message** to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the [built in error types](https://docs.python.org/3/library/exceptions.html#base-classes), but should still include a meaningful message.

This particular exercise requires that you use the [raise statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) to "throw" a `ValueError` when the strands being checked are not the same length. The tests will only pass if you both `raise` the `exception` and include a message with it.

To raise a `ValueError` with a message, write the message as an argument to the `exception` type:

```python
# When the sequences being passed are not the same length.
raise ValueError("Strands must be of equal length.")
```

## Source

### Created by

- @betegelse

### Contributed to by

- @behrtam
- @cmccandless
- @Dog
- @gabriel376
- @GascaK
- @guaneec
- @iandexter
- @ikhadykin
- @kytrinyx
- @N-Parsons
- @parthsharma2
- @pheanex
- @pywkm
- @sjakobi
- @tqa236
- @yawpitch

### Based on

The Calculating Point Mutations problem at Rosalind - https://rosalind.info/problems/hamm/