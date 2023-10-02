#!/usr/bin/env python
import random
from typing import TYPE_CHECKING

import pytest
from deadnews_template_python._main import app
from deadnews_template_python.app import HEALTH, HELLO_WORLD, ITEMS
from starlette import status
from starlette.testclient import TestClient

if TYPE_CHECKING:
    from httpx import Response


@pytest.fixture()
def client() -> TestClient:
    return TestClient(app)


def test_read_root(client: TestClient) -> None:
    response: Response = client.get("/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == HELLO_WORLD


def test_read_health(client: TestClient) -> None:
    response: Response = client.get("/health")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == HEALTH


def test_read_items(client: TestClient) -> None:
    key, value = random.choice(list(ITEMS.items()))

    response: Response = client.get(f"/items/{key}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == value


def test_error(client: TestClient) -> None:
    response: Response = client.get("/error")

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR