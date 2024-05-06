from setuptools import find_packages, setup

package_name = 'waypoint_logger'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='marudhu2004',
    maintainer_email='marudhupaandian@gmail.com',
    description='TODO: Package description',
    license='MIT',
    tests_require=[],
    entry_points={
        'console_scripts': [
            "waypoint_logger:waypoint_logger.py:main"
        ],
    },
)
