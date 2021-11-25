# Serverless Shopping Cart Microservice

## Automatically deploy backend and frontend using Amplify Console


[Create a new personal access token](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line) 
on GitHub. 
Amplify will need this to access your repository. The token will need the “repo” OAuth scope.

Set environment variables:
```bash
export GITHUB_REPO=https://github.com/<your-github-username>/aws-serverless-shopping-cart
export GITHUB_BRANCH=master  # Or whichever branch you wish to track
export GITHUB_OAUTH_TOKEN=<github personal access token>
```

Create the Amplify console application, which will provide basic continuous deployment for your Github repository: 
``` bash
make amplify-deploy  # Creates amplify console application
```

Go to the [AWS Amplify console](https://console.aws.amazon.com/amplify/home), then click on "CartApp" and "run build". 
This will deploy both the frontend and backend:
![Amplify Console](./images/AmplifyConsoleScreen.png)

### Collecting the database endpoints
- Goto `dynamodb` in the aws console
- Goto `tables` in the left menu to find the table whose name starts with **lambda-sample-shoopingcart**
- Create a **backup** of this (to help restore after fault injection)
    - Goto `Backups` in the left menu
    - Select create backup (on demand)
    - Select the above table and give the backup a proper name

### Clean Up
- Delete the CloudFormation stacks created by this project. One is named "CartApp", and then there are 3 with names 
starting with **aws-serverless-shopping-cart-**.
- Delete the backup (if created) for the dynamodb