from llm.plugins import get_plugins


def test_plugin_is_installed():
    plugins = get_plugins()
    names = [plugin["name"] for plugin in plugins]
    assert "llm-{{ cookiecutter.hyphenated }}" in names
