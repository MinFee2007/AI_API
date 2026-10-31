import pinggy

def create_tunnel():
    try:
        # Create tunnels
        tunnel = pinggy.start_tunnel(forwardto="localhost:8000")

        # Print tunnels to screen
        print("\n" + "="*50)
        print("Successfully created a public link")
        print("Public URLs that can be used:")
        for url in tunnel.urls:
            print(f" - {url}")
        print("="*50 + "\n")
        print("Tunnel is running, CTRL + C to stop")

        # Keep the process running to maintain the tunnel connection
        tunnel.wait()

    except Exception as e:
        print(f"Error in creating a tunnel: {e}")

if __name__ == "__main__":
    create_tunnel()