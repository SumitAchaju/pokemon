from dotenv import find_dotenv, dotenv_values

env_path = find_dotenv()
config = dotenv_values(env_path)

DATABASE = {"URL": config["DATABASE_URL"]}
