# Things you'll need to do 

## Sign up for Azure Free

[Sign up right here](https://azure.microsoft.com/en-us/free/)

You'll get a $200 credit, so don't worry about losing any cash. Furthermore, we'll be using many free features at low scale

## Download Chocolatey

[Follow the instructions](https://chocolatey.org/install) to install Chocalatey. It's like Brew, but worse.


## Download Azure CLI + AZ Login

Now, install the Azure

```
$ choco install azure-cli
```

Once that works, just run this 

```
$ az login
```

It'll take you to a browser and then you'll be able to put the rest together 

## Terraform Download and Init

Download terraform via chocalatey
```
$ choco install terraform
```

Then, navigate to the infra folder and terraform init 

```
$ terraform init
```

Once that's gone smoothly, create your resources and we're off and running: 

``` 
$ terraform apply
```


With all of this created, our producing logic lives within the `app/client.py` and our consumption logic lies within the `app/consumer.py`

Our simple FE client lives within `simple-react-full-stack/`. You'll need to ensure that your environment variables, database networking and database tables are all set up to make full use of this.


#### Confluent

You'll need to head to the confluent website and set up your own cluster. I didn't put in the work to terraformize it but i left a skeleton file that shouldn't be too hard to implement

