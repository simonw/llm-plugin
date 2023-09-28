from cookiecutter.main import cookiecutter
import pathlib

TEMPLATE_DIRECTORY = str(pathlib.Path(__file__).parent.parent)


def test_generated_files(tmpdir):
    generate(
        tmpdir,
        {
            "plugin_name": "foo",
            "description": "blah",
        },
    )
    assert paths(tmpdir) == {
        "llm-foo/.github/workflows",
        "llm-foo/LICENSE",
        "llm-foo/README.md",
        "llm-foo/.github/workflows/publish.yml",
        "llm-foo/llm_foo.py",
        "llm-foo/.github/workflows/test.yml",
        "llm-foo/pyproject.toml",
        "llm-foo/.gitignore",
        "llm-foo",
        "llm-foo/.github",
        "llm-foo/tests/test_foo.py",
        "llm-foo/tests",
    }


def generate(directory, context):
    cookiecutter(
        template=TEMPLATE_DIRECTORY,
        output_dir=str(directory),
        no_input=True,
        extra_context=context,
    )


def paths(directory):
    paths = list(pathlib.Path(directory).glob("**/*"))
    paths = [r.relative_to(directory) for r in paths]
    return {str(f) for f in paths if str(f) != "."}
