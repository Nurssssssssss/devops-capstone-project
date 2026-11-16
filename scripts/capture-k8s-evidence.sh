#!/usr/bin/env bash
# Capture Docker image and Kubernetes deployment evidence from a configured cluster.
set -euo pipefail
OUT_DIR="${OUT_DIR:-.}"
mkdir -p "$OUT_DIR"

docker image ls --no-trunc | tee "$OUT_DIR/kube-images"
kubectl get deployment,pods,replicasets,service -o wide | tee "$OUT_DIR/kube-deploy-accounts"

echo "For Tekton evidence, run:"
echo "  tkn pipelinerun list"
echo "  tkn pipelinerun logs <PIPELINE_RUN_NAME> -f > pipelinerun.txt"
