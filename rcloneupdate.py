import requests
from base64 import b64encode,b64encode
from nacl import encoding, public
import os

env_dist = os.environ
rcloneconfvalue=""
publickey="TZKoEY+pjpuiyC/T42DBWuS1Oc160qr3T4Xt/tPzSTQ="
with open('/home/runner/.config/rclone/rclone.conf', 'r') as f:
    rcloneconfvalue=b64encode(f.read().encode('utf-8'))
rcloneconfvalue=rcloneconfvalue.decode('UTF-8')


headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer %s'%env_dist['REPO_TOKEN'],
    'Content-Type': 'application/x-www-form-urlencoded',
}

def encrypt(public_key: str, secret_value: str) -> str:
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")

sendvalue=encrypt(publickey,rcloneconfvalue)
data = '{"encrypted_value":"%s","key_id":"568250167242549743"}'%sendvalue


response = requests.put('https://api.github.com/repos/xusenfa/autoscript/actions/secrets/RCLONECONF', headers=headers, data=data)

print(response.status_code)