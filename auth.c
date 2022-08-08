#include <stdio.h>
#include <string.h>

void split(char *inputArr, char **outputArr, char *delim)
{

    char *temp;
    temp = strtok(inputArr, delim);

    for (int i = 0; temp != NULL; i++)
    {
        outputArr[i] = temp;
        temp = strtok(NULL, delim);
    }
}

int main(int argc, char **argv)
{

    /* check for proper arguments */

    if (argc == 4)
    {
        if (strcmp(argv[1], "register") == 0)
        {
            FILE *fp = fopen("auth.txt", "a");
            if (fp == NULL)
            {
                printf("err 500 %s", "auth.txt");
                return -1;
            }

            char *arg1 = argv[1];
            char *email = argv[2];
            char *password = argv[3];

            fprintf(fp, "%s🇹🇷%s\n", email, password);

            fclose(fp);
            printf("200\n");
            return 0;
        }
        if (strcmp(argv[1], "login") == 0)
        {

            /*---------main code starts here----------*/
            FILE *myScriptFile;
            myScriptFile = fopen("auth.txt", "r");

            /* read txt file and split into array like java split() */

            int bufferLen = 100;
            char buffer[bufferLen];

            char *splitArr[100];

            int passed = 0;
            while (fgets(buffer, bufferLen, myScriptFile) != NULL)
            {

                split(buffer, splitArr, "🇹🇷");

                if (strcmp(argv[2], strtok(splitArr[0], "\n")) == 0)
                {
                    /* first credential passed */
                    if (strcmp(argv[3], strtok(splitArr[1], "\n")) == 0)
                    {
                        /* password passed */
                        passed = 1;
                        break;
                    }
                    else
                    {
                        passed = 2;
                        break;
                    }
                }
            }
            fclose(myScriptFile);
            if (passed == 1)
            {
                printf("200\n");
            }
            if (passed == 2)
            {
                printf("403p\n");
            }
            if (passed == 0)
            {
                printf("403e\n");
            }
        }
    }
    else
    {
        printf("NONE");
    }

    return 0;
}
