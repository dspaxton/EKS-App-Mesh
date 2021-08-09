#!/bin/bash
source cfvars
cat << EOF | kubectl apply -f -
apiVersion: v1
kind: Namespace
metadata:
  name: jobs
---
apiVersion: batch/v1
kind: Job
metadata:
  # Unique key of the Job instance
  name: loaddb
  namespace: jobs
spec:
  template:
    metadata:
      name: loaddb
    spec:
      containers:
      - name: mongoload
        image: mongo
        env:
        - name: DOCDBENDPOINT
          value: ${DOCDBENDPOINT}
        - name: DocumentDBPassword
          value: ${DocumentDBPassword}
        - name: DocumentDBUsername
          value: ${DocumentDBUsername}
        command: ["/bin/bash","-c","apt-get update && \
        apt-get install curl && \
        curl 'https://api.mockaroo.com/api/57f56900?count=1000&key=57c07360' -o products.json && \
        echo $DOCDBENDPOINT && \
        mongoimport --host ${DOCDBENDPOINT} --drop -d products -c items --jsonArray -u ${DocumentDBUsername} -p ${DocumentDBPassword} products.json
        "]
        # command: ["/bin/bash","-c","yum -y update"]
        
      # Do not restart containers after they exit
      restartPolicy: Never
EOF
