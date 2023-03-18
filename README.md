# Docker + GitHub Actions CI/CD process

 - Branch protection enforced, all changes must be submit through Pull Request. 

 - CI tests used to build and run Dockers have been deployed.
 
 - CD tests used to deploy the Dockers to ECR repo have been deployed.

 - Docker1, Docker2, Docker3 folders are setup to push itself to corresponding private ECR repo once been modified.
 
 - Any changes to the above folders will trigger GitHub Action deployment (CD) tests, do not modify unless its ready to deploy.

