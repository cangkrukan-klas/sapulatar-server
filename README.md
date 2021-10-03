# sapulatar-server

## How to start development server
1. Setup your virtualenv

    Example: 

    ```
    $ python -m virtualenv venv
    $ source venv/bin/activate
    ```
3. Install required dependencies
    ```
    $ python setup.py develop
    ```
4. Start development server
    ```
    $ FLASK_APP=sapulatarserver FLASK_ENV=development flask run
    ```
