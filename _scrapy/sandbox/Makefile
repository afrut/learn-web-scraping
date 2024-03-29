# @ on the first command prevents make from echoing the command to stdout.
# && is a bash operator that executes the next command only if the previous is successful.
# Multi-line commands need to be escaped with backslash.
# Comments can exist inside targets but must escape newline with backslash.

clean:
	@# Remove all files and directories in outputs/ except .gitkeep \
	ls outputs | grep -v ".gitkeep" | xargs printf './outputs/%s\n' | xargs rm -rf

basics:
	@scrapy crawl basics --logfile outputs/basics.log

quotes:
	@scrapy crawl quotes -o outputs/quotes.jsonl -t jsonlines --logfile outputs/qutoes.log

crawlspider:
	@scrapy crawl crawlspider -o outputs/crawlspider.jsonl -t jsonlines --logfile outputs/crawlspider.log

checkip:
	@scrapy crawl checkip --logfile outputs/checkip.log

build:
	@docker build --tag scrapoxy \
		--build-arg scrapoxy_conf_path="${SCRAPOXY_CONF_PATH}" \
		- < Dockerfile

run_interactive:
	@docker run --interactive --tty \
		--name scrapoxy_tty \
		--mount type=bind,source="${SCRAPOXY_CONF_PATH}",destination="/scrapoxy/scrapoxy_conf.json",readonly \
		--entrypoint="/bin/bash" \
		scrapoxy

run:
	@docker run --detach \
		--name scrapoxy_server \
		--publish 8888:8888 \
		--publish 8889:8889 \
		--mount type=bind,source="${SCRAPOXY_CONF_PATH}",destination="/scrapoxy/scrapoxy_conf.json",readonly \
		scrapoxy scrapoxy start "/scrapoxy/scrapoxy_conf.json"

clean_docker:
	@docker kill scrapoxy_server;\
	docker rm -f scrapoxy_server;\
	docker rm -f scrapoxy_tty

# "scrapoxy start /scrapoxy/scrapoxy_conf.json"