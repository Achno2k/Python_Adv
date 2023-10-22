while True:
    try:
        age = int(input("Enter your age: "))
        10/age
    except ValueError:
        print("Age can only be an integer")
    except ZeroDivisionError:
        print("0 is not valid")
    else:
        print("age")
        print("Thank You")
        break
    finally:
        print("gonna run regardless")


def div(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print("oops")
        print(err)

print(div(3, "3"))