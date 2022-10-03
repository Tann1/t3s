

INCLUDES=./headers/
SOURCES=./sources
MAIN=main.cpp
OUT=$(basename $(MAIN) .cpp)


default: $(MAIN) $(SOURCES)/*.cpp $(INCLUDES)enum/*.h $(INCLUDES)*.h
	g++ -o $(OUT) $(MAIN) $(SOURCES)/*.cpp -I$(INCLUDES)

clean:
	rm $(OUT)
