# BridgeNet Payment Site

## Project Summary

This is a standalone service that customer service reps can use to complete payments made to BridgeNet via our payment API.

## Development Setup

### Prerequisites

- Python 3.8 (should be available at command line as `python3.8`)
- Postgres Server (installed and running locally)
- An SSH Key configured to use with your GitHub account, which has access to the pronym-inc organization.

### Getting environment setup
You should be able to get started with a few commands.

```
$ git clone git@github.com:pronym-inc/bridgenet_payment.git
Cloning into bridgenet_payment ...
...
$ cd bridgenet_payment
$ install/setup.sh
Creating database...
...
```

### Running the web server
A `manage.py` script is provided in the root of the directory which can be used for interacting with the Django application.
To run the webserver:
```
$ ./manage.py runserver
```

### Running tests
##### Unit Tests
```
$ venv/bin/pytest bridgenet_payment/tests
```
##### Integration Tests
```
$ venv/bin/pytest bridgenet_payment/integration_tests
```