try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '페르칼 25번 행성의 고던족',
    'author': '내 이름',
    'url': '프로젝트 URL',
    'download_url': '내려받을 수 있는 곳.',
    'author_email': '내 이메일',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['gothonweb'],
    'scripts': [],
    'name': 'gothonweb'
}

setup(**config)

