# ASCII Curl Animation

This serves the animation as a streaming HTTP response, so a Windows CMD/PowerShell terminal can play it with only `curl`.

## Deploy on Render

1. Put this folder in a GitHub repository.
2. In Render, create a **Web Service** from that repository.
3. Render will use `render.yaml` automatically.
4. After deployment, copy the service URL.

## Run from CMD

```cmd
curl -N https://vijay-il4v.onrender.com/ascii
```

Stop with `Ctrl+C`.

`-N` is important because it tells curl not to buffer the streamed animation.
