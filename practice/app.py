from decimal import Decimal, ROUND_HALF_UP

from flask import Flask, jsonify, request


def calculate_total(subtotal_cents: int, discount_percent: int) -> int:
    """Implement the integer-cent pricing rule from Session 3."""
    sub_dec = Decimal(str(subtotal_cents))
    disc_dec = Decimal(str(discount_percent))
    multiplier = Decimal(1) - (disc_dec / Decimal(100))
    raw_total = sub_dec * multiplier
    return int(raw_total.quantize(Decimal(1), rounding=ROUND_HALF_UP))


class InMemoryOrderStore:
    """Implement save, find and count for an isolated in-memory store."""

    def __init__(self):
        self.orders = {}

    def save(self, order_id: str, order_data: dict):
        self.orders[order_id] = order_data

    def find(self, order_id: str):
        return self.orders.get(order_id)

    def count(self):
        return len(self.orders)


def create_app(store=None) -> Flask:
    app = Flask(__name__)
    if store is None:
        store = InMemoryOrderStore()

    @app.route('/orders', methods=['POST'])
    def create_order():
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({"error": {"code": "invalid_value"}}), 400

        if 'subtotal_cents' not in data or 'discount_percent' not in data:
            return jsonify({"error": {"code": "missing_field"}}), 400

        subtotal = data['subtotal_cents']
        discount = data['discount_percent']

        if (
            not isinstance(subtotal, (int, float))
            or isinstance(subtotal, bool)
            or not isinstance(discount, (int, float))
            or isinstance(discount, bool)
        ):
            return jsonify({"error": {"code": "invalid_value"}}), 400

        if subtotal < 0 or discount < 0 or discount > 100:
            return jsonify({"error": {"code": "invalid_value"}}), 400

        try:
            total_cents = calculate_total(int(subtotal), int(discount))
        except (ValueError, TypeError):
            return jsonify({"error": {"code": "invalid_value"}}), 400

        order_id = f"ord-{store.count() + 1}"
        order_data = {
            "id": order_id,
            "subtotal_cents": subtotal,
            "discount_percent": discount,
            "total_cents": total_cents,
        }
        store.save(order_id, order_data)
        return jsonify(order_data), 201

    @app.route('/orders/<order_id>', methods=['GET'])
    def get_order(order_id):
        order = store.find(order_id)
        if not order:
            return jsonify({"error": {"code": "not_found"}}), 404
        return jsonify(order), 200

    return app