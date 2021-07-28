from flask import jsonify, current_app


def api_version():
    return (
        jsonify(
            {
                "version": {
                    "api": "0.2.0",
                    "flask_env": current_app.config["FLASK_ENV"],
                    "debug": current_app.config["DEBUG"],
                },
            }
        ),
        200,
    )
