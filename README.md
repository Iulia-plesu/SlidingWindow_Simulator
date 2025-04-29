# Selective Repeat Protocol Simulation

## Overview

**SlidingWindow_Simulator** is a Python-based simulation of the **Selective Repeat ARQ** protocol—an essential technique used in reliable data communication. This simulator models the behavior of a sender and receiver system that transmits data packets over an unreliable network, handling transmission delays, packet loss, acknowledgment (ACK) loss, and retransmissions using a sliding window mechanism.

The purpose of this project is to demonstrate how the Selective Repeat protocol ensures reliable delivery, even in the presence of transmission errors.

## Features

- Simulates a sender and a receiver.
- Implements the Selective Repeat algorithm with retransmission and timeout.
- Models realistic transmission behavior including:
  - Packet loss (20% probability),
  - ACK loss (15% probability),
  - Timeouts and randomized retransmission delays.
- Dynamically generated transmission window size.
- Clear visualization of sender/receiver buffer state and transmission window.

## Getting Started

### Requirements

- Python 3.7 or higher
- No external libraries are required; only Python's built-in `random` and `time` modules are used.

### Installation & Running

Clone and run the repository:

```bash
git clone https://github.com/yourusername/SlidingWindow_Simulator.git
cd SlidingWindow_Simulator
python Main.py
