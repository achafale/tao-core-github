# Copyright (c) 2022-2023, NVIDIA CORPORATION.  All rights reserved.

"""Version string for the TAO Toolkit TF2 AI models/tasks."""

MAJOR = "4"
MINOR = "22.11"
PATCH = "01"
PRE_RELEASE = ''

# Use the following formatting: (major, minor, patch, pre-release)
VERSION = (MAJOR, MINOR, PATCH, PRE_RELEASE)

# Version of the library.
__version__ = '.'.join(map(str, VERSION[:3])) + ''.join(VERSION[3:])

# Version of the file format.
__format_version__ = 2

# Other package info.
__package_name__ = "nvidia-tao-core"
__description__ = "NVIDIA's package for core modules common across TAO Toolkit DNNs."
__keywords__ = "nvidia, tao, core"

__contact_names__ = "Varun Praveen"
__contact_emails__ = "vpraveen@nvidia.com"

__license__ = "NVIDIA Proprietary Software"
