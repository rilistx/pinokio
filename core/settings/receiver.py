from environs import Env


class Receiver:
    env = Env()
    env.read_env('.env')

    @classmethod
    def get_postgres_data(cls) -> dict:
        return {
            'pg_name': cls.env.str("POSTGRES_DB"),
            'pg_user': cls.env.str("POSTGRES_USER"),
            'pg_pass': cls.env.str("POSTGRES_PASSWORD"),
            'pg_host': cls.env.str("POSTGRES_HOST"),
        }

    @classmethod
    def get_redis_data(cls) -> dict:
        return {
            'redis_name': cls.env.str("REDIS_NAME"),
            'redis_host': cls.env.str("REDIS_HOST"),
            'redis_port': cls.env.str("REDIS_PORT"),
        }
