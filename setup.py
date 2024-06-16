from setuptools import setup, find_packages

setup(
    name='test_lib',
    use_scm_version=True,
    description='Library for automation testing of digital instrument clusters.',
    author='Dinesh-D-2000',
    author_email='dineshdeena488@gmail.com',
    url="https://github.com/Dinesh-D-2000/Cluster_Automation_testing_library/tree/main/test_lib",
    packages=find_packages(include=["test_lib", "test_lib.*"]),
    include_package_data=True,
)

print(find_packages(include=["test_lib", "test_lib.*"]))

