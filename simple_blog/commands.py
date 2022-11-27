# -*- coding: utf-8 -*- 
from simple_blog.exts import db
from simple_blog import app
from simple_blog.models import User, Blog
import click


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        click.echo('Drop table first.')
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(drop, username, password):
    """Create admin user."""
    if drop:
        click.echo('Drop table first.')
        db.drop_all()
    db.create_all()

    user = User.query.filter_by(user_name=username).first()
    if user is not None:
        click.echo('Admin is existed, updating password...')
        user.user_name = username
        user.set_password(password)
    else:
        click.echo('Creating user...')
        user = User(user_name=username)
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('Done.')

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def forge(drop):
    """forge the test data"""
    if drop:
        click.echo('Drop table first.')
        db.drop_all()
    db.create_all()

    name = 'Crea'

    blogs = [
        {'title': 'the first blog', 'content': 'hello world!!'},
        {'title': 'the second blog', 'content': 'hello world again!!'}
    ]

    db.session.add(User(user_name=name))
    for blog in blogs:
        db.session.add(Blog(title=blog['title'], content=blog['content']))
    db.session.commit()
    click.echo('Done.')