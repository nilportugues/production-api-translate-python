# 1. Installation and running
 
## 1.1. Development

Run the following script to get you started in no time:

```bash
chmod +x dev.sh
./dev.sh
```
This will start the Flask framework listening on `localhost:5000` .

## 1.2. Production

Use the docker container.
 
# 2. API 

- **API Responses**: Uses `hal+json` standards.
- **API Error Responses**: Uses `vnd+error` error response standard.
- **Documentation**: Uses Swagger (OpenAPI)

## 2.1 Documentation: 

 - **Swagger UI**: http://localhost:5000/api/
 - **Swagger.json**: http://localhost:5000/api/swagger.json
 
## 2.2 Methods

 - [GET] http://localhost:5000/api/text/languages
 - [POST] http://localhost:5000/api/text/detect
 - [POST] http://localhost:5000/api/text/translate
 
# 3. Framework:

API has been written in Python (2.7) and uses the Flask-RESTful framework.
 
**Documentation**: http://flask-restplus.readthedocs.io

## Dockerize it:
- https://github.com/juanjbrown/flask-nginx-gunicorn-docker-sample