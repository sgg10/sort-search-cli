import os
from typing import List, Optional

import click
from click import Context, Command

COMMANDS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))

CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help'],
    token_normalize_func=lambda x: x.lower(),
)


class CLIMultiCommand(click.MultiCommand):

    def list_commands(self, ctx: Context) -> List[str]:
        commands = [
            filename.removeprefix("cmd_").removesuffix(".py")
            for filename in os.listdir(COMMANDS_PATH)
            if filename.startswith("cmd_") and filename.endswith(".py")
        ]
        commands.sort()
        return commands

    def get_command(self, ctx: Context, cmd_name: str) -> Optional[Command]:
        try:
            mod = __import__(f"sort_search.commands.cmd_{cmd_name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli


@click.command(cls=CLIMultiCommand, context_settings=CONTEXT_SETTINGS)
def cli():
    """Welcome to Sort-Search CLI"""
    pass


if __name__ == "__main__":
    cli()
