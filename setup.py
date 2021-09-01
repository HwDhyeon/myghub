"""Setup"""

from setuptools import setup
from setuptools import find_packages


setup_options = {
    'name': 'myghub',
    'version': '0.3.0',
    'description': 'Tracking all GitHub API',
    'author': 'HwDhyeon',
    'author_email': 'dev_donghyun@kakao.com',
    'url': 'https://github.com/HwDhyeon/my-github-tracker',
    'python_requires': '>=3.9',
    'packages': find_packages(),
    'install_requires': [
        'fire>=0.4.0',
        'fastapi>=0.64.0',
        'uvicorn[standard]>=0.13.4',
        'python-dotenv>=0.17.1',
        'PyGithub>=1.55'
    ],
    'entry_points': {
        'console_scripts': [
            'myghub=myghub.main:app'
        ]
    },
    'zip_safe': False,
}

setup(**setup_options)
