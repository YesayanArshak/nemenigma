from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils.module_loading import import_string


from key.keys.base import ABCKeyTool
from key.models import KeyType, KeyToolType


tools: dict[int, ABCKeyTool] = {
	tool_type._value_: import_string(settings.KEY_TOOLS[tool_type._name_]['NAME'])(**settings.KEY_TOOLS[tool_type._name_].get('OPTIONS', {}))
	for tool_type in KeyToolType
}

def validate(key: str, key_type: KeyType, tool: KeyToolType):
	match key_type:
		case KeyType.PUBLIC:
			if not tools[tool._value_].validate_public_key(key):
				raise ValidationError(f'Key is invalid.')
		case KeyType.PRIVATE:
			if not tools[tool._value_].validate_private_key(key):
				raise ValidationError(f'Key is invalid.')
		case _:
			raise NotImplementedError(f'KeyType validation for ({key_type!r}) not implemented.')
