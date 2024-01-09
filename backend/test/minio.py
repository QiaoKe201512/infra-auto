import io

from minio import Minio


def main():
    client = Minio("212.129.252.187:9000",
                   access_key="fj6TR6KuwueNZMyAdZQX",
                   secret_key="2Y9lZAPVKfP8LkL07DwL6WR9uQIKuq5w4IKqvSPI",
                   secure=False
                   )

    res = client.put_object("infra-auto", "test.txt", io.BytesIO(b"hello"), 5)
    print(res)


if __name__ == "__main__":
    main()
