#
# Makefile	$Revision: 1.1 $	$Date: 2002/11/10 15:10:44 $	MB
# 

CC		= gcc
CCOPTS	= -g -W -ansi -O3 -march=pentium -static
LFLAGS	=

LIBS	= -lstdc++

SOURCES	= \
	Enema.cpp \
	main.cpp

HEADERS	= \

OBJS	= $(patsubst %.cpp, %.o, $(SOURCES))
DEPS	= $(patsubst %.cpp, %.d, $(SOURCES))

MAIN	= main.exe

%.d : %.cpp
	@$(CC) -MM $< -o $@

%.o : %.cpp
	$(CC) $(CCOPTS) -c $< -o $@

all: $(MAIN)

clean:
	@-rm $(OBJS)
	@-rm $(DEPS)
	@-rm $(MAIN)
	
$(MAIN): $(DEPS) $(OBJS)
	$(CC) -o $(MAIN) $(LFLAGS) $(OBJS) $(LIBS)

include $(DEPS)
