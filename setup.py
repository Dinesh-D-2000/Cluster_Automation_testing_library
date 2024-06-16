from setuptools import setup, find_packages

setup(
    name='Cluster_Automation_testing_library',
    use_scm_version=True,
    description='Library for automation testing of digital instrument clusters.',
    author='Dinesh-D-2000',
    author_email='dineshdeena488@gmail.com',
    url="https://github.com/Dinesh-D-2000/Cluster_Automation_testing_library",
    packages=find_packages(include=["Cluster_Automation_testing_library"]),
    include_package_data=True,
)
