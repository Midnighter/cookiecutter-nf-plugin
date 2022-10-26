# Copyright (c) 2022 Moritz E. Beber
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Test the cookiecutter template initialization."""


import subprocess
from datetime import date
from pathlib import Path
from typing import Dict

import pytest
from cookiecutter.main import cookiecutter


TEMPLATE = Path(__file__).parent.parent


@pytest.fixture(scope="module")
def cookie_context() -> Dict[str, str]:
    """"""
    today = date.today()
    return {
        "full_name": "Mr. Hankey",
        "email": "hankey@southpark.com",
        "github_username": "hankey2412",
        "plugin_name": "The Cycle",
        "plugin_slug": "nf-cycle",
        "plugin_package": "cycle",
        "plugin_class_prefix": "Cycle",
        "plugin_short_description": "Track the cycle of p**.",
        "release_date": str(today),
        "year": str(today.year),
        "version": "1.0.0",
    }


@pytest.fixture(scope="function")
def project(tmp_path: Path, cookie_context: Dict[str, str]) -> Path:
    cookiecutter(
        template=str(TEMPLATE),
        no_input=True,
        output_dir=tmp_path,
        extra_context={
            "license": "MIT",
            **cookie_context,
        },
    )
    return tmp_path / "nf-cycle"


@pytest.mark.parametrize(
    "license", ["MIT", "BSD-3-Clause", "Apache-2.0", "proprietary"]
)
def test_init_template(tmp_path: Path, cookie_context: Dict[str, str], license: str):
    """Expect that the template can be initialized."""
    cookiecutter(
        template=str(TEMPLATE),
        no_input=True,
        output_dir=tmp_path,
        extra_context={
            "license": license,
            **cookie_context,
        },
    )
    project_files = {path.relative_to(tmp_path) for path in tmp_path.rglob("*")}
    root = Path("nf-cycle")
    expected = {
        root,
        root / "README.md",
        root / "Makefile",
        root / "plugins" / "build.gradle",
        root / "plugins" / "nf-cycle",
        root / "plugins" / "nf-cycle" / "build.gradle",
        root / "plugins" / "nf-cycle" / "src" / "main" / "nextflow" / "cycle",
        root / "plugins" / "nf-cycle" / "src" / "main" / "nextflow" / "cycle" / "CycleConfig.groovy",
        root / "plugins" / "nf-cycle" / "src" / "main" / "nextflow" / "cycle" / "CycleExtension.groovy",
        root / "plugins" / "nf-cycle" / "src" / "main" / "nextflow" / "cycle" / "CyclePlugin.groovy",
        root / "plugins" / "nf-cycle" / "src" / "resources" / "META-INF",
        root / "plugins" / "nf-cycle" / "src" / "resources" / "META-INF" / "extensions.idx",
        root / "plugins" / "nf-cycle" / "src" / "resources" / "META-INF" / "MANIFEST.MF",
    }
    assert expected.issubset(project_files), expected.difference(project_files)
    if license != "proprietary":
        assert (root / "LICENSE") in project_files


def test_gradlew_check(project: Path):
    """Expect that a newly initialized plugin passes the gradle checks."""
    subprocess.run(args=[str(project / "gradlew"), "check"], cwd=project)


def test_gradlew_test(project: Path):
    """Expect that a newly initialized plugin passes the gradle tests."""
    subprocess.run(args=[str(project / "gradlew"), "test"], cwd=project)


def test_gradlew_compile_groovy(project: Path):
    """Expect that a newly initialized plugin's Groovy classes can be compiled."""
    subprocess.run(args=[str(project / "gradlew"), "compileGroovy"], cwd=project)
