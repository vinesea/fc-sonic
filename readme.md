# SONIC

- 部署

```
export imageUrl="registry-intl.cn-hongkong.aliyuncs.com/k3s-server/fc-sonic:$(date +%F-%H-%M-%S)"

s deploy -t ./s.yaml -a guoji-access --use-local -y
```