from travel import create_app
import logging

if __name__=='__main__':
    n_app=create_app()
    n_app.run(debug=True)
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)
