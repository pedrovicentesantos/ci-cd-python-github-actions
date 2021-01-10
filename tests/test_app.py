import pytest
from flask import template_rendered

from src.app import app


@pytest.fixture
def test_client():
    flask_app = app

    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture
def captured_templates(test_client):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


def test_home_endpoint(test_client, captured_templates):
    test_client.get('/')

    assert len(captured_templates) == 1

    template, context = captured_templates[0]

    assert template.name == 'index.html'

    assert 'image_url' in context
    assert 'title' in context
    assert 'cat' in context['image_url']
    assert context['title'] == 'Cat'


def test_dog_endpoint(test_client, captured_templates):
    test_client.get('/dog')

    assert len(captured_templates) == 1

    template, context = captured_templates[0]

    assert template.name == 'index.html'

    assert 'image_url' in context
    assert 'title' in context
    assert 'dog' in context['image_url']
    assert context['title'] == 'Dog'
