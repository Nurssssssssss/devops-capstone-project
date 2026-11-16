"""
Flask application factory configuration and service initialization.
"""
import sys

from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

from service import config
from service.common import log_handlers

app = Flask(__name__)
app.config.from_object(config)

# Restrict cross-origin access to configured origins; '*' is not used.
CORS(app, resources={r"/accounts*": {"origins": app.config.get(
    "CORS_ORIGINS", ["http://localhost:3000"]
)}})

# Apply standard browser security headers. HTTPS redirection is disabled for
# local development; production should terminate TLS at the ingress/load balancer.
Talisman(
    app,
    force_https=app.config.get("TALISMAN_FORCE_HTTPS", False),
    content_security_policy={
        "default-src": ["'self'"],
        "object-src": ["'none'"],
        "frame-ancestors": ["'none'"],
    },
)

# Import routes after app creation to avoid circular imports.
from service import routes, models  # noqa: E402,F401
from service.common import error_handlers, cli_commands  # noqa: E402,F401

log_handlers.init_logging(app, "gunicorn.error")
app.logger.info("ACCOUNT SERVICE STARTING".center(70, "*"))

try:
    models.init_db(app)
except Exception as error:  # pylint: disable=broad-except
    app.logger.critical("%s: Cannot continue", error)
    sys.exit(4)

app.logger.info("Service initialized!")
