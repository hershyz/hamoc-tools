# HTTP methods can be specified in the endpoint, GET for recieving data, POST for anything else server-side related.



# returning data to the client:
@app.route("/my_test_endpoint", methods=["GET"])
def my_test_endpoint():
  return "hello"
    


# we can recieve data from the client as well, this is an example of an endpoint recieving JSON data through POST requests:
@app.route("/create_file", methods=["POST"])
def create_file():
  
  try:
    data = request.get_json()                   # fetch the raw JSON data from the client request
    filename = data['filename']                 # fetching specific fields from the JSON
    extension = data['extension']
    f = open(filename + "." + extension, "a")   # perform the action
    return "success"                            # server response to the client
    
  except:
    return "error creating file"                # failing server response to the client
