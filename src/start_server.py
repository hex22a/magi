import bjoern

from app import create_app

if __name__ == "__main__":
    app = create_app()
    config = {
        "host": "127.0.0.1",
        "port": 8888
    }

    print(f"Serving Falcon app at: {config['host']}:{config['port']}")
    bjoern.run(app, config['host'], config['port'])
