import platform

print(platform.system())
print(platform.release())
print(platform.processor())
print(platform.architecture())
print(platform.machine())

#The platform module provides an API to get information about the underlying system/platform where our code runs.
# Information such as OS name, Python Version, Architecture, Hardware information, etc. is exposed via platform module functions.