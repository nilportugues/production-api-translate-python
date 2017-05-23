# 1. Installation and running
 
## 1.1. Development

Meet the requirements: 

```bash
sudo apt-get install -y python python-pip python-virtualenv 
```

Run the following script to get you started in no time:

```bash
chmod +x dev.sh
./dev.sh
```
This will start the Flask framework listening on `127.0.0.1:8080` .

## 1.2. Production

Generate the build: 

- cd translate_api
- python setup.py sdist
- move the resulting tarball to the project's root directory.
- modify the docker-compose path.

Use the docker container.
 
 
# 2. API 

- **API Responses**: Uses `hal+json` standards.
- **API Error Responses**: Uses `vnd+error` error response standard.
- **Documentation**: Uses Swagger (OpenAPI)

## 2.1 Documentation: 

 - **Swagger UI**: http://127.0.0.1:8080/api/
 - **Swagger.json**: http://127.0.0.1:8080/api/swagger.json
 
## 2.2 Methods

 - [GET] http://127.0.0.1:8080/api/text/languages
 - [POST] http://127.0.0.1:8080/api/text/detect
 - [POST] http://127.0.0.1:8080/api/text/translate
 
# 3. Framework:

API has been written in Python (2.7) and uses the Flask-RESTful framework.
 