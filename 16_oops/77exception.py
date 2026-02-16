try:        
    number=int(input("Enter a number : "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("Somethng Went wrong")

finally:
    print("DO some cleanup here")