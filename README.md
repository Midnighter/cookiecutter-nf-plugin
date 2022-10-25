# Cookiecutter Template for Nextflow Plugins

_Generate a project directory structure and files for your very own [nextflow plugin](https://www.nextflow.io/docs/latest/plugins.html)._

## Usage

### Dependencies

Create a Python virtual environment. You can [read this guide to learn more](https://realpython.com/python-virtual-environments-a-primer/)
about them and how to create one. Alternatively, particularly if you are a
Windows or Mac user, you can also use [Anaconda](https://docs.anaconda.com/anaconda/).

After creating a virtual environment, install dependencies with `pip` or `conda`.

```bash
pip install cruft jinja2-strcase
```

### Create

Then run [`cruft`](https://cruft.github.io/cruft) to generate your project template by answering the questions that follow.

```bash
cruft create https://github.com/Midnighter/cookiecutter-nf-plugin
```

The cookiecutter project itself is provided under the [Apache Software License 2.0](https://www.apache.org/licenses/LICENSE-2.0), however, you can freely choose the license for your generated plugin.

### Update

If, at a later point, you want to update your plugin project with changes added to this cookiecutter template, you can do so with one command from the root of your project directory:

```bash
cruft update
```

You will get a chance to review the changes to be merged into your existing project.

## Copyright

-   Copyright © 2022 Moritz E. Beber
-   Free software distributed under the [Apache Software License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
