from typing import Optional, Generic, TypeVar

Value = TypeVar("Value")

class List(Generic[Value]):
	class Node:
		def __init__(self, value: Value, next: Optional["List.Node"] = None):
			self.value = value
			self.next = next

		def __repr__(self) -> str:
			return f"Node({self.value})"

		def __eq__(self, other: object) -> bool:
			if not isinstance(other, List.Node):
				return False
			return self.value == other.value and self.next == other.next

	def __init__(self, head: Optional["List.Node"] = None):
		self.head = head

	def __repr__(self) -> str:
		return f"List({self.head})"
