# Distributed Systems Assignment (2021-2025)

This repository contains Python implementations for **Lamport's Logical Clock** and **Vector Clock**, two mechanisms used in distributed systems to ensure event ordering and maintain causality.

## Files

- `lamport_clock.py`: Implementation of Lamport's Logical Clock.
- `vector_clock.py`: Implementation of Vector Clock.

## Overview

### Lamport's Logical Clock
Lamport's Logical Clock provides a logical ordering of events in a distributed system where there is no global clock. It ensures the "happened-before" relationship (\(a \to b\)) between events is preserved.

**Key Features**:
- Maintains a single scalar clock for each process.
- Updates the clock on internal events, message sends, and message receives.

### Vector Clock
Vector Clocks extend Lamport's Logical Clock by maintaining a vector of timestamps, allowing each process to track the logical time of all other processes.

**Key Features**:
- Tracks causality more accurately.
- Maintains a vector of timestamps for each process.

## Example Outputs

### Lamport's Logical Clock
```bash
Process 1 performs an event.
Logical Clock: 1

Process 1 sends a message to Process 2.
Process 1 clock after sending: Logical Clock: 2

Process 2 receives the message from Process 1.
Process 2 clock after receiving: Logical Clock: 3
```
### Vector Clock
```bash
Process 1 performs an event.
Process 0 Clock: [1, 0]

Process 1 sends a message to Process 2.
Process 1 clock after sending: Process 0 Clock: [2, 0]

Process 2 receives the message from Process 1.
Process 2 clock after receiving: Process 1 Clock: [2, 1]
```
