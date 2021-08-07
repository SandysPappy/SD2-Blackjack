from website import create_app

# this file creates the app by calling create_app in website > init.py

app = create_app()

# only if we run this file (not if we import this file), will we execute this line
# prevents the app from running if you accidentally import main from another file
if __name__ == '__main__':
    app.run(debug=True)


# https://youtu.be/dam0GPOAvVI?t=3848

# https://youtu.be/dam0GPOAvVI?t=6100