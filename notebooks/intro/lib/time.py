from typing import Callable, Any

def time(function: Callable[..., Any], runs: int = 20) -> float:
	"""
	Measure the time taken to execute a function.

	Args:
		function: The function to measure.
		runs: The number of times to run the function

	Returns:
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
