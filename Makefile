SRC=./source
OBJ=./objects

NAME = CN.out
CC = g++
CPPFILES = $(foreach D, $(SRC), $(wildcard $(D)/*.cpp))
OBJECTS = $(patsubst $(SRC)/%.cpp,$(OBJ)/%.o,$(CPPFILES))

all: $(NAME)

run:
	python3 Interface.py

$(NAME): $(OBJECTS)
	$(CC) $(OBJECTS) -o $@ -lginac -lcln


$(OBJ)/%.o: $(SRC)/%.cpp
	$(CC) -c $< -o $@ 

clean-all: clean
	@rm -rf $(OBJ)/*.o $(OBJ)/*.d

clean:
	@rm -rf *.o *.d *.txt 
