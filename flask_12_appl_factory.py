# Instead of creating a Flask instance globally, you will create it inside a function. This function is known as the application factory. Any configuration, registration, and other setup the application needs will happen inside the function, then the application will be returned.
# The Application Factory
#


import asyncio

<<<<<<< HEAD
# refer to flask_12_flaskr application
=======
@unsync
async def unsync_async():
    await asyncio.sleep(0.1)
    return 'I like decorators'

print(unsync_async().result())
>>>>>>> 939acde9c81e7c2c6123fa83100c21a8dd38cb08
