#include <stdio.h>
#include <stdlib.h>
#include <error.h>
#include <errno.h>
#include <netdb.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>


static int get_host(const char *hostname){
	struct hostent *host = NULL;	
	host = gethostbyname(hostname);
	
	if ( host == NULL ){
		fprintf(stderr,"gethostbyname:%s\b",strerror(errno));
		return -1;
	}
	printf("IP=%s\n",inet_ntoa(*((struct in_addr *)host->h_addr_list[0])));
	return 0;
}


int main(int argc,char *argv){
	get_host("www.youku.com");

	return 0;
}
