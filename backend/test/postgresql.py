import psycopg


def main():
    pg_url = "postgresql://{}:{}/{}?user={}&password={}".format(
        "212.129.252.187", 5432, "infra_auto", "postgres", "TX1hRq75fM3FTPYViNCh"
    )

    conn = psycopg.connect(pg_url)

    dbRes = conn.execute("SELECT 1")

    print(dbRes)


if __name__ == "__main__":
    main()
