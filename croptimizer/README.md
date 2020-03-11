## Croptimizer server

`pip install flask`

`bash start_api_server.sh`

spins up a server at `localhost:5000`

test: `curl --url http://127.0.0.1:5000/ -X POST -H "Content-Type: application/json" --data '{"oid":"12341234"}'`

response =>`{"oid":"12341234"}`