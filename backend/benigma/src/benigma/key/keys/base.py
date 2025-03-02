import abc


class ABCKeyTool(abc.ABC):
	@abc.abstractmethod
	def validate_public_key(self, public_key: str) -> bool:
		pass

	@abc.abstractmethod
	def validate_private_key(self, private_key: str) -> bool:
		pass

