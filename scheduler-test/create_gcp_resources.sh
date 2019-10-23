#!/bin/bash

set -e

TOPIC_NAME=pubsub-topic-test-scheduler
FUNCTION_NAME=subscription-functions-test-scheduler
SCHEDULER_NAME=scheduler-test

gcloud pubsub topics create $TOPIC_NAME --verbosity=debug

gcloud functions deploy $FUNCTION_NAME --runtime=python37 --trigger-topic=$TOPIC_NAME --entry-point=execute --memory=1024MB --verbosity=debug --timeout=540 -q				

gcloud scheduler jobs create pubsub $SCHEDULER_NAME --schedule='*/10 * * * *' --topic=$TOPIC_NAME --message-body='{}' --verbosity=debug
