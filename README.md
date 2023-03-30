# python-secrets
Secrets testing on a Python application

The application itself retrieves a list of CIDR ranges published for AWS services, filters them, and returns a filtered list. At the moment, it only retrieves ranges for the `GLOBAL` and `us-west-2` regions and the `AMAZON` and `EC2` services (since that's all I needed when I wrote this code), but will eventually prompt the user to select the desired services and regions for the filtered CIDR list.

The purpose of this repository is to catch secrets using an external tool that may be revealed in the future.