import click
import llm


@llm.hookimpl
def register_commands(cli):
    return
    # @cli.command()
    # def hello_world():
    #     "Say hello world"
    #     click.echo("Hello world!")
