# Final project evidence capture

These scripts capture **real output** from a running environment; they do not
manufacture assessment evidence.

## REST CRUD evidence
Start the Flask service and PostgreSQL first, then run:

```bash
chmod +x scripts/capture-rest-evidence.sh
API_URL=http://localhost:8080 ./scripts/capture-rest-evidence.sh
```

It creates `rest-create-done`, `rest-list-done`, `rest-read-done`,
`rest-update-done`, and `rest-delete-done` with the request and actual
response for each operation.

## Docker and Kubernetes evidence
After building/loading the image and applying the Kubernetes manifests:

```bash
chmod +x scripts/capture-k8s-evidence.sh
./scripts/capture-k8s-evidence.sh
```

This creates `kube-images` and `kube-deploy-accounts`. The Kubernetes
Deployment expects an `accounts-db` Secret containing the database URI.

## Tekton evidence
After running the pipeline in your Tekton/OpenShift environment:

```bash
tkn pipelinerun list
tkn pipelinerun logs <PIPELINE_RUN_NAME> -f > pipelinerun.txt
```

Do not submit sample or placeholder output: use the actual command output from
your own running cluster.

## Screenshots and Kanban
The planning screenshots must be captured from the actual GitHub Projects
Kanban board after arranging the stories, estimates, labels, and sprint
assignments. The local scripts cannot create authentic screenshots of that
board or of an external Skills Network/OpenShift IDE.
