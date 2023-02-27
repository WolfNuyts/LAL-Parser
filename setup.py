import setuptools

setuptools.setup(
    name='lal_parser',
    version='1.0',
    author='KhalilMrini',
    license='',
    url='https://github.com/KhalilMrini/LAL-Parser',
    author_email='',
    description='Neural Adobe-UCSD Parser',
    install_requires=open('requirements.txt').read().strip().splitlines(),
    package_dir={"": "src_joint"},
    packages=setuptools.find_packages("src_joint"),
    include_package_data=True,
    python_requires='>=3.8',
)