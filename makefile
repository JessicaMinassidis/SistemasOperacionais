all: libinverter.so

libinverter.so: inverter.o
	gcc -shared inverter.o -o libinverter.so
inverter.o:
	gcc -c inverter.c
clean:
	rm *.o *.so


