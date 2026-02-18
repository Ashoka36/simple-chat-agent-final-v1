# Simple Chat Agent

This is a simple Chat Agent built with Flask that can be hosted on Render.

## Deployment on Render

1. Fork this repository.
2. Go to [Render](https://render.com/); log in and create a "new Blueprint".
   - Or, create a "new Web Service" and select this repo.
3. Render will automatically detect the configuration from `render.yaml`.
4. Wait for the build and deployment to finish.

## Hpw to Use

Once deployed, you can talk to the agent by sending a POST request to the `/chat` endpoint:

```shell
curl -X POST https://your-app-name.onrender.com/chat \
    -H "Content-Type: application/json" \
    -d '{"message": "hello"}'
```

Response:
```json
{ "response": "Hi! How can I help you today?" }
```
