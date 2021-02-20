# Nexmo Forward SMS
Forward SMS from Virtual Nexmo Number to other phone Number

## Download project
git clone https://github.com/earguinarena/nexmo-forward-sms.git

## Install Environment
Install Serverless framework
```
npm install -g serverless
```

Install required Serverless packages
```
npm ci
```

## Deployment
```
sls deploy
```

## Setup Credentials

* Install Aws cli https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
* Configure https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
  
```
  aws configure 
```

## Configure Parameters
* Purchased Virtual Number
```
aws ssm put-parameter \
    --name "/vonage/virtual_number" \
    --type "String" \
    --value "value" \
    --overwrite
```

* Destination Number (without the + )
```
aws ssm put-parameter \
    --name "/vonage/destination_number" \
    --type "String" \
    --value "value" \
    --overwrite
```

* Api Key (from Nexmo settings, see below)
```
aws ssm put-parameter \
    --name "/vonage/api_key" \
    --type "String" \
    --value "value" \
    --overwrite
```

* Api Secret key (from Nexmo settings, see below)
```
aws ssm put-parameter \
    --name "/vonage/api_secret" \
    --type "String" \
    --value "value" \
    --overwrite
```


## Nexmo Configuration
Nexmo Settings https://dashboard.nexmo.com/settings

Configure 
* "Delivery receipts" : 
```https://<hex>.execute-api.<region>.amazonaws.com/dev/webhooks/inbound-sms```
* "HTTP method": POST-JSON 

Send Message to your virtual number Test it :)


## Optional - Develop Environment
```
virtualenv venv --python=python3 
source venv/bin/activate 
pip install flask boto3 vonage
```

## Optional - Run Mock
```
sls wsgi  serve
```