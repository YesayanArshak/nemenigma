import tempfile


import gnupg


from key.keys.base import ABCKeyTool


class GPGKeyTool(ABCKeyTool):
	def validate_public_key(self, public_key: str) -> bool:
		with tempfile.TemporaryDirectory() as tmp_dir:
			gpg = gnupg.GPG(gnupghome=tmp_dir)

			scan_result = gpg.scan_keys_mem(public_key)

			if not scan_result:
				return False

			if scan_result[0]['type'] != 'pub':
				return False

			return True

	def validate_private_key(self, private_key: str) -> bool:
		with tempfile.TemporaryDirectory() as tmp_dir:
			gpg = gnupg.GPG(gnupghome=tmp_dir)

			scan_result = gpg.scan_keys_mem(private_key)

			if not scan_result:
				return False

			if scan_result[0]['type'] != 'sec':
				return False

			return True

