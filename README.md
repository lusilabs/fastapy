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
- [ ] token login endpoint
	- [ ] sqlite or postgres?
- [ ] rq-dashboard
- [ ] openseespy.. crossenv? .. build package (compile src code openseespy) locally on arm.

Goal is to deploy it to GCP free tier with K8s to see it in action.