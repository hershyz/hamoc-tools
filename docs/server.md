<h1>Server, Self-Hosting, and Adding Functions</h1>
<p>
  The entire backend of this project is a Python Flask server, hosted on a <a href="http://hershyz.pythonanywhere.com">PythonAnywhere</a> server.
  
  <strong>Server Requirements</strong>
  <pre>
    <a href="https://www.python.org/downloads/">Python >=  3.7.6</a>
    Flask      (pip install flask)
    Yfinance   (pip install yfinance)
    
    All packages can be installed with pip (included with Python by default).
    Flask and Yfinance have their own dependencies, but should be installed along with their respective pip commands.
  </pre>
  
  <strong>Directory Structure</strong>
  <pre>
    /server (root)
      |- options      (data storage for options)
      |- stocks       (data storage for stocks)
      |- ...
      |- app.py       (API entry point, Flask endpoint handler)
      |- ...
      |- symbols.txt  (storage for target stock symbols)
      |- ...
      |- (other source files)
  </pre>
  
  <strong>Self-Hosting</strong>
  <pre>
    cd server
    python app.py
    ...
    Flask will provide a localhost HTTP address, which can then be tested from cURL or the <a href="https://github.com/hershyz/hamoc-tools/blob/main/docs/api-wrapper.md">api wrapper</a>.
  </pre>
 </p>
 
 <p>
   <strong>Adding Functions</strong>
    <pre>
      All functions are stored as endpoints, which are routed by Flask.
      The HTTP methods to an endpoint can be specified, GET for fetching data, POST for doing anything else server-side.
      ...
      Adding an endpoint to the <a href="https://github.com/hershyz/hamoc-tools/blob/main/server/app.py">main file</a> can be done like so:
    </pre>
</p>

```python
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
```

   <strong>Hosting Elsewhere</strong>
   <pre>
    The code is already deployed to a <a href="http://hershyz.pythonanywhere.com">PythonAnywhere</a> server,
    but Flask webservers can be deployed to GCP, AWS, Azure, Heroku, etc...
    A requirements file can be found <a href="https://github.com/hershyz/hamoc-server/blob/main/requirements.txt">here</a>.
    Additionally, some services may require a <a href="https://devcenter.heroku.com/articles/procfile">procfile</a>.
   </pre>
