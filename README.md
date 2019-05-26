# aws-chalice-echosvc
poc echo api using AWS chalice microservice framework

experiments with AWS Chalice: https://chalice.readthedocs.io/en/latest/

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
