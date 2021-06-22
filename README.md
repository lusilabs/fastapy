# fem-api
Uses opensees under the hood to build FEM models.

## FastAPI
Make it dead simple.

`api/token/`
`api/models/` CRUD for running, creating models
`api/jobs/`


## Reference (Docs) Quickstart

```
{
	"options": {
		"validate_input": false
	},
	"functions" : {

	},
	"model": {
		...
	},

}

```

## TODO
merge branches.
- [ ] frontend
	- [ ] best option? nextjs?.. easily deployable. a way for users to sign in, start jobs and PAY.

- billing.. how to charge a service?
	- give ui + stripe

- [ ] rq-dashboard
	- [ ] view result data of jobs? --possible?
	- [ ] provide a protected view to dashboard via FASTAPI?

- logs
	- [ ] kibana + elasticsearch

- [ ] postgres and automated migrations
	- [ ] sharded + multi-tenant
		- [ ] sqlalchemy horizontal sharding
	- [ ] test failovers
	- [ ] read-only replicas

- [ ] dask and multi-processing

- [ ] deploy
	- [ ] First deploy it with docker-compose.
	- [ ] Goal is to deploy it to GCP free tier with K8s to see it in action.