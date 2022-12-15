import eel

# Set web files folder
eel.init('web')

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)
   # Call a Javascript function

eel.start('index.html', size=(300, 200))  # Start
