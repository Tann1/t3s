CC=g++
INCLUDES=./headers 
GAME_LOGIC_INCLUDES=./game_logic/headers
SOURCES=./sources
GAME_LOGIC_SOURCES=./game_logic/sources
APP=gui_rps_app.cpp
WXLIB=`wx-config --cxxflags --libs`
OUT=rps
default:  $(SOURCES)/*.cpp $(GAME_LOGIC_SOURCES)/*.cpp $(APP)
	$(CC) $(GAME_LOGIC_SOURCES)/*.cpp $(SOURCES)/*.cpp $(APP) -I$(INCLUDES) -I$(GAME_LOGIC_INCLUDES)  $(WXLIB) -o $(OUT)

clean:
	rm $(OUT)
