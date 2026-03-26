try:
    result = 10/2
except TypeError as error:
    print(error)
except ZeroDivisionError as error:
    print("batatinhas")


#else:
    #print("conseguimos dividor!")
finally:
    print("concluido")