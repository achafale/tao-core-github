# Copyright (c) 2017-2020, NVIDIA CORPORATION.  All rights reserved.

load("//ci/runtime_resources:extension.bzl", "py_static_analysis")
load("@pip_deps//:requirements.bzl", "requirement")
package(default_visibility = ["//visibility:public"])

py_library(
    name = "all",
    srcs = ["__init__.py"],
    deps = [
        ":clearml",
    ],
)

py_library(
    name = "clearml",
    srcs = ["clearml.py"],
    deps=[
        requirement("clearml"),
    ],
)

py_static_analysis(
    name = "static_test",
    python_module = "iva",
)
