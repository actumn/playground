#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include "kusearch_process.h"

static int pipes[2];

void* process(void *arg);
void print_result();

int main(int argc, char* argv[])
{
	/* init arguments */
	if(argc < 4 || atoi(argv[2]) < 1) {
		printf("Usage: ./search path processes keyword 1 2 3 \n");
		exit(1);
	}
	file = argv[1];
	processCount = atoi(argv[2]);
	keywordCount = argc - 3;
	keywords = argv + 3;


	/* file size */
	FILE *fp;
	char *line = NULL;
	size_t len = 0;
	ssize_t read;

	fp = fopen(file, "r");
	if (fp == NULL)
		exit(-1);

	fseek(fp, 0L, SEEK_END);
	fileSize = ftell(fp);

	fclose(fp);

	/* create pipe */
	if(pipe(pipes) == -1) {
		printf("pipe() error");
		return -1;
	}

	/* fork */
	int i;
	pid_t *child_ids = malloc(sizeof(pid_t) * processCount);
	for(i = 0; i < processCount; i++){
		if((child_ids[i] = fork()) < 0){
			printf("fork error\n");
			free(child_ids);
			return 1;
		}
		/* child */
		else if(child_ids[i] == 0){
			process((void*) i);
			free(child_ids);
			return 0;
		}
	}

	/* parent */
	int status;
	for(i = 0; i < processCount; i++){
		waitpid(child_ids[i], &status, 0);
	}
	free(child_ids);


	/* print result */
	print_result();

	return 0;
}

void* process(void *arg) {
	int process_id = (int)arg;

	int *result = malloc(sizeof(int) * keywordCount);
	memset(result, 0, sizeof(int) * keywordCount);

	int start = fileSize / processCount * process_id;
	int end = fileSize / processCount * (process_id + 1);
	int i;

	if(fileSize < processCount) {
		start = process_id;
		end = process_id + 1;
		if(start >= fileSize) return;
	}
	if(end > fileSize) end = fileSize;

	FILE *f = fopen(file, "r");
	if(!f) return;

	for(i = 0; i < keywordCount; i++){
		char *keyword = keywords[i];
		int keyword_len = strlen(keyword);

		fseek(f, start, SEEK_SET);

		int offset = start;

		while(offset < end && !feof(f)) {
			int keyword_i;
			int find = 0;
			for(keyword_i = 0; keyword_i < keyword_len; keyword_i++) {
				if(keyword[keyword_i] != fgetc(f)) break;
			}

			if(keyword_i == keyword_len)
				result[i]++;

			offset++;

			fseek(f, offset, SEEK_SET);
		}


	}

	write(pipes[1], result, sizeof(int) * keywordCount);
}


void print_result() {
	int i, keyword_i;
	int *buf = malloc(sizeof(int) * keywordCount);
	int *result = malloc(sizeof(int) * keywordCount);
	memset(result, 0, sizeof(int) * keywordCount);

	for(i = 0; i < processCount; i++){
		read(pipes[0], buf, sizeof(int) * keywordCount);
		for(keyword_i = 0; keyword_i < keywordCount; keyword_i++)
			result[keyword_i] += buf[keyword_i];

	}

	for(keyword_i = 0; keyword_i < keywordCount; keyword_i++)
		printf("%s : %d\n", keywords[keyword_i], result[keyword_i]);
}
