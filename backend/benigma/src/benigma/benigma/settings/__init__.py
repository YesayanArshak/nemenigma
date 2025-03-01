import os


match os.environ.get('DJANGO_MODE'):
	case 'DEVELOPMENT':
		from .dev import *
	case 'PRODUCTION':
		from .prod import *
	case DJANGO_MODE:
		raise ValueError(f"ENV DJANGO_MODE must be 'DEVELOPMENT' or 'PRODUCTION'.(not {DJANGO_MODE})")
