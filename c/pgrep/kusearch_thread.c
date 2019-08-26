#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <pthread.h>
#include "kusearch_thread.h"

void* thread(void *arg);
void print_result();

int main(int argc, char* argv[])
{
	/* init arguments */
	if(argc < 4 || atoi(argv[2]) < 1) {
		printf("Usage: ./search path processes keyword 1 2 3 \n");
		exit(1);
	}
	file = argv[1];
	threadCount = atoi(argv[2]);
	keywordCount = argc - 3;
	keywords = argv + 3;

	resultCount = (int*)malloc(sizeof(int) * keywordCount);
	memset(resultCount, 0, sizeof(int) * keywordCount);


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

	/* thread */
	int i;
	pthread_t *thread_ids = malloc(sizeof(thread_ids) *  threadCount);

	for(i = 0; i < threadCount; i++)
		pthread_create(&thread_ids[i], NULL, thread, (void *)i);

	int status;
	for(i = 0; i < threadCount; i++)
		pthread_join(thread_ids[i], (void **)&status);


	/* print result */
	print_result();

	return 0;
}

void* thread(void *arg) {
	int process_id = (int)arg;

	int start = fileSize / threadCount * process_id;
	int end = fileSize / threadCount * (process_id + 1);
	int i;

	if(fileSize < threadCount) {
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

			if(keyword_i == keyword_len){
				resultCount[i]++;
			}
			offset++;

			fseek(f, offset, SEEK_SET);
		}


	}
}


void print_result() {
	int keyword_i;

	for(keyword_i = 0; keyword_i < keywordCount; keyword_i++)
		printf("%s : %d\n", keywords[keyword_i], resultCount[keyword_i]);
}
