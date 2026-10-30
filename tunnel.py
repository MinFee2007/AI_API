import pinggy

def create_tunnel():
    try:
        tunnel = pinggy.start_tunnel(forwardto="localhost:8000")

        print("\n" + "="*50)
        print("Successfully created a public link")
        print("Public URLs that can be used:")
        for url in tunnel.urls:
            print(f" - {url}")
        print("="*50 + "\n")
        print("Tunnel is running, CTRL + C to stop")

        tunnel.wait()

    except Exception as e:
        print(f"Error in creating a tunnel: {e}")

if __name__ == "__main__":
    create_tunnel()