import dash_app_factory
import flask_app_factory

if __name__ == '__main__':
    dash_app_factory.dash_app.run_server(debug=True,port=8080,host='127.0.0.1')