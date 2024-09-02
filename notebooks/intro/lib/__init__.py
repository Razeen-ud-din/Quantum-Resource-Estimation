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

def plot(
	x: list[int],
	y: list[float],
	x_label: str,
	y_label: str,
	title: str,
	format: str = "o",
	style: str = "seaborn-v0_8"
):
	"""
	Plots a graph of x and y.

	Parameters
	----------
		x
			The x-axis values.
		y
			The y-axis values.
		x_label
			The x-axis label.
		y_label
			The y-axis label.
		title
			The title of the graph.
		format
			The format of the points.
		style
			The style of the graph.
	"""
	import matplotlib.pyplot as Plot

	Plot.style.use(style)
	Plot.xlabel(x_label)
	Plot.ylabel(y_label)
	Plot.title(title)
	Plot.plot(x, y, format)
	Plot.show()
