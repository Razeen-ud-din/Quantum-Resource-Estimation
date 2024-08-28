from typing import Optional, Generic, TypeVar

Value = TypeVar("Value")

class List(Generic[Value]):
	class Node:
		def __init__(self, value: Value, next: Optional["List.Node"] = None):
			self.value = value
			self.next = next

	def __init__(self, head: Optional["List.Node"] = None):
		self.head = head
