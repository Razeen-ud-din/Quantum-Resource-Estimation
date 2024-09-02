class Array:
	"""A contiguous array of integers."""
	def __init__(self, *data: int):
		"""
		Initializes an array with the given data.

		Parameters
		----------
		data
			The data to store in the array.

		Notes
		-----
		* The data is stored as a NumPy array internally.
		"""
		from numpy import array

		self.data = array(data, dtype=int)

	@property
	def is_empty(self) -> bool:
		"""
		Whether the array is empty.

		Returns
		-------
		bool
			`True` if the array is empty; `False` otherwise.
		"""
		return len(self) == 0

	def find_index(self, new_value: int) -> int:
		"""
		Finds the index of the new value that would keep the array sorted.

		Parameters
		----------
		new_value
			The new value.

		Returns
		-------
		int
			The index of the given value.

		Notes
		-----
		* The index is found via linear search
		* This is to maintain parity with the linked list implementation
		"""
		# If the array is empty, the new value goes at the start.
		if self.is_empty:
			return 0

		# Otherwise, it goes at the first index where the new value is smaller.
		for (index, value) in enumerate(self.data):
			if new_value <= value:
				return index

		# If there is no such index, the new value goes at the end.
		return len(self)

	def insert(self, value: int, index: int):
		"""
		Inserts the given value at the given index.

		Parameters
		----------
		value
			The value to insert at the given index.
		index
			The index to insert the value at.
		"""
		from numpy import insert

		self.data = insert(self.data, index, value)

	def remove(self, index: int):
		"""
		Removes the value at the given index.

		Parameters
		----------
		index
			The index to remove the value at.
		"""
		from numpy import delete

		self.data = delete(self.data, index)

	def __len__(self) -> int:
		return self.data.size

	def __getitem__(self, index: int) -> int:
		return self.data[index]

	def __setitem__(self, index: int, value: int):
		self.data[index] = value

	def __repr__(self) -> str:
		return f"Array({self.data})"

	def __str__(self):
		if self.is_empty:
			return "╭─ ─ ─ ─╮\n│ ᴇᴍᴘᴛʏ │\n╰─ ─ ─ ─╯"

		# Determine the width of the largest number
		max_width = max(len(str(value)) for value in self.data)

		top = ""
		middle = ""
		bottom = ""

		for value in self.data:
			top += f"╭{'─' * (max_width + 2)}╮"
			middle += f"│ {value:^{max_width}} │"
			bottom += f"╰{'─' * (max_width + 2)}╯"

		return f"{top}\n{middle}\n{bottom}"
