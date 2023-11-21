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