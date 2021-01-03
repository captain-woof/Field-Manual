# Useful built-ins

### String Manipulation Functions
    ```
    char *strcpy (char *dest, char *src);
    Copy src string into dest string.

    char *strncpy(char *string1, char *string2, int n);
    Copy first n characters of string2 to stringl .

    int strcmp(char *string1, char *string2);
    Compare string1 and string2 to determine alphabetic order.

    int strncmp(char *string1, char *string2, int n);
    Compare first n characters of two strings.

    int strlen(char *string);
    Determine the length of a string.

    char *strcat(char *dest, const char *src);
    Concatenate string src to the string dest.

    char *strncat(char *dest, const char *src, int n);
    Concatenate n chracters from string src to the string dest.

    char *strchr(char *string, int c);
    Find first occurrence of character c in string.

    char *strrchr(char *string, int c);
    Find last occurrence of character c in string.

    char *strstr(char *string2, char string*1);
    Find first occurrence of string string1 in string2.

    char *strtok(char *s, const char *delim) ;
    Parse the string s into tokens using delim as delimiter.
    ```

### Memory Management Functions
    ```
    void *calloc(int num elems, int elem_size);
    Allocate an array and initialise all elements to zero .

    void free(void *mem address);
    Free a block of memory.

    void *malloc(int num bytes);
    Allocate a block of memory.

    void *realloc(void *mem address, int newsize);
    Reallocate (adjust size) a block of memory.
    ```

### Buffer Manipulation
    ```
    void* memcpy(void* s, const void* ct, int n);
    Copies n characters from ct to s and returns s. s may be corrupted if objects overlap.

    int memcmp(const void* cs, const void* ct, int n);
    Compares at most (the first) n characters of cs and ct, returning negative value if cs<ct, zero if cs==ct, positive value if cs>ct.

    void* memchr(const void* cs, int c, int n);
    Returns pointer to first occurrence of c in first n characters of cs, or NULL if not found.

    void* memset(void* s, int c, int n);
    Replaces each of the first n characters of s by c and returns s.

    void* memmove(void* s, const void* ct, int n);
    Copies n characters from ct to s and returns s. s will not be corrupted if objects overlap.
    ```
    
### File Functions
  ```
  fopen ("file_name", "mode");
  Returns a file pointer.
	
  fclose (file_pointer);
  Closes the stream.
	
  fputc(char, file_pointer);
  It writes a character to the file pointed to by file_pointer.
	
  fputs(str, file_pointer);
  It writes a string to the file pointed to by file_pointer.
	
  fprintf(file_pointer, str, variable_lists);
  It prints a string to the file pointed to by file_pointer. The string can optionally include format specifiers and a list of variables variable_lists.
	
  fgetc(file_pointer);
  It returns the next character from the file pointed to by the file pointer. When the end of the file has been reached, the EOF is sent back.
  
  fgets(buffer, n, file_pointer);
  It reads n-1 characters from the file and stores the string in a buffer in which the NULL character '\0' is appended as the last character.
    	
  fscanf(file_pointer, conversion_specifiers, variable_adresses);
  It is used to parse and analyze data. It reads characters from the file and assigns the input to a list of variable pointers variable_adresses using conversion specifiers. Keep in mind that as with scanf, fscanf stops reading a string when space or newline is encountered.
  ```

### Character Functions

    int isalnum(int c);
    The function returns nonzero if c is alphanumeric

    int isalpha(int c);
    The function returns nonzero if c is alphabetic only

    int iscntrl(int c);
    The function returns nonzero if c is a control chracter

    int isdigit(int c);
    The function returns nonzero if c is a numeric digit

    int isgraph(int c);
    The function returns nonzero if c is any character for which either isalnum or ispunct returns nonzero.

    int islower(int c);
    The function returns nonzero if c is a lower case character.

    int isprint(int c);
    The function returns nonzero if c is space or a character for which isgraph returns nonzero.

    int ispunct(int c);
    The function returns nonzero if c is punctuation

    int isspace(int c);
    The function returns nonzero if c is space character

    int isupper(int c);
    The function returns nonzero if c is upper case character

    int isxdigit(int c);
    The function returns nonzero if c is hexa digit

    int tolower(int c);
    The function returns the corresponding lowercase letter if one exists and if isupper(c); otherwise, it returns c.

    int toupper(int c);
    The function returns the corresponding uppercase letter if one exists and if islower(c); otherwise, it returns c.

### Error Handling Functions

    void perror(const char *s);
    produces a message on standard error output describing the last error encountered.

    char *strerror(int errnum );
    returns a string describing the error code passed in the argument errnum.

