from controllers.user_controller import user_routes

app = Bottle()
app.mount('/users', user_routes)