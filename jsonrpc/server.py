# from jsonrpcserver import Success, method, serve

# @method
# def ping():
#     return Success("pong")

# if __name__ == "__main__":

#     serve()


from jsonrpcserver import method, serve, Success

@method
def hello(name):
    return Success(f"Hello, {name}!")

serve()
