"""
REST API routes for the Customer Accounts microservice.
"""
from flask import abort, jsonify, make_response, request, url_for

from service import app
from service.common import status
from service.models import Account


@app.route("/health", methods=["GET"])
def health():
    """Return service health."""
    return jsonify(status="OK"), status.HTTP_200_OK


@app.route("/", methods=["GET"])
def index():
    """Return API metadata."""
    return jsonify(name="Account REST API Service", version="1.0"), status.HTTP_200_OK


def check_content_type(media_type="application/json"):
    """Reject requests that do not use the expected media type."""
    if request.mimetype != media_type:
        abort(
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            description=f"Content-Type must be {media_type}",
        )


@app.route("/accounts", methods=["POST"])
def create_accounts():
    """Create a customer account."""
    check_content_type()
    account = Account()
    account.deserialize(request.get_json(silent=True))
    account.create()
    response = make_response(jsonify(account.serialize()), status.HTTP_201_CREATED)
    response.headers["Location"] = url_for("read_account", account_id=account.id)
    return response


@app.route("/accounts", methods=["GET"])
def list_accounts():
    """List all customer accounts."""
    accounts = [account.serialize() for account in Account.all()]
    return jsonify(accounts), status.HTTP_200_OK


@app.route("/accounts/<int:account_id>", methods=["GET"])
def read_account(account_id):
    """Read one customer account."""
    account = Account.find(account_id)
    if account is None:
        abort(status.HTTP_404_NOT_FOUND, description="Account not found")
    return jsonify(account.serialize()), status.HTTP_200_OK


@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    """Update an existing customer account."""
    check_content_type()
    account = Account.find(account_id)
    if account is None:
        abort(status.HTTP_404_NOT_FOUND, description="Account not found")
    account.deserialize(request.get_json(silent=True))
    account.id = account_id
    account.update()
    return jsonify(account.serialize()), status.HTTP_200_OK


@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    """Delete an existing customer account."""
    account = Account.find(account_id)
    if account is None:
        abort(status.HTTP_404_NOT_FOUND, description="Account not found")
    account.delete()
    return "", status.HTTP_204_NO_CONTENT
