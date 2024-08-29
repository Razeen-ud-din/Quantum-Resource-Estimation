# Azure Quantum Resource Estimator Workshop

QWorld's workshop materials for Azure Quantum Resource Estimator.

## Outline

1. Introduction
	* What is resource estimation?
	* Why do we need it?
	* Different examples of asymptotic complexity versus practical resource usage:
		- Mergesort vs Quicksort
		- Array vs Linked Lists
	* Classical error correction

2. Classical Resource Estimation
	* Error correction in classical computing: we need reduntant information
		- Types of errors
		- Error detection and correction techniques
	* Physical versus logical bits (in classical computing)
	* Hands-on: Building a simple classical resource estimator

3. Quantum Resource Estimation
	* The importance of resource estimation in quantum computing
		- How many qubits are needed for useful quantum computations?
		- How long until quantum-safe encryption is needed?
		- Basics of quantum error correction (to understand why and how much overhead is involved)
	* Challenges
		- Qubit count (circuit width)
			- Physical versus logical qubits
		- Circuit depth
		- Fault tolerance
		- Error correction schemes
		- Hardware topology
		- Gate count
		- (Universal) Gate Sets
		- _T_ gates
	* Introduction to QREs:
		- [Azure Quantum Resource Estimator](https://learn.microsoft.com/en-us/azure/quantum/intro-to-resource-estimation)
		- [`pyLITQTR`](https://github.com/isi-usc-edu/pyLIQTR)
		- ...
4. Quantum Resource Estimation: A First Example
	* Sparse State Preparation

5. Amplitude amplification with Grover

6. Phase estimation

7. TBD
	* Walkthrough fo estimating resources for Shor's algorithm
	* Some other algorithm related to security / cryptography

## Setup Instructions

### Setting up a Virtual Environment

1. **Install Python 3.8+**: Ensure you have Python 3.8 or higher installed. You can download it from [python.org](https://www.python.org/).

2. **Create a Virtual Environment**:
    ```sh
    python -m venv .venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
        ```sh
        .venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source .venv/bin/activate
        ```

4. **Install Required Packages**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Launch Jupyter Notebook**:
    ```sh
    jupyter notebook
    ```

## Additional Resources

- [Azure Quantum Documentation](https://learn.microsoft.com/en-us/azure/quantum/)
- [Qiskit Documentation](https://qiskit.org/documentation/)
