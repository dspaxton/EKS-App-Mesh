#!/bin/bash
source cfvars
aws cloudformation --region $REGION create-stack --stack-name $CLUSTERNAME-ecs-fargate --template-body file://ecs.yaml --parameters ParameterKey=VPCID,ParameterValue=$VPC ParameterKey=PrivateSubnet1,ParameterValue=$PRIVATESUBNET1 ParameterKey=PrivateSubnet2,ParameterValue=$PRIVATESUBNET2 ParameterKey=PrivateSubnet3,ParameterValue=$PRIVATESUBNET3 ParameterKey=PrivateNamespace,ParameterValue=$NAMESPACE ParameterKey=VPCCIDR,ParameterValue=$VPCCIDR --capabilities CAPABILITY_IAM

echo "Waiting for ECS Fargate Stack to be deployed"

aws cloudformation --region $REGION wait stack-create-complete --stack-name $CLUSTERNAME-ecs-fargate


aws appmesh --region $REGION update-route --cli-input-json file://update-route.json
echo "Deployed and mesh configured"
