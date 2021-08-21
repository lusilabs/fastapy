# README
Complete scalable backend.
Dead-simple no-setup. KISS. DRY.

access swagger docs here/login
```
http://localhost:8888/docs
```

jobs dashboard
```
http://localhost:9181
```

## TODO
how to solve storing results in folders? .yml files... .csv files
out files.. do I just dump everything back in the html call or give a link to an ephemereal bucket?

- login/users
	via JWT, this will use postgrest in the background ?? too difficult?

-
- pass in a string or a file that opensees will execute... all results will be put in a bucket. or a subset will be returned in the response.
- store results in google cloud buckets that expire in like a week
- [ ] prod -- gcp stderr or other hosted solution on production
- [ ] prod -- provide a (protected ?) view to dashboard (via FASTAPI?) admin needs to look at queue on prod.
- deploy
	- [ ] First deploy it with docker-compose.
	- [ ] then deploy it to GCP free tier with K8s to see it in action.
	- how to handle entrypoint and load balancer?
		- [ ] CI/CD ? gitlab ?