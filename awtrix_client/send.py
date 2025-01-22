import json
import base64
import requests
import click


esp_32_host = "http://192.168.1.100"
user_password = "admin:admin"
hashpass = base64.b64encode(user_password.encode())
hashpass = hashpass.decode()


@click.group()
def cli():
    pass


@cli.command()
@click.option("--message", "-m", required=True)
def message(message: str):
    response = requests.post(
        f"{esp_32_host}/api/notify",
        headers={"Authorization": f"Basic {hashpass}"},
        json={"text": message, "hold": True, "duration": 15},
    )
    print(response)


@cli.command()
def dismiss():
    response = requests.post(
        f"{esp_32_host}/api/notify/dismiss",
        headers={"Authorization": f"Basic {hashpass}"},
        json={},
    )
    print(response)


@cli.command()
def draw():
    response = requests.post(
        f"{esp_32_host}/api/notify",
        headers={"Authorization": f"Basic {hashpass}"},
        json={
            "draw": [
                {"dc": [28, 4, 3, "#FF0000"]},
                {"dr": [20, 4, 4, 4, "#0000FF"]},
                {"dt": [0, 0, "Hello", "#00FF00"]},
            ]
        },
    )
    print(response)


if __name__ == "__main__":
    cli()
