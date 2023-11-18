# @ on the first command prevents make from echoing the command to stdout.
# && is a bash operator that executes the next command only if the previous is successful.
# Multi-line commands need to be escaped with backslash.
# Comments can exist inside targets but must escape newline with backslash.

all: basics quotes crawlspider

clean:
	@# Remove all files and directories in outputs/ except .gitkeep \
	ls outputs | grep -v ".gitkeep" | xargs printf './outputs/%s\n' | xargs rm -rf

crawl:
	@scrapy crawl basics && \
	scrapy crawl quotes -o outputs/quotes.jsonl

basics:
	@scrapy crawl basics

quotes:
	@scrapy crawl quotes -o outputs/quotes.jsonl

crawlspider:
	@scrapy crawl crawlspider -o outputs/crawlspider.jsonl