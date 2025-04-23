from setuptools import setup

setup(
    name='quillpy',
    version='0.1.8',
    description='A lightweight terminal-based text editor',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='@mralfiem591',
    url='https://github.com/mralfiem591/quillpy',
    license='MIT',
    python_requires='>=3.6',
    project_urls={
        'Bug Tracker': 'https://github.com/mralfiem591/quillpy/issues',
        'Source Code': 'https://github.com/mralfiem591/quillpy',
    },
    packages=['quillpy'],
    install_requires=[
        'windows-curses; platform_system=="Windows"',
        'pywin32; platform_system=="Windows"'
    ],
    entry_points={
        'console_scripts': [
            'quillpy=quillpy.quill:main'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Text Editors :: Documentation',
        'Topic :: Utilities'
    ]
)
