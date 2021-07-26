from flask import jsonify


def api_version():
    return (
        jsonify(
            {
                "version": {
                    "api": "0.1.0",
                },
            }
        ),
        200,
    )
