from typing import Callable, Any

def time(function: Callable[..., Any], runs: int = 100) -> float:
	"""
	Measure the time taken to execute a function.

	Parameters
	----------
		function
			The function to measure.
		runs
			The number of times to run the function

	Returns
	-------
		float
			The time taken to execute the function.
	"""
	from timeit import default_timer as timer

	sum = 0.0

	for _ in range(runs):
		start_time = timer()
		function()
		end_time = timer()
		elapsed_time = end_time - start_time
		sum += elapsed_time

	return sum / runs

def sci(number: str) -> str:
	"""
	Converts a number to scientific notation.

	Parameters
	----------
		number
			The number to convert.

	Returns
	-------
		str
			The number in scientific notation.
	"""

	superscript = {
		"0": "⁰",
		"1": "¹",
		"2": "²",
		"3": "³",
		"4": "⁴",
		"5": "⁵",
		"6": "⁶",
		"7": "⁷",
		"8": "⁸",
		"9": "⁹",
		"-": "⁻",
	}

	[mantissa, exponent] = number.split("e")
	exponent = str(int(exponent))

	new_exponent = "".join([superscript[symbol] for symbol in exponent])

	return f"{mantissa}·10{new_exponent}"
