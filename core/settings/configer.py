from core.settings.receiver import Receiver


receiver = Receiver()

postgres_data = receiver.get_postgres_data()
redis_data = receiver.get_redis_data()

postgres_url = 'postgresql+asyncpg://{pg_user}:{pg_pass}@{pg_host}/{pg_name}'.format(**postgres_data)
redis_url = 'redis://{redis_host}:{redis_port}/{redis_name}'.format(**redis_data)
