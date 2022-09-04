import requests
import os

env_dist = os.environ
status={"queued","in_progress"}
taskamount=0
for i in status:
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer %s'%env_dist['REPO_TOKEN'],
    }

    params = {
        'status': '%s'%i,
    }

    response = requests.get('https://api.github.com/repos/xusenfa/autoscript/actions/workflows/flexget.yml/runs', params=params, headers=headers)
    taskamount+=response.json()["total_count"]
if taskamount>1:
    os.system('echo "RUN=shutdown" >> $GITHUB_ENV')
else:
    os.system('echo "RUN=run" >> $GITHUB_ENV')