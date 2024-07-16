# CTFd for KPCTF

## What is CTFd for KPCTF?

CTFd for KPCTF is a CTF platform based on CTFd v3.4.0. It's once used to hold KPCTF which is a CTF competition in FAFU. It comes with everything you need to run a CTF and it's easy to customize with plugins and themes. Besides, it also integrates some plugins and adapts them to the current version.

## Addons

- theme
	- neon theme
- plugin
	- ctfd-whale
	- ctfd-matrix-scoreboard-plugin
	- ctfd-one-answer-challenge-plugin

## What is new?

In addition to adding the above plugins and themes, we have also added an Easter egg page and added some JS code to some pages, such as adding a countdown to the start and end of the competition.

## What is changes

Please note that we have changed the default theme to `neon` and modified some of the `core`'s built-in features to adapt to the current theme. To prevent the impact of the `core` theme, we have modified some of the code so that the `core` theme does not appear in the front-end options. We also do not recommend using this theme in this project.

We also modified the default font, etc. If you feel that the current font does not meet your aesthetic or reading preferences, you can replace the corresponding parts in the settings. Please refer to the official user manual for specific methods.

## Usage

1. Install dependencies: `pip3 install -r requirements.txt`.
2. Create docker swarm:  `docker swarm`.
3. Add node's label: `docker node update --label-add name=linux your_node_name`, please replace your_node_name with the real name, you can use `docker node ls` to see them.
4. Start container: `docker compose up -d` or `./docker-compose-linux-x86_64 up -d`.
5. Visit the site: `ip:8000`, and then completing setup.
6. Complete ctfd-whale's ip and others.
7. Add your competition and challenges. More to read offical user manual.
8. To stop id: `docker compose down` or `./docker-compose-linux-x86_64 down`.

