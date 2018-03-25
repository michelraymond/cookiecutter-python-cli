import click as ck


@ck.command()
@ck.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@ck.argument('name', default='world', required=False)
def main(name, as_cowboy):
    """{{ cookiecutter.project_short_description }}"""
    greet = 'Howdy' if as_cowboy else 'Hello'
    ck.echo('{0}, {1}.'.format(greet, name))
