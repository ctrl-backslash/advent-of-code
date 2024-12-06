import glob
import importlib

import typer
from rich import print
from typing_extensions import Annotated

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main(
    date: Annotated[str, typer.Argument()],
    part: Annotated[int, typer.Argument(min=1, max=2)] = 1,
    input_file: Annotated[str, typer.Argument()] = 'input',
):
    date = f'dec_{date.removeprefix("dec_")}'
    if (
        not (files := list(glob.glob(f'{date}/{input_file.removesuffix(".txt")}*.txt')))
        and not (files := list(glob.glob(f'{input_file.removesuffix(".txt")}*.txt')))
        and not (
            input_file.startswith('test')
            and (
                files := list(
                    glob.glob(f'{date}/test*{input_file.removeprefix("test")}*.txt')
                )
                or list(glob.glob(f'test*{input_file.removeprefix("test")}*.txt'))
            )
        )
        and not (files := list(glob.glob(input_file)))
    ):
        raise typer.BadParameter(f'Unable to find {input_file}')

    print(
        getattr(importlib.import_module(f'{date}.solution'), f'part{part}')(
            open(files[0]).read().splitlines()
        )
    )


if __name__ == '__main__':
    app()
