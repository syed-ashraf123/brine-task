Project README
Below, you'll find essential information on the project structure and how to run Docker files, deployments, and services.

Project Structure

## Codes Folder: 
Contains all the code files for the project.

## Test Folder: 
Includes test files and suites for ensuring the reliability of the code.

## Infra Folder: 
Holds infrastructure-related files and configurations.
Running Docker

To run any Docker file, use the following command:

## sudo docker compose up


Deployments
Deployments are orchestrated using Kubernetes. To apply a deployment configuration, use the following command:

## kubectl apply -f deployment-_.yaml
Replace deployment-_.yaml with the specific deployment configuration file you want to apply. 

Services
For running services, apply the service configuration using the following command:

## kubectl apply -f service-_.yaml
Replace service-_.yaml with the specific service configuration file you want to apply. 

Thanks
