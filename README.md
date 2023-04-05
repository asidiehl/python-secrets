# python-secrets
Secrets testing on a Python application

The application itself retrieves a list of CIDR ranges published for AWS services, filters them, and returns a filtered list. At the moment, it only retrieves ranges for the `GLOBAL` and `us-west-2` regions and the `AMAZON` and `EC2` services (since that's all I needed when I wrote this code). Eventually the application will prompt the user to select the desired services and regions for the filtered CIDR list.

In the interest of passing `bandit` security testing, the URL pointing to AWS's `ip-ranges.json` is being removed from the code. In order for this to work you'll need to download the `ip-ranges.json` file yourself from the [AWS documentation page](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ip-ranges.html) for AWS IP ranges. The code expects this file to exist at the root of the repository. An example `curl` command to achieve this would look like the following, run from the root of the repository.

```
curl https://ip-ranges.amazonaws.com/ip-ranges.json --output ip-ranges.json
```

The purpose of this repository is to catch secrets using an external tool that may be revealed in the future.
