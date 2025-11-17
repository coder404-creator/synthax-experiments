
choice = input("do you want to run this command? ").lower()

if choice == 'yes':
    for i in range(10):
        print('*' * i)
else:
    print("CLOSING")
