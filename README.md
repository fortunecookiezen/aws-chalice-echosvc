# aws-chalice-echosvc
poc echo api using AWS chalice microservice framework

experiments with AWS Chalice: https://chalice.readthedocs.io/en/latest/

to create project:

    $ chalice new-project --profile _profile_ _projectname_

to deploy:

    $ chalice deploy --profile _profile_

to delete:

    $ chalice delete --profile _profile_

to test locally:

    $ chalice local
Service paths:

    /

returns "hello world"

    /echo
    
returns client ip address    

    /rickroll

returns Never Gonna Give You Up (duh)

    /hello/{name}

returns "hello $name"
