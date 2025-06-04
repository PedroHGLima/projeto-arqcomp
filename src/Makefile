CC = gcc
CFLAGS = -Wall -mavx -O3 -fopenmp

DGEMM_EXEC = ../bin/dgemm.exe
DGEMM_OBJS = main.o dgemm.o

TARGETS = $(DGEMM_EXEC)
OBJS = $(DGEMM_OBJS)

all: $(TARGETS)

$(TARGETS): $(OBJS)
	$(CC) -o $@ $^ $(CFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(TARGETS) $(OBJS)

.PHONY: all clean
