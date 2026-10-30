import requests

BASE_URL = "http://127.0.0.1:8000"

def test_endpoints():
    # 1. Test GET /
    print("--- Test Root Endpoint ---")
    res_root = requests.get(f"{BASE_URL}/")
    print("Status:", res_root.status_code)
    print("Response:", res_root.json())

    # 2. Test GET /health
    print("\n--- Test Health Endpoint ---")
    res_health = requests.get(f"{BASE_URL}/health")
    print("Status:", res_health.status_code)
    print("Response:", res_health.json())

    # 3. Test POST /predict (Input hợp lệ 1)
    print("\n--- Test Predict (Input 1) ---")
    payload1 = {"text": "I absolutely love learning FastAPI and AI!"}
    res_pred1 = requests.post(f"{BASE_URL}/predict", json=payload1)
    print("Status:", res_pred1.status_code)
    print("Response:", res_pred1.json())

    # 4. Test POST /predict (Input hợp lệ 2)
    print("\n--- Test Predict (Input 2) ---")
    payload2 = {"text": "This product was terrible and stopped working after two days."}
    res_pred2 = requests.post(f"{BASE_URL}/predict", json=payload2)
    print("Status:", res_pred2.status_code)
    print("Response:", res_pred2.json())

    # 5. Test Invalid Input (Xử lý lỗi)
    print("\n--- Test Invalid Input ---")
    payload_bad = {"text": ""}
    res_bad = requests.post(f"{BASE_URL}/predict", json=payload_bad)
    print("Status:", res_bad.status_code)
    print("Response:", res_bad.json())

if __name__ == "__main__":
    test_endpoints()