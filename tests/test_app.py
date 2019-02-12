import json
from pathlib import Path

import pytest


@pytest.fixture(scope='module')
def flask_app():
    from gj_union.flask_api import create_app
    return create_app()


@pytest.fixture(scope='module')
def client(flask_app):
    with flask_app.test_client() as client:
        yield client


@pytest.fixture(scope='module')
def post_json():
    return json.loads(Path('tests/post.json').read_text())


@pytest.fixture(scope='module')
def response_json():
    return json.loads(Path('tests/response.json').read_text())


def test_post(client, post_json, response_json):
    response = client.post('/', json=post_json)
    print(response)
    assert response.status_code == 200
    assert 'type' in response.json
    assert 'coordinates' in response.json
    assert response.json == response_json
