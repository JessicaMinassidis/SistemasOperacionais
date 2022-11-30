import ctypes

strings = ['Sistemas Operacionais', 'Centro Universitário Senac', 'Reversão de Textos', 'Bênção']

for str in strings:
    lib_inverter = ctypes.CDLL("./libinverter.so")
    lib_inverter.inverter.argtypes = [ctypes.c_char_p]
    lib_inverter.inverter.restype = ctypes.c_char_p
    str_tratada = str.encode('utf8')
    string_invertida=lib_inverter.inverter(str_tratada)
    print (string_invertida.decode('utf8', 'strict'))
