CC=g++
INCLUDES=./headers
SOURCES=./sources
APP=gui_rps_app.cpp
WXLIB=`wx-config --cxxflags --libs`
OUT=rps
default: $(INCLUDES)/*.h $(SOURCES)/*.cpp $(APP)
	$(CC) $(SOURCES)/*.cpp $(APP) -I$(INCLUDES) $(WXLIB) -o $(OUT)

clean:
	rm $(OUT)
