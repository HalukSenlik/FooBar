# FooBar

PreReq:
You need Python3.12 for this project.


Boilerplate for spinning up firestore and firebase functions emulator. To get started run:
`bash scripts/firebase_emulator.sh `

Then you should be able to curl the endpoint via:
`curl http://127.0.0.1:5001/foo-bar/us-central1/on_request_example`
response should be `Bar`

I also have this function in my `~/.zshrc` to help clean up:
```commandline
kill_emulator() {
    for port in 4003 9099 5001 8080 9199 4400 4500 9150 8081; do
        echo "Killing process on port $port..."
        # Find the PID using the port and kill it
        lsof -ti tcp:${port} | xargs kill -9
    done
    echo "All specified ports have been killed."
}


```
