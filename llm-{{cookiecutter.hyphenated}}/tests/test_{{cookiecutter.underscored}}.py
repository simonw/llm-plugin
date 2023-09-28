from llm.plugins import pm


def test_plugin_is_installed():
    names = [mod.__name__ for mod in pm.get_plugins()]
    assert "llm_{{ cookiecutter.underscored }}" in names
