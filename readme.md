Simple microservice to classify sentiment of german text snippets. 
Quick start (Prequisite: Installed docker) : 
1. cd into Repo: `` cd /path_to_repo/.../german-sentiment-service`` 
2. run into command line: `` docker build .``  
3. run into command line: `` docker run german-sentiment-service-test``  to check if everythings fine
4. run into command line: `` docker run german-sentiment-service``  to start service
5. Show docs with http://localhost:8001/docs in your favourite browser
6. Get sentiment for text "Ich liebe Cornelsen" with http://localhost:8001/?text=Ich%20liebe%20Cornelsen