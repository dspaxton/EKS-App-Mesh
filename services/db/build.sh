source ../../setup/cfvars
sed  "s/ENDPOINT/$DOCDBENDPOINT/" app.template > app.py
sed  -i "s/USERNAME/$DocumentDBUsername/" app.py
sed  -i "s/PASSWORD/$DocumentDBPassword/" app.py
docker build -t $ACCOUNTNUMBER.dkr.ecr.$REGION.amazonaws.com/$(basename $PWD) .
docker push $ACCOUNTNUMBER.dkr.ecr.$REGION.amazonaws.com/$(basename $PWD)
