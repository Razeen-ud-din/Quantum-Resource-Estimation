def factorize(r: int) -> tuple[int, int]:
	"""
	Factorizes the input into its two prime factors.

	Parameters
	----------
	r
		The number to factorize.
		Must be a positive composite integer that has exactly two prime factors.

	Returns
	-------
	tuple[int, int]
		The two prime factors of the input number.

	Raises
	------
	ValueError
		If the input is prime.
	"""
	from math import floor, sqrt

	# We handle the special case of 2 separately so we can optimize later
	if r % 2 == 0:
		p = 2
		q = r // 2
		return (p, q)

	# 𝑝 > 2 because we already checked if 𝑟 was an even number
	lower_limit = 3

	# 𝑝 < ⌊√𝑟 + 1⌋ because 𝑟 cannot have factors larger than √𝑟
	upper_limit = floor(sqrt(r) + 1)

	# 𝑝 is prime ⇒ 𝑝 is not an even number
	# ∴ we can take steps of size 2, if we start from 3
	step_size = 2

	for p in range(lower_limit, upper_limit, step_size):
		if r % p == 0:
			q = r // p
			return (p, q)

	# Exiting loop without finding a factor ⇒ 𝑟 is prime
	raise ValueError("r is prime")
