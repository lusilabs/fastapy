# README
Complete scalable backend.
Dead-simple no-setup. KISS. DRY.

## TODO
how to solve storing results in folders? .yml files... .csv files
out files.. do I just dump everything back in the html call or give a link to an ephemereal bucket?
- pass in a string or a file that opensees will execute... all results will be put in a bucket. or a subset will be returned in the response.

- login/users
	via JWT, this will use postgrest in the background ?? too difficult?


- [ ] rq-dashboard
	- [ ] prod -- provide a (protected ?) view to dashboard (via FASTAPI?) admin needs to look at queue on prod.

- logs
	- [ ] prod -- gcp stderr or other hosted solution on production

- deploy
	- [ ] First deploy it with docker-compose.
	- [ ] then deploy it to GCP free tier with K8s to see it in action.
	- how to handle entrypoint and load balancer?
		- [ ] CI/CD ? gitlab ?