from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='DiscordHooks',
    version='1.0',
    packages=['DiscordHooks'],
    install_requires=requirements,
    url='https://github.com/MeitarR/DiscordHooks',
    license='',
    author='MeitarR',
    author_email='meitarr013@gmail.com',
    description='A python module for easily execute discord webhooks with embeds and more.'
)
