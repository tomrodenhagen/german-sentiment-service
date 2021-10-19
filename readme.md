Simple microservice to classify sentiment of german text snippets. 
Quick start (Prequisite: Installed docker) : 
1. cd into Repo: `` cd /path_to_repo/.../german-sentiment-service`` 
2. run into command line: `` docker-compose up``  to build and start service
3. Show docs with http://localhost:8001/docs in your favourite browser
4. Get sentiment for text "Ich liebe Cornelsen" with http://localhost:8001/?text=Ich%20liebe%20Cornelsen