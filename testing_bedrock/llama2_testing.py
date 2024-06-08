import os
import json
import boto3
import sys

bedrock=boto3.client(service_name="bedrock-runtime")

prompt_data="""
Act as a dictionary  and write a meaning of that  word  intelligent """

payload={
    "prompt":"[INST]"+ prompt_data +"[/INST]",
    "max_gen_len":512,
    "temperature":0.3,
    "top_p":0.9
}

body=json.dumps(payload)
model_id="meta.llama2-70b-chat-v1"
response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body=json.loads(response.get("body").read())
repsonse_text=response_body['generation']
print(repsonse_text)