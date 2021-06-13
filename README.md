0xa92cec6a3e2d2796044b7002a359ecdc3aa157ae

https://gist.githubusercontent.com/ralph-pichler/3b5ccd7a5c5cd0500e6428752b37e975/raw/aa576d6d28b523ea6f5d4a1ffb3c8cc0bbc2677f/cashout.sh


https://goerli.infura.io/v3/59f4c639ec4941548964d3ab772f593b


apt-get update -y && apt-get install docker -y && apt-get install docker-compose -y





docker run -it --rm erlang /bin/bash
- docker system prune

删除所有镜像

- docker rmi $(docker images -q)

杀死所有正在运行的容器
- docker kill $(docker ps -a -q)
删除所有已经停止的容器
- docker rm $(docker ps -a -q)
删除所有未打 dangling 标签的镜像
c docker rmi $(docker images -q -f dangling=true)


https://portswigger.net/burp/communitydownload
https://www.paterva.com/web7/community/community.php
https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#



sprinkle 0xa92cec6a3e2d2796044b7002a359ecdc3aa157ae
--swap-endpoint wss://mainnet.infura.io/ws/v3/59f4c639ec4941548964d3ab772f593b

bee-windows-amd64>bee.exe start --config bee-default.yaml --swap-endpoint wss://goerli.infura.io/ws/v3/59f4c639ec4941548964d3ab772f593b
                                  
docker run --name chiaok -v /temp:/temp -d ghcr.io/chia-network/chia:latest

docker run --net=host -v /run/media/yangmi/chia:/temp -d ghcr.io/chia-network/chia:latest


docker exec -it chiaok venv/bin/chia plots create -k 32 -f b7be10ac7eb05fbf27af6153606f5ff5469141fd5417aaa8fa3b225cc8d41a6ab986749e5a50ea09b502777b47d0c6a4 -p a541438b8f42e99666bdfa3a7fbf89b6cfdc9878ece814b4a2256fcce144896b5360d8670da323db8236440cd6d4f1eb -b 15000 -r 8 -u 128 --exclude_final_dir -t /temp -d /temp


0x1a9dccc03d3762a597e517957bc436737d6a3c22



clef-signer-enable: false
data-dir: D:/swarm
swap-enable: true
swap-endpoint: http://rpc.slock.it/goerli
verbosity: trace
welcome-message: "okokoko"
debgu-api-enable: true

