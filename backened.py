from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

coupons = ["COUPON123", "DISCOUNT50", "SALE2025", "FREEGIFT", "SAVE20"]
claimed_coupons = []
ip_tracking = {}

@app.route('/claim_coupon', methods=['POST'])
def claim_coupon():
    user_ip = request.remote_addr
    print(f"Received request from IP: {user_ip}")

    if user_ip in ip_tracking:
        print(f"IP {user_ip} has already claimed a coupon.")
        return jsonify({"message": "You have already claimed a coupon!"}), 429

    if not coupons:
        print("No coupons available.")
        return jsonify({"message": "No coupons available"}), 404

    coupon = coupons.pop(0)
    claimed_coupons.append(coupon)
    ip_tracking[user_ip] = coupon
    print(f"Coupon {coupon} claimed by IP {user_ip}")

    return jsonify({"message": "Coupon claimed successfully!", "coupon": coupon})

@app.route('/admin/coupons', methods=['GET'])
def get_coupons():
    return jsonify({"available": coupons, "claimed": claimed_coupons})

if __name__ == '__main__':
    app.run(debug=True)
