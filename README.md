# README
Dead-simple no-setup. KISS. DRY.
Complete scaleable backend.
##
Make it dead simple.

`api/token/`
`api/models/` CRUD for running, creating models
`api/jobs/`

## TODO
- billing.. how to charge a service?
	- let users buy credits thru a simple web-based checkout process
	- curl -X `/credits`
	- let users buy subs for unlimited credits
	- stripe payment links https://www.swyx.io/stripe-payment-links/

- [ ] rq-dashboard
	- [ ] prod -- view result data of jobs? -- possible?
	- [ ] prod -- provide a protected view to dashboard via FASTAPI? admin needs to look at queue in

- logs
	- [ ] dev -- kibana + elasticsearch locally EKS
	- [ ] prod -- gcp stderr or other hosted solution on production

- [ ] postgres with sqlalchemy
	- [ ] automated migrations (alembic) with pydantic?
	- [ ] sharded + multi-tenant
		- [ ] sqlalchemy horizontal sharding
	- [ ] read-only replicas
	- [ ] test failovers

- [ ] hasura
	- [ ] https://hasura.io/docs/latest/graphql/core/guides/sample-apps/index.html
	- [ ] auth and current jwt implementation
	- [ ] roles based queries+mutations
	- [ ] set up soft deletes

- [ ] deploy
	- [ ] First deploy it with docker-compose.
	- [ ] Goal is to deploy it to GCP free tier with K8s to see it in action.
	- how to handle entrypoint and load balancer?
		- [ ] CI/CD with GitLab ?

- [ ] develop a Skylab.
	- use apollo ? consume hasura schemas instantly: tables on the frontend
	- JWT login
	- Next.js to its fullest. fast SPA with SSR.
	- very easy html https://devdojo.com/tails/app + EMMET