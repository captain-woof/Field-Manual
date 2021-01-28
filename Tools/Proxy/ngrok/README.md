# ngrok

ngrok is a reverse proxy that creates a secure tunnel from a public endpoint to a locally running web service. ngrok captures and analyzes all traffic over the tunnel for later inspection and replay.

### What can I do with ngrok? (From [https://github.com/inconshreveable/ngrok](https://github.com/inconshreveable/ngrok))

    Expose any http service behind a NAT or firewall to the internet on a subdomain of ngrok.com
    Expose any tcp service behind a NAT or firewall to the internet on a random port of ngrok.com
    Inspect all http requests/responses that are transmitted over the tunnel
    Replay any request that was transmitted over the tunnel
    
### How to setup:

1. Signup at [ngrok.com](ngrok.com)
2. Follow the setup instructions shown in your dashboard to set up your auth token

### How to use:

- **Expose a local webserver:**

Once you've started a local webserver, fire up ngrok by pointing it to the port where your local server is running:

`./ngrok http 80`

The output will list a forwarding URL, which will point to your local server. You'll also see any active tunnels listed on the status page.

- **SSH to a Raspberry Pi/Any device:**

If you find yourself working with a Raspberry Pi or any similar network-connected device, it's useful to have fast and easy remote access. First, make sure to install ngrok on the device. Next, start a TCP tunnel on the device by listening on any port you choose:

`./ngrok tcp 22`

- **Expose a TCP based service running on port 1234**

`ngrok tcp 1234`

- **Inspect & replay requests:**

Visit `http://localhost:4040` once you have ngrok running to see live requests on your tunnels. Quickly inspect the headers and responses, or replay a request to speed up your development process.
