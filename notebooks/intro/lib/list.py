from typing import Optional, Self

class List:
	"""A doubly linked list."""
	class Node:
		"""A node of a linked list."""
		def __init__(
			self, value: int = 0,
			previous: Optional[Self] = None,
			next: Optional[Self] = None,
		):
			"""
			Initializes a node with the given value and links.

			Parameters
			----------
			value
				The value to store in the node.
			previous
				The previous node in the list.
			next
				The next node in the list.
			"""
			self.value = value
			self.previous = previous
			self.next = next

		def __repr__(self) -> str:
			return f"Node({self.value}, {repr(self.previous)}, {repr(self.next)})"

		def __str__(self) -> str:
			width = len(str(self.value))

			top = f"╭{'─' * (width + 2)}╮"
			middle = f"│ {self.value} │"
			bottom = f"╰{'─' * (width + 2)}╯"

			if self.previous is not None:
				top = " ╭-╮" + top
				middle = "→· " + middle
				bottom = " ╰-╯" + bottom

			if self.next is not None:
				top += "╭-╮ "
				middle += " ·←"
				bottom += "╰-╯ "

			return f"{top}\n{middle}\n{bottom}"

	def __init__(self, head: Optional[Node] = None):
		"""
		Initializes a linked list with the given head node.

		Parameters
		----------
		head
			The head node of the list.
		"""
		self.head = head

	@property
	def is_empty(self) -> bool:
		"""
		Whether the list is empty.

		Returns
		-------
		bool
			`True` if the list is empty; `False` otherwise.
		"""
		return self.head is None

	def find_node(self, new_value: int) -> Optional[Node]:
		"""
		Finds the node after which the new value should be inserted to keep the linked list sorted.

		Parameter
		----------
		new_value
			The new value.

		Returns
		-------
		Node
			The node after which the new value should be inserted.
		None
			If the new value should be inserted at the start.

		Notes
		-----
		* The node is found via linear search.
		* This is to maintain parity with the array implementation.
		"""
		if self.is_empty:
			return None

		current = self.head
		assert current is not None, "not self.is_empty ⇒ self.head is not None"

		while (current.next is not None) and (new_value > current.next.value):
			current = current.next

		return current

	def insert(self, new_value: int, node: Optional[Node]):
		"""
		Inserts the given value after the given node.

		Parameters
		----------
		new_value
			The value to insert after the given node.
		node
			The node after which to insert the value.
		"""
		if node is None:
			self.head = self.Node(new_value, None, self.head)
			return

		new_node = self.Node(new_value, node, node.next)
		node.next = new_node

		if new_node.next is not None:
			new_node.next.previous = new_node

	def remove(self, node: Node):
		"""
		Removes the given node from the linked list.

		Parameters
		----------
		node
			The node to remove.
		"""
		if node is self.head:
			self.head = node.next
			if node.next is not None:
				node.previous = None
			return

		assert node.previous is not None, "Only the head node has no previous node"
		node.previous.next = node.next

	def __len__(self) -> int:
		length = 0
		current = self.head
		while current is not None:
			length += 1
			current = current.next
		return length

	def __getitem__(self, index: int) -> Node:
		if index < 0:
			raise IndexError("Index must be non-negative")

		current_node = self.head
		current_index = 0

		while current_node is not None:
			if current_index == index:
				return current_node
			current_node = current_node.next
			current_index += 1

		raise IndexError("Index out of bounds")

	def __setitem__(self, index: int, value: int):
		if index < 0:
			raise IndexError("Index must be non-negative")

		if (index == 0) and (self.is_empty):
			self.head = self.Node(value)
			return

		moved_node = self[index]
		new_node = self.Node(value, moved_node.previous, moved_node)

		if moved_node.previous is not None:
			moved_node.previous.next = new_node

		moved_node.previous = new_node

	def __repr__(self) -> str:
		return f"List({self.head})"
