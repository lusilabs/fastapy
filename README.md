# README
Complete scalable backend.
Dead-simple no-setup. KISS. DRY.
## Swagger view endpoints

`api/token/`
`api/models/` CRUD for running, creating models
`api/jobs/`

## TODO
- [ ] rq-dashboard
	- [ ] prod -- view result data of jobs? -- possible?
	- [ ] prod -- provide a protected view to dashboard via FASTAPI? admin needs to look at queue in

- logs
	- [ ] dev -- kibana + elasticsearch locally EKS
	- [ ] prod -- gcp stderr or other hosted solution on production

- [ ] deploy
	- [ ] First deploy it with docker-compose.
	- [ ] Goal is to deploy it to GCP free tier with K8s to see it in action.
	- how to handle entrypoint and load balancer?
		- [ ] CI/CD with GitLab ?