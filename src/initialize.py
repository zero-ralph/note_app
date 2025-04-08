import argparse
import toml
import uvicorn
from src.main import app
from src.config.database import configure_database
from src.config.settings import Settings


def main():
    parser = argparse.ArgumentParser(prog="NoteTagApp", description="Exam")
    parser.add_argument('-s', '--settings', required=True, help="Path to the toml settings file ")
    
    args = parser.parse_args()

    settings = Settings.from_toml(args.settings)
    configure_database(settings)
    return settings

if __name__ == "__main__":
    settings = main()
    uvicorn.run(app, port=settings.general.port)
