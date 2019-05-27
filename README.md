# aws-chalice-echosvc
poc echo api using AWS chalice microservice framework. 

[AWS Chalice](https://chalice.readthedocs.io/en/latest/) is a microframework for writing serverless apps in python. It allows you to quickly create and deploy applications that use AWS Lambda. It provides:

* A command line tool for creating, deploying, and managing your app
* A decorator based API for integrating with Amazon API Gateway, Amazon S3, Amazon SNS, Amazon SQS, and other AWS services.
* Automatic IAM policy generation


## Command Line Options:

to create project:

    $ chalice new-project --profile _profile_ _projectname_

to deploy:

    $ chalice deploy --profile _profile_

to delete:

    $ chalice delete --profile _profile_

to test locally:

    $ chalice local

to create cli deployment cloudformation and zip files:

    $ chalice package _directoryName_

## Service paths:

    /

returns "hello world"

    /echo
    
returns client ip address    

    /rickroll

returns Never Gonna Give You Up (duh)

    /hello/{name}

returns "hello $name"

### References:

https://github.com/aws/chalice

https://chalice.readthedocs.io/en/latest/
